from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
import sqlite3
from functools import wraps
import math
import os
import pdfkit
import tempfile
import traceback
from datetime import datetime  # <-- added import

app = Flask(__name__)
app.secret_key = "your_secret_key"  # CHANGE THIS for security

DB_NAME = "invoices.db"

# Hardcoded admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"  # Change this for production!

# === DB INIT ===
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS invoices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                customer_email TEXT,
                invoice_number TEXT NOT NULL UNIQUE,
                invoice_date TEXT NOT NULL,
                items TEXT,
                grand_total REAL,
                notes TEXT
            )
        """)
        conn.commit()
init_db()

# === Login required decorator ===
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            flash("Please log in to access this page.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

def find_wkhtmltopdf():
    env_path = os.environ.get("WKHTMLTOPDF_PATH")
    if env_path and os.path.isfile(env_path):
        return env_path
    possible_windows = [
        r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe",
        r"C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe"
    ]
    for p in possible_windows:
        if os.path.isfile(p):
            return p
    possible_unix = [
        "/usr/local/bin/wkhtmltopdf",
        "/usr/bin/wkhtmltopdf",
        "/bin/wkhtmltopdf"
    ]
    for p in possible_unix:
        if os.path.isfile(p):
            return p
    return None

# === Custom filter for date formatting ===
@app.template_filter('datetimeformat')
def datetimeformat(value):
    try:
        dt = datetime.strptime(value, "%Y-%m-%d")
        return dt.strftime("%d/%m/%Y")
    except Exception:
        return value

# === Routes ===

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["logged_in"] = True
            flash("Logged in successfully.", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password.", "danger")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("login"))

@app.route("/invoice/<invoice_number>")
@login_required
def view_invoice(invoice_number):
    invoices_dir = "saved_invoices"
    pdf_path = os.path.join(invoices_dir, f"{invoice_number}.pdf")

    if os.path.exists(pdf_path):
        # Option 1: Send PDF directly to browser to preview
        return send_file(pdf_path, as_attachment=False, download_name=f"{invoice_number}.pdf")

        # Option 2: If you want an HTML preview, you would need to save the invoice data or render from DB
        # Then render an HTML template instead of PDF
    else:
        flash("Invoice not found.", "warning")
        return redirect(url_for("dashboard"))

@app.route("/")
@login_required
def dashboard():
    search = request.args.get("search", "").strip()
    page = int(request.args.get("page", 1))
    per_page = 10

    query = "SELECT id, customer_name, invoice_number, invoice_date, grand_total FROM invoices"
    params = []

    if search:
        query += " WHERE LOWER(customer_name) LIKE ?"
        params.append(f"%{search.lower()}%")

    query += " ORDER BY invoice_date DESC, id DESC"

    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        count_query = query.replace(
            "SELECT id, customer_name, invoice_number, invoice_date, grand_total", "SELECT COUNT(*)"
        )
        c.execute(count_query, params)
        total_count = c.fetchone()[0]

        total_pages = math.ceil(total_count / per_page)
        if page < 1:
            page = 1
        elif page > total_pages and total_pages > 0:
            page = total_pages

        query += " LIMIT ? OFFSET ?"
        params.extend([per_page, (page - 1) * per_page])
        c.execute(query, params)
        invoices = c.fetchall()

    # Metrics for dashboard summary (all invoices, no search filter)
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT COUNT(*), IFNULL(SUM(grand_total), 0) FROM invoices")
        total_invoices, total_revenue = c.fetchone()

        c.execute("""
            SELECT COUNT(*)
            FROM invoices
            WHERE strftime('%m', invoice_date) = strftime('%m', 'now') 
            AND strftime('%Y', invoice_date) = strftime('%Y', 'now')
        """)
        invoices_this_month = c.fetchone()[0]

        avg_invoice = total_revenue / total_invoices if total_invoices else 0

        # For chart: invoices per month in current year
        c.execute("""
            SELECT strftime('%m', invoice_date) AS month, COUNT(*) 
            FROM invoices 
            WHERE strftime('%Y', invoice_date) = strftime('%Y', 'now')
            GROUP BY month
            ORDER BY month
        """)
        month_data = dict(c.fetchall())
    
        # Prepare chart data keys and labels
        month_keys = [f"{i:02d}" for i in range(1, 13)]  # '01'...'12'
        chart_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        chart_data = [month_data.get(month, 0) for month in month_keys]

    # Calculate next invoice number
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT invoice_number FROM invoices ORDER BY id DESC LIMIT 1")
        last = c.fetchone()
        if last:
            try:
                last_num = int(last[0].replace("INL-", ""))
            except Exception:
                last_num = 0
            next_num = last_num + 1
        else:
            next_num = 1
        next_invoice_number = f"INL-{next_num:04d}"

    # Format metrics for display
    total_revenue_fmt = f"₦{total_revenue:,.2f}"
    avg_invoice_fmt = f"₦{avg_invoice:,.2f}"

    return render_template(
        "dashboard.html",
        invoices=invoices,
        page=page,
        total_pages=total_pages,
        search=search,
        totalInvoices=total_invoices,
        totalRevenue=total_revenue_fmt,
        invoicesThisMonth=invoices_this_month,
        avgInvoice=avg_invoice_fmt,
        chart_labels=chart_labels,
        chart_data=chart_data,
        next_invoice_number=next_invoice_number 
    )

@app.route("/generate_invoice", methods=["POST"])
@login_required
def generate_invoice():
    try:
        wk_path = find_wkhtmltopdf()
        if not wk_path:
            error_msg = (
                "wkhtmltopdf not found. Install wkhtmltopdf and ensure it's on PATH "
                "or set environment variable WKHTMLTOPDF_PATH to the executable path."
            )
            return render_template("error.html", message=error_msg), 500

        pdf_config = pdfkit.configuration(wkhtmltopdf=wk_path)

        customer_name = request.form.get("customer_name", "").strip()
        customer_email = request.form.get("customer_email", "").strip()
        invoice_date = request.form.get("invoice_date", "").strip()
        notes = request.form.get("notes", "").strip()

        descriptions = request.form.getlist("description[]")
        quantities = request.form.getlist("quantity[]")
        prices = request.form.getlist("price[]")

        if not customer_name or not invoice_date:
            flash("Customer name and invoice date are required.", "danger")
            return redirect(url_for("dashboard"))

        # Auto-generate next invoice number in format INL-0001 etc.
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute("SELECT invoice_number FROM invoices ORDER BY id DESC LIMIT 1")
            last = c.fetchone()
            if last:
                last_num = int(last[0].replace("INL-", ""))
                next_num = last_num + 1
            else:
                next_num = 1
            invoice_number = f"INL-{next_num:04d}"

        items = []
        for i in range(len(descriptions)):
            desc = descriptions[i].strip() if i < len(descriptions) else ""
            if not desc:
                continue
            try:
                qty = float(quantities[i]) if i < len(quantities) and quantities[i] != "" else 0.0
                price = float(prices[i]) if i < len(prices) and prices[i] != "" else 0.0
            except Exception:
                qty = 0.0
                price = 0.0
            total = qty * price
            items.append({
                "description": desc,
                "quantity": qty,
                "price": price,
                "total": total,
            })

        grand_total = sum(item["total"] for item in items)
        logo_url = url_for("static", filename="logo.png", _external=True)

        rendered = render_template(
            "invoice_template.html",
            customer_name=customer_name,
            customer_email=customer_email,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            items=items,
            grand_total=grand_total,
            logo_url=logo_url,
            notes=notes,
        )

        # Save PDF permanently
        invoices_dir = "saved_invoices"
        os.makedirs(invoices_dir, exist_ok=True)
        pdf_path = os.path.join(invoices_dir, f"{invoice_number}.pdf")
        pdfkit.from_string(rendered, pdf_path, configuration=pdf_config)

        # Save invoice info in DB
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute(
                """
                INSERT INTO invoices (customer_name, customer_email, invoice_number, invoice_date, items, grand_total, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    customer_name,
                    customer_email,
                    invoice_number,
                    invoice_date,
                    str(items),
                    grand_total,
                    notes,
                ),
            )
            conn.commit()

        # Send generated PDF to browser for download
        return send_file(pdf_path, as_attachment=True, download_name=f"{invoice_number}.pdf")

    except Exception:
        tb = traceback.format_exc()
        return f"<h3>Server error</h3><pre>{tb}</pre>", 500

if __name__ == "__main__":
    app.run(debug=True)

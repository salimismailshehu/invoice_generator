User Authentication

You want a single admin user with a login system, right?
only single user. admin.

Should the admin credentials be hardcoded for simplicity, or do you want a user registration system to create/change admin user?
admin credentials should be hardcoded for simplicity

Invoice Storage & Search
You want all generated invoices saved to a database (SQLite)?
yes should be saved in to a database
Should the search be by invoice number, customer name, date range, or other fields?
search by billing name only
Do you want pagination for the invoice list if it grows large?
yes add pagination

Dashboard Metrics
What kind of metrics are you imagining? 
use these
Total invoices generated (all-time or filtered period)
Total revenue (sum of all invoice totals)
Number of invoices generated this month/week/day
Average invoice amount
Maybe some charts (bar chart over time,)

Invoice Management
Should the admin be able to download/view invoices from the dashboard/history?
not download just view.
Do you want ability to delete invoices or edit them after creation?
no deletion 
Should invoices be stored as PDF files on disk or only in DB?
just chose the best option

UI & UX
Do you want a modern Bootstrap-based UI for dashboard and forms?
give me modern Bootstrap-based UI clean and professioinal
Should the invoice creation form be part of the dashboard or separate page?
let it be on the dashboard page
Would you want search/filter fields above the invoice table?
yes above but just search.

well additional features later. lets get this going step by step. 

Additional Features
Emailing invoices automatically?
Exporting invoice data (CSV/Excel)?
User activity logs?
Multi-currency or tax calculation?

I built an invoice generation app with Flask that lets users create, manage, and preview invoices as PDFs. What are practical ways I can monetize this app? i want to also create a landing page for it.
Landing Page Essentials to Convert Visitors
Clear Value Proposition
What your app does (“Generate professional invoices in seconds”)
Who it’s for (freelancers, small businesses, agencies)

Main Features
Highlight ease of use, PDF generation, customization options
Emphasize benefits like saving time, professional branding

Call-to-Action (CTA)
“Try for free,” “Create your first invoice now,” “Start your free trial”
Place CTAs above the fold and at multiple points on the page

Visuals & Demo
Screenshot or short video/gif showing the app in action
Show a sample invoice PDF preview

Pricing Section
Brief overview of free vs paid plans (if applicable)
Link to detailed pricing

Testimonials or Social Proof
If you have beta users or early feedback, showcase it

Contact or Support Info
Make it easy to get help or ask questions

Mobile-Friendly & Fast
Landing page should load quickly and look good on phones



Demo / Free Use:
Is the demo on the landing page a fully functional basic invoice creator but with limited customization options?
yes 
Can users save their invoices or only generate and download/export them temporarily?
only generate and download 

Premium Package:
For the premium package, you mentioned custom design + hosting — does this mean you build a tailored invoice template and set up the app for each client individually?
yes 
How do you plan to handle payments for this service? Online payment? Offline bank transfer? WhatsApp payment?
mainly offline bank transfer or crypto payments
Will premium clients get access to the admin login/dashboard, or is that just for you as the service provider?
premium clients get access to admin login/dashboard
Will the dashboard allow premium clients to manage multiple invoices, clients, or other features?
yes 

Scalability & Onboarding:
How do you plan to onboard new premium clients? Will they fill a form with requirements on the site or contact you directly via phone/WhatsApp/email?
they will fill form on the site or contact via phone/WhatsApp/email
What’s the expected turnaround time for creating their custom invoice system?
less than 1hr

Pricing Model:
Is the minimum N15,000 a one-time fee for the initial setup and hosting?
yes. 
Will you charge recurring fees (monthly/annual) for hosting and support?
yes annually. i will charge when clients what other features

Technical Setup:
Will you host these custom invoices on a shared server or separate environments per client?
preferablely separate enviornment, but which is the best or this?
How will you handle data security and backups for each client’s data?
maybe if the clients request the option


Which pagination style do you prefer?
page numbers with "Prev"/"Next" links?
For filtering/search, should it be case-insensitive substring match on billing name?
yes 
What date format do you prefer for invoices? (Your existing code uses strings for dates.)
DD/MM/YYYY
For charts, do you prefer a simple JavaScript library (Chart.js is lightweight and popular)?
yes simple JavaScript library

when i click generate the error 127.0.0.1 - - [09/Aug/2025 13:05:06] "POST / HTTP/1.1" 405 -, also on the fom

for the dashboard.html invoice maker, replace it with this form including design and functions 

<div class="row g-3 mb-3">
      <div class="col-md-6">
        <label class="form-label small-muted">Invoice #</label>
        <input name="invoice_number" class="form-control" required placeholder="{{ next_invoice_number }}">
      </div>

<!doctype html>
<html lang="en">
<head>
    <title>Invoice Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            background-color: #f3f6f9;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .card-soft {
            border: none;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.05);
            border-radius: 12px;
            background: #fff;
            padding: 2rem;
            margin-bottom: 2rem;
        }
        input, select, textarea {
            border-radius: 10px;
            border: 1px solid #ddd;
            padding: 10px 15px;
            transition: border-color 0.3s ease;
        }
        input:focus, textarea:focus {
            border-color: #4e89ff;
            box-shadow: 0 0 8px rgba(78, 137, 255, 0.4);
            outline: none;
        }
        .btn-primary {
            border-radius: 50px;
            padding: 10px 25px;
            box-shadow: 0 4px 10px rgba(78, 137, 255, 0.3);
            transition: background-color 0.3s ease;
        }
        .btn-primary:hover {
            background-color: #3c72e0;
        }
        .total-box {
            background: linear-gradient(90deg, #f8fbff, #ffffff);
            border-radius: 12px;
            padding: 12px 16px;
            box-shadow: 0 6px 18px rgba(14,30,37,0.04);
            font-weight: 600;
            color: #2c3e50;
        }
        @media (max-width: 576px) {
            .form-label {
                font-size: 0.9rem;
            }
            .btn {
                width: 100%;
                margin-bottom: 0.75rem;
            }
            .d-flex.gap-2.align-items-center.mt-2 {
                flex-direction: column !important;
                align-items: stretch !important;
            }
            #itemsContainer .item-row {
                flex-wrap: wrap;
                gap: 0.5rem;
            }
            #itemsContainer .item-row > * {
                flex: 1 1 100% !important;
            }
            #itemsContainer .item-row button {
                width: 100%;
            }
        }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container-fluid">
        <a class="navbar-brand" href="{{ url_for('dashboard') }}">Invoice Admin</a>
        <div>
            <a href="{{ url_for('logout') }}" class="btn btn-outline-light">Logout</a>
        </div>
    </div>
</nav>

<div class="container my-4">

    <h2 class="mb-4">Dashboard</h2>

    <!-- Flash messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        {% for category, message in messages %}
          <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          </div>
        {% endfor %}
      {% endif %}
    {% endwith %}

    <!-- Metrics Card -->
<div class="card-soft">
    <div class="row gy-3">
        <div class="col-6 col-md-3">
            <div class="p-3 bg-light rounded-3 text-center shadow-sm">
                <h5 class="mb-1">Total Invoices</h5>
                <div id="totalInvoices" class="fs-4 fw-bold">{{ totalInvoices }}</div>
            </div>
        </div>
        <div class="col-6 col-md-3">
            <div class="p-3 bg-light rounded-3 text-center shadow-sm">
                <h5 class="mb-1">Total Revenue</h5>
                <div id="totalRevenue" class="fs-4 fw-bold">{{ totalRevenue }}</div>
            </div>
        </div>
        <div class="col-6 col-md-3">
            <div class="p-3 bg-light rounded-3 text-center shadow-sm">
                <h5 class="mb-1">Invoices This Month</h5>
                <div id="invoicesThisMonth" class="fs-4 fw-bold">{{ invoicesThisMonth }}</div>
            </div>
        </div>
        <div class="col-6 col-md-3">
            <div class="p-3 bg-light rounded-3 text-center shadow-sm">
                <h5 class="mb-1">Average Invoice Amount</h5>
                <div id="avgInvoice" class="fs-4 fw-bold">{{ avgInvoice }}</div>
            </div>
        </div>
    </div>
</div>


    <!-- Chart Card -->
    <div class="card-soft">
        <canvas id="invoiceChart"></canvas>
    </div>

    <!-- Invoice Creation Form Card -->
    <div class="card-soft">
        <h4 class="mb-3">📄 Create Invoice</h4>
        <p class="small-muted mb-4">Soft, friendly form — add items and get a PDF invoice.</p>

        <form action="{{ url_for('generate_invoice') }}" method="POST" id="invoiceForm">
            <div class="row g-3 mb-3">
                <div class="col-md-6">
                    <label class="form-label small-muted">Customer Name</label>
                    <input name="customer_name" class="form-control" required placeholder="e.g. Alhaji Musa">
                </div>
                <div class="col-md-6">
                    <label class="form-label small-muted">Customer Email</label>
                    <input name="customer_email" class="form-control" type="email" placeholder="optional@example.com">
                </div>
            </div>

            <div class="row g-3 mb-3">
                <div class="col-md-6">
                    <label class="form-label small-muted">Invoice Number</label>
                    <input name="invoice_number" class="form-control" required placeholder="{{ next_invoice_number }}" readonly style="background-color:#e9ecef; cursor:not-allowed;">
                </div>
                <div class="col-md-6">
                    <label class="form-label small-muted">Invoice Date</label>
                    <input name="invoice_date" class="form-control" type="date" required>
                </div>
            </div>

            <h6 class="mt-3 mb-2">Items</h6>
            <div id="itemsContainer">
                <div class="item-row d-flex gap-2 align-items-center mb-3 flex-wrap">
                    <input name="description[]" class="form-control flex-grow-1" placeholder="Item description" required>
                    <input name="quantity[]" class="form-control" type="number" min="1" step="1" value="1" style="width:100px">
                    <input name="price[]" class="form-control" type="number" min="0" step="0.01" value="0.00" style="width:140px">
                    <button type="button" class="btn btn-outline-danger btn-sm" onclick="removeRow(this)">Remove Item - X</button>
                </div>
            </div>

            <div class="d-flex gap-2 align-items-center mt-2 flex-wrap">
                <button type="button" class="btn btn-outline-primary btn-pill" id="addItemBtn">Add Item - +</button>
                <div class="ms-auto total-box">
                    <div class="small-muted">Grand total</div>
                    <div style="font-size:1.25rem; font-weight:600">₦ <span id="grandTotal">0.00</span></div>
                </div>
            </div>

            <div class="mt-4">
                <label class="form-label small-muted">Notes (optional)</label>
                <textarea name="notes" class="form-control" rows="2" placeholder="E.g. Payment within 7 days"></textarea>
            </div>

            <div class="mt-4 text-end">
                <button type="submit" class="btn btn-primary btn-pill px-4">Generate PDF</button>
            </div>
        </form>
    </div>

    <!-- Search Form Card -->
    <div class="card-soft">
        <form class="mb-0" method="GET" action="{{ url_for('dashboard') }}">
            <div class="input-group">
                <input type="text" name="search" class="form-control" placeholder="Search by Billing Name" value="{{ search }}">
                <button class="btn btn-primary" type="submit">Search</button>
            </div>
        </form>
    </div>

    <!-- Invoice Table Card -->
    <div class="card-soft">
        <div class="table-responsive">
            <table class="table table-bordered table-hover align-middle mb-0">
                <thead class="table-primary">
                    <tr>
                        <th>Invoice #</th>
                        <th>Billing Name</th>
                        <th>Invoice Date</th>
                        <th>Grand Total</th>
                    </tr>
                </thead>
                <tbody>
                    {% if invoices %}
                        {% for inv in invoices %}
                        <tr>
                            <td>{{ inv[2] }}</td>
                            <td>{{ inv[1] }}</td>
                            <td>{{ inv[3] }}</td>
                            <td>₦{{ "%.2f"|format(inv[4]) }}</td>
                        </tr>
                        {% endfor %}
                    {% else %}
                        <tr><td colspan="4" class="text-center">No invoices found.</td></tr>
                    {% endif %}
                </tbody>
            </table>
        </div>

        <!-- Pagination -->
        <nav class="mt-3">
            <ul class="pagination justify-content-center mb-0">
                <li class="page-item {% if page <= 1 %}disabled{% endif %}">
                    <a class="page-link" href="{{ url_for('dashboard', search=search, page=page-1) }}">Prev</a>
                </li>
                {% for p in range(1, total_pages + 1) %}
                    <li class="page-item {% if p == page %}active{% endif %}">
                        <a class="page-link" href="{{ url_for('dashboard', search=search, page=p) }}">{{ p }}</a>
                    </li>
                {% endfor %}
                <li class="page-item {% if page >= total_pages %}disabled{% endif %}">
                    <a class="page-link" href="{{ url_for('dashboard', search=search, page=page+1) }}">Next</a>
                </li>
            </ul>
        </nav>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

<script>
     function recalc() {
        let grand = 0;
        document.querySelectorAll('#itemsContainer .item-row').forEach(row => {
            const q = parseFloat(row.querySelector('input[name="quantity[]"]').value) || 0;
            const p = parseFloat(row.querySelector('input[name="price[]"]').value) || 0;
            grand += q * p;
        });
        document.getElementById('grandTotal').textContent = grand.toFixed(2);
    }

    document.getElementById('addItemBtn').addEventListener('click', () => {
        const container = document.getElementById('itemsContainer');
        const div = document.createElement('div');
        div.className = 'item-row d-flex gap-2 align-items-center mb-3 flex-wrap';
        div.innerHTML = `
            <input name="description[]" class="form-control flex-grow-1" placeholder="Item description" required>
            <input name="quantity[]" class="form-control" type="number" min="1" step="1" value="1" style="width:100px">
            <input name="price[]" class="form-control" type="number" min="0" step="0.01" value="0.00" style="width:140px">
            <button type="button" class="btn btn-outline-danger btn-sm" onclick="removeRow(this)">✕</button>
        `;
        container.appendChild(div);
    });

    function removeRow(btn) {
        const row = btn.closest('.item-row');
        if (document.querySelectorAll('#itemsContainer .item-row').length > 1) {
            row.remove();
        } else {
            row.querySelector('input[name="description[]"]').value = '';
            row.querySelector('input[name="quantity[]"]').value = 1;
            row.querySelector('input[name="price[]"]').value = '0.00';
        }
        recalc();
    }

    document.addEventListener('input', (e) => {
        if (e.target.matches('input[name="quantity[]"], input[name="price[]"]')) recalc();
    });

    // initial calc
    recalc();

    // Placeholder Chart.js bar chart
    const ctx = document.getElementById('invoiceChart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: 'Invoices per Month',
                backgroundColor: 'rgba(13, 110, 253, 0.7)',
                borderColor: 'rgba(13, 110, 253, 1)',
                borderWidth: 1,
                data: [3, 7, 4, 6, 9, 5, 7, 6, 4, 3, 2, 1]
            }]
        },
        options: {
            scales: { y: { beginAtZero: true } }
        }
    });
</script>

</body>
</html>



from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
import sqlite3
from functools import wraps
import math
import os
import pdfkit
import tempfile
import traceback

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
    
    # Prepare chart data (12 months)
    chart_labels = [f"{i:02d}" for i in range(1,13)]
    chart_data = [month_data.get(month, 0) for month in chart_labels]

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

    return render_template(
        "dashboard.html",
        invoices=invoices,
        page=page,
        total_pages=total_pages,
        search=search,
        total_invoices=total_invoices,
        total_revenue=total_revenue,
        invoices_this_month=invoices_this_month,
        avg_invoice=avg_invoice,
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



lets improve the UI. Dont change layout and functions. we just need improve the UI. let do the following:
1. let have section on like cards to easily see the sections. 
2. let make it soft and appealing not too ridged
3. let make more mobile friendly
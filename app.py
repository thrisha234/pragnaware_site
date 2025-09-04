from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import sqlite3
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Ensure database exists
DB_PATH = "database.db"
if not os.path.exists(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            company TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.context_processor
def inject_globals():
    # Company brand colors; adjust if your logo hex codes differ
    return {
        "BRAND_PRIMARY": "#0768FF",   # Blue
        "BRAND_ACCENT": "#10B981",    # Green
        "COMPANY_NAME": "Pragnaware Solutions"
    }

@app.route("/")
def home():
    return render_template("index.html", page="home")

@app.route("/about")
def about():
    return render_template("about.html", page="about")

@app.route("/services")
def services():
    return render_template("services.html", page="services")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Collect form data
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        company = request.form.get("company")
        message = request.form.get("message")  # match textarea name

        # Store in SQLite
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            INSERT INTO contacts (name, email, phone, company, message)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, phone, company, message))
        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    return render_template("contact.html", page="contact")

# Optional: serve a favicon if you place one at static/assets/icons/favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'assets/icons/favicon.ico', mimetype='image/vnd.microsoft.icon')

# Optional: Admin page to view submissions
@app.route("/admin/contacts")
def view_contacts():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, name, email, phone, company, message FROM contacts ORDER BY id DESC")
    contacts = c.fetchall()
    conn.close()
    return render_template("admin_contacts.html", contacts=contacts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session management

# Google Apps Script Web App URL
SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzFL8Qh2G7ySCZ1uSyfihKZJI0XL7de6dMmN0TKZQxzrlixQ5Y625MRv0243JfgRHcN/exec"

# Dummy credentials for login
USER_CREDENTIALS = {"admin": "ksrct"}

@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", username=session["user"])

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session["user"] = username  # Set session
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/update_qr", methods=["POST"])
def update_qr():
    if "user" not in session:
        return jsonify({"error": "Unauthorized access"}), 403

    data = request.json
    old_qr = data.get("oldQR")
    new_qr = data.get("newQR")

    if not old_qr or not new_qr:
        return jsonify({"error": "Missing old QR or new QR."}), 400

    # Extract mobile and event name from old QR
    try:
        mobile, event_name = old_qr.split(" - ", 1)
    except ValueError:
        return jsonify({"error": "Invalid old QR format"}), 400

    # Send extracted data to Google Apps Script
    params = {"mobile": mobile, "event": event_name, "newQR": new_qr}
    response = requests.get(SCRIPT_URL, params=params)

    if response.status_code == 200:
        return jsonify({"message": f"Updated QR Code for {mobile} in {event_name} -> {new_qr}"})
    else:
        return jsonify({"error": "Failed to update QR code. Please try again."}), 500

if __name__ == "__main__":
    app.run(debug=True)

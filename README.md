# assignQR
QR Code Scanner
Overview
A web-based QR code scanner that captures and processes QR codes to extract mobile numbers and event names, updating them via a server endpoint.
Features

Scans QR codes using device camera.
Extracts mobile number and event name from scanned data.
Supports scanning "Old QR" and "New QR" separately.
Sends scanned data to a server endpoint for updating.
Responsive UI with status feedback.

Prerequisites

Modern browser with WebRTC support (e.g., Chrome, Firefox, Safari).
Camera access enabled.
Server endpoint (/update_qr) to handle POST requests (not included).

Setup

Host the index.html file on a web server.
Ensure the server supports HTTPS for camera access.
Set up a backend to handle the /update_qr endpoint.

Usage

Open the webpage in a browser.
Click "Scan Old QR" or "Scan New QR" to start scanning.
Point the camera at a QR code.
Scanned data populates the respective input fields.
Click "Update Sheets" to send data to the server.

Dependencies

jsQR (included via CDN).

Notes

QR codes must contain a mobile number (10 digits) and event name.
The app assumes a specific QR code format for parsing.
Backend implementation for /update_qr is required for full functionality.

Limitations

No local data validation beyond basic checks.
Requires a server to process updates.
Camera access may be restricted on some devices.

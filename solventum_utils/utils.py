import frappe
import qrcode
import base64
from io import BytesIO

def generate_upi_qr(doc, method=None):
    """
    Solventum Engineering - Pro UPI QR Generator
    Triggered via hooks.py
    """
    upi_id = "9538027519@ybl"
    payee_name = "Solventum OPC Private Limited"
    amount = doc.grand_total
    
    # Construct the UPI string
    upi_url = f"upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&cu=INR"
    # URL encode the payload for the API
    # Since we are in a custom app, we can use standard imports safely
    import urllib.parse
    safe_payload = urllib.parse.quote(upi_url)

    # Use the external API - this produces a SHORT URL (~120 chars)
    # This will easily fit in the 500 character limit
    doc.payment_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={safe_payload}"

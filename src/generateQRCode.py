"""
Summary: Generate QR codes that display information about stored items in storage boxes 

Input: html link, image of contents, description of boxes

Output: QR code with box information

How to run: python generateQRCode.py
"""

import qrcode
import os

# Directory to save QR codes
base_dir = r"D:\QRCodeDatabase"
qr_dir = os.path.join(base_dir, "qr_codes")
os.makedirs(qr_dir, exist_ok=True)

# Data for your box
boxes = [
    {
        "html_url": "https://drive.google.com/uc?export=view&id=1H3m3El9h2BgDWHui5QgyVpvougd--Aia",  # Your HTML file link
        "description": "Box 1: Electronics"
    }
]

# Generate QR codes
for idx, box in enumerate(boxes, start=1):
    # Use the HTML link for the QR code
    qr_data = box['html_url']
    print(f"Generating QR code for Box {idx}: {qr_data}")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    # Save the QR code image
    qr_filename = os.path.join(qr_dir, f"box_{idx}_qrcode.png")
    img.save(qr_filename)
    print(f"QR code saved to: {qr_filename}")

print("All QR codes generated successfully!")

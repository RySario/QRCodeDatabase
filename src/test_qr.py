import qrcode
import os

# Directory to save QR codes
base_dir = r"D:\QRCodeDatabase"
qr_dir = os.path.join(base_dir, "qr_codes")
os.makedirs(qr_dir, exist_ok=True)

# Data for your box
boxes = [
    {"image_url": "https://drive.google.com/uc?export=view&id=1SijAAqoYTUc6hexQLpIvi7oPqNXx7c6V", "description": "Box 1: Electronics"}
]

# Generate QR codes
for idx, box in enumerate(boxes, start=1):
    qr_data = box['image_url']  # Only include the link
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

    qr_filename = os.path.join(qr_dir, f"box_{idx}_qrcode.png")
    img.save(qr_filename)
    print(f"QR code saved to: {qr_filename}")

print("All QR codes generated successfully!")

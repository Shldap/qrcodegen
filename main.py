import qrcode
from PIL import Image

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")

    return qr_code

def save_qr_code(qr_code, filename):
    qr_code.save(filename)

def display_qr_code(qr_code):
    qr_code.show()

def main():
    website_url = "https://www.example.com"  # Replace with your website URL

    generated_qr_code = generate_qr_code(website_url)
    save_qr_code(generated_qr_code, "qr_code.png")  # Save the QR code to a file
    display_qr_code(generated_qr_code)  # Display the QR code

if __name__ == "__main__":
    main()

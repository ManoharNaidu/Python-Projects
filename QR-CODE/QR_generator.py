import pyqrcode


# String which represents the QR code
gen_qr = input("Enter anything to generate a QR-code: ")

# Generate QR code
url = pyqrcode.create(gen_qr)

qr_name = input("Enter a name for qr-code to save: ")
# Create and save the svg file naming "myqr.svg"
#url.svg(qr_name + ".svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png(qr_name , scale = 6)

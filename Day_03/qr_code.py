import qrcode
# User to Enter data
data = input("Enter the data to be encoded: ")
img_name = input("Type the name of your code image: ")

# Create an Instance of the QRCode class from qrcode library
qrObj = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qrObj.add_data(data)
qrObj.make(fit=True)

# Create Image for the code
if len(data) == 0 or len(img_name):
    print("Empty strings are not allowed")
else:
    image = qrObj.make_image(fill_color="black", back_color="white")
    image.save("Img/{}.png".format(img_name))
    print("Code generated Successfully!")



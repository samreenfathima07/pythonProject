# install all the libraries needed
# create a func that collects the texts and converts into a QR code
# save qr code as an image
# run the func

import qrcode


def generate_qrcode(text):
    qr = qrcode.QR.code(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")


generate_qrcode("https://www.codewithtomi.com")

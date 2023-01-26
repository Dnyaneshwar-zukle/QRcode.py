import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,border=4,)
qr.add_data("https://www.instagram.com/mauli.io_/")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="orange")
img.save("Dnyaneshwar_insta.jpg")
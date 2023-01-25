import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.ERROR_CORRECT_H,
                 box_size=10,border=4,)
link=input("Enter the link for making QRcode :")
qr.add_data(link)
qr.make(fit=True)
img=qr.make_image(fill_color='white',back_color="black")
img.save('tt.png')
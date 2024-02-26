import image
import qrcode
qr=qrcode.QRCode(
    version =30,
    box_size=10,
    border=5


)
data="https://www.tinkercad.com/login?next=%2Fthings%2F6N8YeVhYVVK-daring-sango%2Feditel%3Ftenant%3Dcircuits"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")

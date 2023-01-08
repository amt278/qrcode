import qrcode

# img = qrcode.make("adham")
# img.save("qrcode.png")


qr = qrcode.QRCode()
qr.add_data('https://github.com/amt278')
qr.make()

img = qr.make_image(fill_color='white', back_color='black')
img.save("pp.jpg")

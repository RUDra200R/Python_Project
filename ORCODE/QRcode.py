import qrcode

feature = qrcode.QRCode(version=1, box_size=40, border=3)
feature.add_data("https://www.udemy.com/courses/search/?src=ukw&q=python+masterclass")
feature.make(fit=True)
img = feature.make_image(fill_color="Red", back_color="White")
img.save("MyQrcode.png")

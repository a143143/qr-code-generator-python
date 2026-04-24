import qrcode
import qrcode.image.svg as svg

factory = svg.SvgImage

data = "www.linkedin.com/in/ayisha-sahwas-713522372"

img = qrcode.make(
    data,
    image_factory=factory,
    box_size=20,   # increase size (try 20 or 30)
    border=5
)

img.save("my_qr5.svg")

print("QR Code created successfully!")

import qrcode
from qrcode.image.styledpil import StyledPilImage

qr_natura = qrcode.QRCode(error_correction= qrcode.ERROR_CORRECT_H)

qr_natura.add_data('https://www.natura.com.br/consultoria/storer')

image = qr_natura.make_image(image_factory=StyledPilImage, embeded_image_path='logo_natura.png')

image.save('qrCode_natura.png')

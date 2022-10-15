import qrcode
from PIL import Image

#invitation information
date = input("Enter event date: ")
guest = input("Enter guest name:  ")
address = input("Enter event address: ")
event = input("Enter event name: ")
host = input("Enter host name: ")

#symbol on invitation qr code
qr_logo = 'appicon.png'

logo = Image.open(qr_logo)

basewidth = 100

#image_size
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
QRcode = qrcode.QRCode(
    error_correction = qrcode.constants.ERROR_CORRECT_H
)

#qr code data from invitation information
text1 = "Invitation to " + host + "'s " + event + " on " + date + " come to " + address + " provide this at the gate."

#get text1 variable to qrcode
QRcode.add_data(text1)

#generate qrcode
QRcode.make()

#qrcode color
QRcolor = 'Black'

QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

#qrcode size
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

#save qrcode
QRimg.save(guest + '\'s_invitation_to_' + event + '.png')

#message shown when invitation get finished successfully
print('Invitation complete!')

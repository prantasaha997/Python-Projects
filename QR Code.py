import qrcode # type: ignore

#taking UPI id as a input
upi_id = input("Enter your UPI id: ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
#pa=recipent name, tn=payment message

#defining the payment

bkash_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
nagad_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
rocket_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#QR code for each payment app
bkash_qr = qrcode.make(bkash_url)
nagad_qr = qrcode.make(nagad_url)
rocket_qr = qrcode.make(rocket_url)

#Save Image
bkash_qr.save('bkash_qr.png')
nagad_qr.save('nagad_url.png')
rocket_qr.save('rocket_url.png')

#install pip
bkash_qr.show()
nagad_qr.show()
rocket_qr.show()
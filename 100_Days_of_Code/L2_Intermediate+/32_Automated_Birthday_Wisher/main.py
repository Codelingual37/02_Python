import smtplib

email = "allforcode.37@gmail.com"
receiver = "receivercode37@yahoo.com"
password = "fyqewsxbxddffhue"
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
	connection.starttls()
	connection.login(user=email, password=password)
	connection.sendmail(from_addr=email, to_addrs=receiver, msg="Subject:Hello\n\nThis is the body of the email.")
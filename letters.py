import smtplib
#help(smtplib)
smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.starttls()
smtp_obj.login('slvjova.inna@gmail.com','25111989inna77')
smtp_obj.sendmail(from_addr="slvjova.inna@gmail.com",to_addrs="inna.slvjeva@gmail.com",msg="It's works")
smtp_obj.quit()

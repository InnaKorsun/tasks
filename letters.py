import smtplib
#help(smtplib)
smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.starttls()
import pdb; pdb.set_trace()
help(smtp_obj.login('slvjova.inna@gmail.com','25111989inna77'))
smtp_obj.login('slvjova.inna@gmail.com','25111989inna77')

lsmtp_obj.sendmail(from_addr="slvjova.inna@gmail.com",to_addrs="inna.slvjeva@gmail.com",msg="Its works")
smtp_obj.quit()

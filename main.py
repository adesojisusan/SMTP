import datetime as dt
import smtplib
import random


MY_EMAIL = "ntomolere@gmail.com"
EMAIL_PASSWORD = "Overcomer2020."
RECEIVER_EMAIL = "peterawotola@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("SMTP.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER_EMAIL, msg=f"Subject:MONDAY MOTIVATION\n\n{quote}")

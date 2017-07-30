import datetime
import calendar
import smtplib
from email.mime.text import MIMEText

now = datetime.datetime.now()

today_date = datetime.date.today()  # today's date

cy = now.year  # current year
cm = now.month  # current month

last_day = calendar.monthrange(cy, cm)[1]  # last day of currrent month

# the date and name of the last day of month
date_ld = datetime.date(cy, cm, last_day)
date_ld_name = calendar.day_name[date_ld.weekday()]

# the date of last Workday of month
if date_ld_name == "Saturday":
    date_ld = date_ld - datetime.timedelta(days=1)
elif date_ld_name == "Sunday":
    date_ld = date_ld - datetime.timedelta(days=2)

# if last day is Monday, the wk-2 is previous friday, else it is last workday minus 1
if date_ld_name == "Monday":
    date_ldm2 = date_ld - datetime.timedelta(days=3)
else:
    date_ldm2 = date_ld - datetime.timedelta(days=1)

# if today is workday-2 then send the reminder via e-mail
if today_date == date_ldm2:

    FROM = "youremail@yahoo.com"
    TO = ["1stadress@yahoo.com", "2ndaddress", "etc"]  # must be a list

    SUBJECT = "Hello!"
    TEXT = """Hi all,

 Please note that today is workday -2 for current month and tasks deadline is 1 pm !

 This is an automatic email reminder."""

    # Prepare actual message
    message = """From: %srnTo: %srnSubject: %srn

 %s
 """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail
    username = str("youremail@yahoo.com")
    password = str("your password")

    server = smtplib.SMTP("smtp.mail.yahoo.com", 587, timeout=10)
    server.set_debuglevel(1)

    try:
      server.starttls()
      server.login(username, password)
      server.sendmail(FROM, TO, message)
      print("The reminder e-mail for WK-2 was sent !")
    except:
      print("Couldn't send e-mail regarding WK-2")
    finally:
      server.quit()
    input("Press any key to exit..")

# if today is not workday -2 do nothing !
else:
    print("Today is not workday -2")
    input("Press any key to exit")
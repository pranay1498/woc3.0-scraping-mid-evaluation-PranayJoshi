import csv
import smtplib
from email.message import EmailMessage

FILEPATH = 'info.csv'


# to write the data in file
def writeFile(datalist):
    try:
        with open(FILEPATH, 'w') as fo:
            headers = ['organisation', 'link', 'technology']
            csv_writer = csv.DictWriter(fo, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(datalist)
            fo.close()
    except Exception as e:
        print("something went wrong while writing data to file")
        print(e)


# to send mail
def sendMail(mail_id, password):
    msg = EmailMessage()
    msg['Subject'] = 'Take a look at these organisations!'
    msg['From'] = mail_id
    msg['To'] = mail_id
    msg.set_content("Take a look at the list of organisations curated for you: \n File Attached")

    # read the file data to attach in mail
    with open(FILEPATH, 'rb') as f:
        file_data = f.read()

    # add attachment to mail
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='organisation data.csv')

    try:
        # connect to smtp server, login to gmail and send the mail from and to users own account
        smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpobj.ehlo()
        smtpobj.login(mail_id, password)
        smtpobj.send_message(msg)
        smtpobj.close()
    except Exception as e:
        print("something went wrong during sending mail, \ncheck if you have allowed third party app access in your account settings")
        print(e)

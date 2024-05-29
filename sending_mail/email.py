import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "angelinebishoyi@gmail.com"
receiver_email = "manikumaripudi2000@gmail.com"
password = "blhg adby ygsi rvrj"

message = MIMEMultipart() 
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Test Email'

body = "Hello, Python."
# filename = "kpiimage.png"
# with open(filename, "rb") as attachment:
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())

# encoders.encode_base64(part)

# part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {filename}",
# )
message.attach(MIMEText(body, 'plain'))
# message.attach(part)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")
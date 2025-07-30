
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
from email.utils import formatdate

# Load credentials from environment
load_dotenv()

EMAIL_ADDRESS = os.environ["EMAIL_USER"]
EMAIL_PASSWORD = os.environ["EMAIL_PASS"]

# Path to your Excel report
REPORT_PATH = "/home/ubuntu/Music-cost/aws_cost_report.xlsx"  # <-- Add Your Report File Path

# Email configuration
msg = EmailMessage()
msg["From"] = EMAIL_ADDRESS
msg["To"] = "***"  # <-- Add Main Recipients Here
msg["Cc"] = "***", "phyokhant@abccsmm.com" # <-- Add CC Recipients Here
msg["Subject"] = "AWS Cost Monthly Report"
msg["Date"] = formatdate(localtime=True)
msg.set_content("This mail provide the AWS Cost Report for 6 Months duration. Please let us know if you have any concern about this report.")

# Attach the Excel file
with open(REPORT_PATH, "rb") as f:
    file_data = f.read()
    file_name = os.path.basename(REPORT_PATH)

msg.add_attachment(file_data, maintype="application",
                   subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                   filename=file_name)

# Send the email and delete the file after success
try:
    with smtplib.SMTP("smtp.office365.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("✅ Email sent with attachment!")

    # Delete the file after successful send
    os.remove(REPORT_PATH)
    print(f"🧹 Deleted report: {REPORT_PATH}")

except Exception as e:
    print("❌ Failed to send email or delete the report:")
    print(e)
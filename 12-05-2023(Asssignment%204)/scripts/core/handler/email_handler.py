import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.schemas.inventory_schemas import Email
from scripts.logging.logs import logger
from scripts.constants.email_constants import email_object
from scripts.core.handler.inventory_handler import Item_handler


class Email_handler:
    """this class helps in building an smtp mail structure for sending to the recepient"""

    def send_email(self, Email: Email):
        sender_email = email_object.email_name
        sender_password = email_object.email_password
        receiver_email = Email.rec_email

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Total Price Of The Inventory List"

        price_object = Item_handler()

        result = price_object.find_total()
        body = str(result)
        message.attach(MIMEText(("Total amount : " + body), "plain"))

        try:

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            server.quit()
            logging.info({"message": "Email sent successfully"})
            return {"message": "Email sent successfully"}

        except Exception as e:
            logging.error({"message": str(e)})
            return {"message": str(e)}

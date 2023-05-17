import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.schemas.inventory_schemas import Email
import json
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

        inventory_object = Item_handler()
        result = inventory_object.find_total()
        get_list = inventory_object.fetch()
        result2= json.dumps(get_list, default=str, indent=2)
        result3 = str(result2)
        body = str(result)
        message.attach(MIMEText(("THESE ARE THE ITEMS IN YOUR INVENTORY :\n" +result3 + "\n Total amount : " + body), "plain"))

        try:

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            server.quit()
            logger.info({"message": "Email sent successfully"})
            return {"message": "Email sent successfully"}

        except Exception as e:
            logger.error({"message": str(e)})
            return {"message": str(e)}

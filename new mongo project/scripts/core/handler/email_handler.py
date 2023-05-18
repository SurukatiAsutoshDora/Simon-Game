import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.schemas.inventory_schemas import Email
import json
from tabulate import tabulate
import pandas as pd
from prettytable import PrettyTable
from scripts.logging.logs import logger
from scripts.constants.email_constants import email_object
from scripts.db.mongo import Item_handler


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
        df = pd.DataFrame(get_list)
        

        col_alignments = ['center', 'center', 'center']

        # Format DataFrame as a table using tabulate with colalign parameter
        table = tabulate(df, headers='keys', tablefmt='psql', colalign=col_alignments)
        body = str(result)
        message.attach(MIMEText(("THESE ARE THE ITEMS IN YOUR INVENTORY :\n" +table + "\n Total amount : " + body), "plain"))

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

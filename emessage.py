from datetime import datetime, timedelta
import numpy as np

import pandas as pd
from dateutil.utils import today

from openpyxl import load_workbook
import openpyxl
import smtplib

import win32com.client

def send_email():

    df = pd.read_excel('List.xlsx', "List")
    # Iterating over rows
    ol = win32com.client.Dispatch("outlook.application")
    olmail_item = 0x0  # size of the new email

    for index, row in df.iterrows():
        #print(row['Name'],row['EmailID'],row['Message1'])
        #print(df)
        table_style_html = ""
        email_message = "<p style='"'color:#003366; font-family: Calibri; font-size:14.5px; text-align:left;'"'>Hi Name,<br><br>Msg<br></p>"
        footer = "<p style='"'color:#003366;font-family: Calibri; font-size:14.5px;text-align:left;'"'>Best Regards,<br>Linga<br></p>"

        new_email = ol.CreateItem(olmail_item)
        new_email.Subject = "Happy New Year 2025 !!"
        new_email.To = row['EmailID']

        email_message = email_message.replace("Name", row['Name'])
        email_message = email_message.replace("Msg", row['Message1'])

        final_html = table_style_html + email_message + footer
        new_email.HTMLBody = final_html
        #print(final_html)
        # attach='C:\\Users\\admin\\Desktop\\Python\\Sample.xlsx'
        # new_email.Attachments.Add(attach)

        # To display the mail before sending it
        # new_email.Display()

        new_email.Send()


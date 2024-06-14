import win32com.client as win32
import psutil
import os
import subprocess
import sys
import constant

# Open Outlook.exe. Path may vary according to system config
# Please check the path to .exe file and update below
     
def open_outlook():
    try:
        subprocess.call(['C:\Program Files\Microsoft Office\Office16\Outlook.exe'])
        os.system("C:\Program Files\Microsoft Office\Office16\Outlook.exe");
    except:
        print("Outlook didn't open successfully")
 
# Checking if outlook is already opened. If not, open Outlook.exe and send email
def isOutlookOpen():
    flag = 0
    for item in psutil.pids():
        p = psutil.Process(item)
        if p.name() == "OUTLOOK.EXE":
            flag = 1
            break
        else:
            flag = 0
    return(bool(flag))
    
# Drafting and sending email notification to senders. You can add other senders' email in the list
def send_notification():
    if isOutlookOpen():
        outlook = win32.Dispatch('outlook.application')
        newMail = outlook.CreateItem(constant.olMailItem)
        newMail.Subject = "Test email from Python"
        #newMail.Subject = "check"
        newMail.BodyFormat = constant.olFormatPlain    #or olFormatRichText or olFormatPlain
        #newMail.HTMLBody = "test"
        #newMail.HTMLBody = "Test email from Python"
        newMail.To = "lingasamy_k@infosys.com"
        attachment1 = "d:/test.txt"
        with open(attachment1 , 'r') as myfile:
            data=myfile.read()
        #attachment2 = sys.argv[4]
        newMail.Body = "Test email from Python" + data
        newMail.Attachments.Add(Source=attachment1)
        #newMail.Attachments.Add(attachment2)
        
        newMail.display()
        # or just use this instead of .display() if you want to send immediately
        newMail.Send()

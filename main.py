from items.bulkChicken import bulkChicken
from utils.notifierService import sendEmail
from utils.emailList import emailList

chicken = bulkChicken()

if(chicken != ""):

# Set your Gmail account credentials
  sender_email = 'ENTER YOUR SMTP EMAIL'  
  receiver_emails = emailList  
  password = 'ENTER YOUR SMTP PASSWORD'  

  # Example usage
  subject = 'Save On Foods has Sale Items'
  message = chicken

  sendEmail(subject, message, sender_email, receiver_emails, password)
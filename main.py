from items.bulkChicken import bulkChicken
from utils.notifierService import sendEmail
from utils.emailList import emailList

# Add your scraper function within the items dictionary
items = {
  'Save On Chicken': bulkChicken(),
  #'Save On Ground Pork': groundPork()
}

messages = []

for itemName, itemDetails in items.items():
  if itemDetails:
    messages.append(f"{itemName}: {itemDetails}")

if(messages):

# Set your Gmail account credentials
  sender_email = 'ENTER YOUR SMTP EMAIL'  
  receiver_emails = emailList  
  password = 'ENTER YOUR SMTP PASSWORD'  

  # Example usage
  subject = 'Save On Foods has Sale Items'
  message = '\n'.join(messages)

  sendEmail(subject, message, sender_email, receiver_emails, password)
#### Adding a New Watch Item

To add a new food item to watch, within the items folder, create a new function referencing the bulkChicken.py as a template.

Then within the main.py file, modify the script to include your newly created function by adding your function into the items dictionary.

#### Setting up your SMTP

Google currently has a free SMTP server you can use with a regular gmail account. You can use any SMTP server you have, but for the everyday folk, Google is the best and will get you on the road fairly quickly. 

Once you have an SMTP server set up, plug in the credentials into the main.py file. 

#### Running the Script

To run, you will first need the following modules:

1) bs4
2) plyer
3) requests

`pip install requests bs4 plyer requests`

After installing the modules, run the main.py file on any Windows task scheduler or Linux chron job daily and get notified when your commonly purchased items are on sale. 

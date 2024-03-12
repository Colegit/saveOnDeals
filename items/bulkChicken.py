import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

# Function to check the price and send a notification
def bulkChicken():

    thingWatched = "Save On Foods Chicken Breast"

    # Target price threshold
    target_price = 38.99

    # URL of the webpage to monitor
    url = 'https://www.saveonfoods.com/sm/pickup/rsid/5515/product/western-family-boneless-chicken-breasts-00062639291518'

    # Send a GET request to the webpage
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element that contains the price
    price_element = soup.find(class_='PdpMainPrice--4c0ljm kLdUIn')

    if price_element:
        # Get the price value
        price_text = price_element.text.strip().strip('$').replace(',', '')
        price = float(price_text)

        # Check if the price is below the target
        if price < target_price:
            # Prepare the notification message
            message = f'{thingWatched} dropped below ${target_price}. Current price: ${price}'

            # Send the desktop notification
            notification.notify(
                title='Price Drop Alert',
                message=message,
                timeout=50  # Display the notification for 10 seconds
            )
            print(message)
            return message
        return ""
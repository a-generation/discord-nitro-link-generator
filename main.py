import random
import string
import requests
import time

def generate_random_string(length=18):
    """Generate a random alphanumeric string of a given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def send_to_discord(webhook_url, message):
    """Send a message to a Discord webhook."""
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    return response.status_code

def check_gift_code(code):
    """Check the gift code via the specified URL."""
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response

def main():
    print("Welcome to the Discord Gift Code Checker")
    webhook_url = input("Please enter your Discord webhook URL: ").strip()
    
    # Send initial message to Discord webhook
    initial_message = "Discord Gift Code Checker started."
    send_to_discord(webhook_url, initial_message)
    
    while True:
        code = generate_random_string()
        response = check_gift_code(code)
        if response.status_code == 200:
            print(f"{code} - valid")
            send_to_discord(webhook_url, f"Valid code found: {code}")
        else:
            print(f"{code} - invalid")
        time.sleep(1)  # Adding a delay to avoid excessive requests

if __name__ == "__main__":
    main()

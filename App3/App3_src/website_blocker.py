import time
from datetime import datetime as dt

host_path = "C:/Windows/System32/drivers/etc/"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now.day(), 8) < dt.now() < dt(
            dt.now().year, dt.now().month, dt.now.day(), 16):
        print("Working hours...")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(website)
    else:
        print("Fun hours...")
    time.sleep(5)
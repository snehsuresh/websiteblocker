import time
from datetime import datetime as dt

host_path = "/etc/hosts"  #path of your host file goes here
redirect= "127.0.0.1"
website_list=["www.facebook.com", "facebook.com" , "www.yahoo.com", "yahoo.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16): #if current time is greater than 8am/hrs  and less than 4pm or 16hrs
        print("working hour")
        with open(host_path, 'r+') as file:
            content = file.read()
            print(content)

            for site_to_block in website_list:
                if site_to_block in content:
                    pass
                else:
                    file.write("\n" + redirect + "  " + site_to_block + "\n" )

    else:
        print("free time")
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0) #putting the pointer to the start of the file, against the conventional position of pointer at the end.

            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()


    time.sleep(5)

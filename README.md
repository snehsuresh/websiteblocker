# Website blocker

Its a Python code that can help you overcome the temptation of distracting and addictive websites.

## Working

Just type in the word python or python3 if you have both versions, followed by the path to your script, just like this:


```bash
python3 blocker.py
```
To schedule this python program on linux, you need to use the *cron* service. You will add the script to your crontab

```bash
sudo crontab -e
```
Then add the location of your script after *@reeboot python3* at the end of your crontab
```bash
@reboot python3 /home/..../.../blocker.py

```

## Usage
Add the websites you need to block to the website_list
```python
import time

from datetime import datetime as dt

host_path = "/etc/hosts"
redirect= "127.0.0.1"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
# websiteblocker

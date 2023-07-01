![logo](https://github.com/N0rz3/Isearch/assets/123885505/460a9ddf-9222-4e50-a627-3d0cfa0a7b58)

[![python version](https://img.shields.io/badge/Python-3.10%2B-brightgreen)](https://www.python.org/downloads/)
[![license](https://img.shields.io/badge/License-GNU-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.fr.html)


# **Isearch is an osint tool which is based on instagram 📷**


# **😇 Abouts Isearch**

Isearch or rather Instagram search is a tool that retrieves information on an instagram profile (only public)

**Features of script**
 - fully async
 - asynchrone scraping 
 - menu in cli format (commands)

**Features**
 - id
 - username
 - fullname
 - biography
 - profile picture
 - number of followers
 - number of following
 - externals links
 - public / private account
 - buisness account
 - verified account
 - public phone number (+lookup)
 - public email
 - potentiels emails
 - download of profile picture


## **🛠️ Requirements / Launch**

- [Python 3](https://www.python.org/downloads/)

```
git clone https://github.com/N0rz3/Isearch.git
cd Isearch
pip install -r requirements.txt
```




### **😲 Usage**
```python isearch.py```
```
 ____                                    __     
/_   | ______ ____ _____ _______   ____ |  |__  
 |   |/  ___// __ \\__  \\_  __ \_/ ___\|  |  \ 
 |   |\___ \\  ___/ / __ \|  | \/\  \___|   Y  \ 
 |___/____  >\___  >____  /__|    \___  >___|  /    (BY 🦊 @N0rz3) 
          \/     \/     \/            \/     \/ 
       
🐦 Twitter: @norze15
☕ Donations: https://www.buymeacoffee.com/norze

usage: isearch.py [-h] [-d] <username>

option:
    -h, --help          show this help message and exit
    -d, --download      download the profile picture of the target
```

**For the proper functioning of the script it will be necessary to deposit your session id in the data.json**

![id](https://github.com/N0rz3/N0rz3/assets/123885505/68df7a56-82b7-4454-85dd-ffc504b33fca)

```json
{
    "sessionID": "YOUR_SESSION_ID"
}
```

**📚 Example input:**

```python isearch.py instagram```

**📚 Example output:**

![output](https://github.com/N0rz3/N0rz3/assets/123885505/39b80b17-baf3-4a44-90de-4a9a168843ea)



## **🌞 More**


### **✔️ / ❌ Rules**

**this tool was designed for educational purposes only and is not intended for any mischievous use, I am not responsible for its use.**


### **📜 License**

**This project is [License GPL v3](https://www.gnu.org/licenses/gpl-3.0.fr.html) be sure to follow all rules 👍**


### **💖 Thanks**
If you like what i do, please subscribe 💖. And if you find this tool is useful don't forget to star 🌟

**💶 Support me 👇**

<a href="https://www.buymeacoffee.com/norze" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50" ></a>

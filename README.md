<picture><img align="left" src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/duo.svg" width="20%"/></picture>
<h1>DuoXPy - Project Sandy</h1>
<h3>⚡️ XP farm and Streak keeper for Duolingo</h3>
<h4>Powered by Python 🐍</h5>

#

<p align="center">
  <a href="#feature">Feature</a>
  •
  <a href="#usage">Usage</a>     
  •
  <a href="#config">Config</a>     
  •
  <a href="#preview">Preview</a>
  •
  <a href="#disclaimer">Disclaimer</a>
</p>
<p align="center">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/gorouflex/DuoXPy?style=flat">
</p>

#

### ⚠️ This repository is still in its early stages and may not work as expected for some accounts, please try completing at least 9 lessons and run it again after 2-3 days ⚠️, <a href="#how-to-fix-error-500---no-skillid-found-in-xpgains">fix here</a>     

### Belongs to the Sandy Project

- [Sandy](https://github.com/gorouflex/Sandy/) ( Official Documents and Information Repository for Project Sandy )
- [HoneygainPot](https://github.com/gorouflex/HoneygainPot/) ( 🐝 Automatically claim your Honeygain lucky pot every day 🍯 )
- [DuoXPy](https://github.com/gorouflex/DuoXPy/) ( ⚡️ XP farm and Streak keeper for Duolingo 🔥 )
  
> [!IMPORTANT]
> **Read all** documents in this repo before doing anything!
> 
> Don't forget to star ⭐ this repository
> - Always update your repo following the original repo to get the latest update + bug fixes; I will not support anything if your repo is outdated
> - **Do not** enter your information ( token ) into 2 workflows file ( `daily.yml` and `manual.yml` ) because it will not work and may leak your information to everyone
> - (*): Do not fork this repo if one of these or all of these ( not CodeQL and CL ) GitHub Actions status badge show failing, and wait until one of these or two of these show passing then you can fork again
> - `Daily lessons` workflows always run every 14:00 UTC + 0; if you want to change it, refer to [this](https://github.com/gorouflex/DuoXPy/blob/main/README.md#how-to-change-the-schedule-that-the-workflows-will-run)
> <img src="https://i.imgur.com/htGeFlY.jpg">
  
# Feature 

- XP farm ⚡️
- Streak keeper 🔥

# Usage 

  0. Download from Releases    
  1. Go to [Duolingo](https://www.duolingo.com) and log in to your Duolingo account
  2. Open the browser's console by pressing `F12` button ( or `Fn+F12` on some laptops )
  3. Click on the tab `Console` then paste this to the console

```
document.cookie
  .split(';')
  .find(cookie => cookie.includes('jwt_token'))
  .split('=')[1]
```
  4. Copy the token without `'` ( example: 'abcde1234` -> abcde1234 )
  5. Open CMD, run `pip install requests` or `pip3 install requests`
  6. Click and run `DuoXPy.py` or using `python` or `python3` command
  7. Follow instructions	

> [!IMPORTANT]
> Usually, if you enter a lot of lessons ( like >1000 ) or if Duolingo cannot handle the request, you will receive an error code or log, and the lesson will be skipped. So, think wisely before entering the lesson!
> 
> If you got `No skillId found in xpGains` log then try to do least 1 lesson so it can run back to normal!

## How to fix `Error 500 - No SkillID found in xpGains`?

- Do not let your latest study session empty, at least get them to level 1 like these images below by completing 1 lesson or some lessons ( applied for every single course like English, Spanish, Japanese, etc... )

<p align="center">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/wrong.png">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/correct.png">
</p>

# Config

- Usually, you can find your config folder in the same place as the `main.py` file. In some specific cases, you might need to locate your config through the information window in the `main.py` file
- You can change your information and lessons in the config file

# Preview

<p align="left">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/preview.png">
</p>

# Disclaimer

> [!WARNING]
> This project is licensed under the [MIT License](https://mit-license.org/).
>
> For more information, see the [LICENSE file](./LICENSE).
> - This script is **not** affiliated with Duolingo
> - Use it at your **own risk** and responsibility  
> - I'm **not responsible** for any consequences that may arise from using this script
> - This script won't help with your daily or friend quests, it can only earn XP to move up the league rank
> - This script won't do real lessons or stories, only practices, so it won't affect your learning path
> - You may be **banned** from Duolingo if you overuse it, so use it wisely.
> - This repo is only for education purposes! 
### Special thanks to 💖
- [rfoal](https://github.com/rfoel/) x [duolingo](https://github.com/rfoel/duolingo) for the source code and idea
- [ESSTX](https://github.com/ESSTX) for xpGains fixes [PR #1](https://github.com/gorouflex/DuoXPy/pull/1), [PR #2](https://github.com/gorouflex/DuoXPy/pull/2)

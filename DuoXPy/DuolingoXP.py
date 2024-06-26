import os
import json
import base64
import configparser
import time
from datetime import datetime
import urllib.request
import urllib.parse
import urllib.error
from colorama import Fore, Style, init
import ctypes
import logging
import requests
init(autoreset=True)

y = Fore.LIGHTYELLOW_EX
b = Fore.MAGENTA
w = Fore.LIGHTWHITE_EX
r = Fore.RED
g = Fore.GREEN

current_dir = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = os.path.join(current_dir, 'config.ini')
VERSION = '3.0.0'
GITHUB_REPO_GO = 'gorouflex/DuoXPy'
GITHUB_REPO_OH = 'ohfeel/DuoXPy'
GITHUB_OHFEEL = 'ohfeel'
config = configparser.ConfigParser()
logging.basicConfig(filename='DuoXPy/duoxpy.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.ERROR)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    ctypes.windll.kernel32.SetConsoleTitleW(f"DuolingoXP bot  - Made by @ohfeel - Version {VERSION} - fork of DuoXPy by @gorouflex")
    print(f"""\n\n{Fore.RESET}    ██████╗ ██╗   ██╗ ██████╗ ██╗     ██╗███╗   ██╗ ██████╗  ██████╗     ██╗  ██╗██████╗     ██████╗  ██████╗ ████████╗
    ██╔══██╗██║   ██║██╔═══██╗██║     ██║████╗  ██║██╔════╝ ██╔═══██╗    ╚██╗██╔╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
    ██║  ██║██║   ██║██║   ██║██║     ██║██╔██╗ ██║██║  ███╗██║   ██║     ╚███╔╝ ██████╔╝    ██████╔╝██║   ██║   ██║   
    ██║  ██║██║   ██║██║   ██║██║     ██║██║╚██╗██║██║   ██║██║   ██║     ██╔██╗ ██╔═══╝     ██╔══██╗██║   ██║   ██║   
    ██████╔╝╚██████╔╝╚██████╔╝███████╗██║██║ ╚████║╚██████╔╝╚██████╔╝    ██╔╝ ██╗██║         ██████╔╝╚██████╔╝   ██║   
    ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝         ╚═════╝  ╚═════╝    ╚═╝   \n""".replace('█', f'{b}█{y}'))
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n{w} https://github.com/{GITHUB_OHFEEL} | https://github.com/{GITHUB_REPO_OH} | fork of https://github.com/{GITHUB_REPO_GO} \n{y}------------------------------------------------------------------------------------------------------------------------\n""".replace('|', f'{b}|{w}'))

def create_config():
    clear()
    duolingo_jwt = input("Enter your Duolingo JWT: ")
    lessons = input("Enter the number of lessons: ")
    timer = input("Enter the timer interval in seconds: ")
    config['Settings'] = {
        'DUOLINGO_JWT': duolingo_jwt,
        'LESSONS': lessons,
        'TIMER': timer
    }
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
    print(f"{g}Configuration file created successfully!{Fore.RESET}")

def check_config_integrity():
    if not os.path.isfile(CONFIG_FILE) or os.stat(CONFIG_FILE).st_size == 0:
        create_config()
        return
    config.read(CONFIG_FILE)
    if not config.has_section('Settings') or not all(config.has_option('Settings', opt) for opt in ['DUOLINGO_JWT', 'LESSONS', 'TIMER']):
        create_config()

def read_config():
    config.read(CONFIG_FILE)
    return config['Settings']

def update_settings():    
    while True:
        print()
        print(f"{y}[{b}+{y}]{w}  Settings{Fore.RESET}\n")
        print(f"{y}[{w}#{y}]{w}  1. Duolingo Token:{Fore.RESET}")
        print(f"{y}[{w}#{y}]{w}  2. Number of Lessons:{Fore.RESET}")
        print(f"{y}[{w}#{y}]{w}  3. Timer Interval:{Fore.RESET}")
        print(f"{y}[{w}#{y}]{w}  b. Back{Fore.RESET}\n")
        choice = input(f"{y}[{b}?{y}]{w} Option: ").lower().strip()
        print()
        if choice == '1':
            config['Settings']['DUOLINGO_JWT'] = input(f"Enter your Duolingo JWT [{config['Settings']['DUOLINGO_JWT']}]: ") or config['Settings']['DUOLINGO_JWT']
        elif choice == '2':
            config['Settings']['LESSONS'] = input(f"Enter the number of lessons [{config['Settings']['LESSONS']}]: ") or config['Settings']['LESSONS']
        elif choice == '3':
            config['Settings']['TIMER'] = input(f"Enter the timer interval in seconds [{config['Settings']['TIMER']}]: ") or config['Settings']['TIMER']
        elif choice == 'b':
            break
        else:
            print(f"{r}Invalid option. Please try again.{Fore.RESET}")
            input("Press Enter to continue.")
        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)
        print(f"{g}Settings updated successfully!{Fore.RESET}")

def decode_jwt(jwt):
    _, payload, _ = jwt.split('.')
    decoded = base64.urlsafe_b64decode(payload + "==")
    return json.loads(decoded)


def http_request(method, url, headers=None, data=None):
    try:
        req = urllib.request.Request(url, headers=headers or {}, data=data, method=method)
        with urllib.request.urlopen(req) as response:
            return response.getcode(), response.read().decode('utf-8')
    except Exception as e:
        # Log the error
        logging.error(f"HTTP request failed: {e}")
        raise
def get_latest_ver():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    status, data = http_request("GET", f"https://api.github.com/repos/{GITHUB_REPO_OH}/releases/latest", headers)
    if status == 200:
        release_info = json.loads(data)
        return release_info['tag_name']
    else:
        raise Exception("Failed to fetch the latest version from GitHub")

def check_updates():
    LOCAL_VERSION = VERSION
    max_retries = 3
    skip_update_check = False
    for i in range(max_retries):
        try:
            latest_version = get_latest_ver()
            break
        except:
            if i < max_retries - 1:
                print(f"{r}Failed to fetch latest version. Retrying {i+1}/{max_retries}...{Fore.RESET}")
                time.sleep(5)
            else:
                clear()
                print(f"{r}Failed to fetch latest version{Fore.RESET}")
                result = input("Do you want to skip the check for updates? (y/n): ").lower().strip()
                if result == "y":
                    skip_update_check = True
                else:
                    print(f"{r}Quitting...{Fore.RESET}")
                    raise SystemExit
    if not skip_update_check:
        if LOCAL_VERSION < latest_version:
            clear()
            print(f"{y}New version available: {latest_version}. Updating the script...{Fore.RESET}")
            updater()
            raise SystemExit
        elif LOCAL_VERSION > latest_version:
            clear()
            print(f"{y}Welcome to the DuoXPy Beta Program{Fore.RESET}")
            print(f"{y}This beta build may not work as expected and is only for testing purposes!{Fore.RESET}")
            result = input("Do you want to continue (y/n): ").lower().strip()
            if result != "y":
                print(f"{r}Quitting...{Fore.RESET}")
                raise SystemExit

def updater():
    latest_url = f"https://raw.githubusercontent.com/{GITHUB_REPO_OH}/main/DuoXPy/DuoXPy.py"
    response = urllib.request.urlopen(latest_url)
    data = response.read().decode('utf-8')
    with open(__file__, 'w', encoding='utf-8') as f:
        f.write(data)
    print(f"{g}Script updated successfully.{Fore.RESET}")
    input("Press Enter to restart the script")
    raise SystemExit

def run():
    clear()
    config = read_config()
    duolingo_jwt = config['DUOLINGO_JWT']
    lessons = int(config['LESSONS'])
    timer = int(config['TIMER'])
    print(f"{y}[{b}+{y}]{w}Current configuration:{Fore.RESET}\nLessons: {lessons}\nTimer: {timer} seconds")
    print(f"{y}[{w}#{y}]{w}Running...{Fore.RESET}")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {duolingo_jwt}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    try:
        date = datetime.now().strftime('%Y-%m-%d')
        sub = decode_jwt(duolingo_jwt)['sub']
        print(f"{y}[{b}#{y}]{w}Date: {date} {Fore.RESET}")
        response = requests.get(
            f"https://www.duolingo.com/{date}/users/{sub}?fields=fromLanguage,learningLanguage,xpGains",
            headers=headers,
        )
        data = response.json()
        # Take element required to make a request
        fromLanguage = data['fromLanguage']
        learningLanguage = data['learningLanguage']
        try:
            xpGains = data['xpGains']
            skillId = xpGains[0]['skillId']
        except:
            print(f"{colors.FAIL}Your Duolingo account has been banned/does not exist or you didn't do any lesson, please do at least 1 lesson{colors.ENDC}")
            logging.error("Your Duolingo account has been banned/does not exist or you didn't do any lesson, please do at least 1 lesson")
            exit(-1)

        skillId = next(
            (xpGain['skillId'] for xpGain in reversed(xpGains) if 'skillId' in xpGain),
            None,
        )
        
        if skillId is None:
            print(f"{colors.FAIL}{colors.WARNING}--------- Traceback log ---------{colors.ENDC}\nNo skillId found in xpGains\nPlease do at least 1 or some lessons in your skill tree\nVisit https://github.com/gorouflex/DuoXPy#how-to-fix-error-500---no-skillid-found-in-xpgains for more information{colors.ENDC}")
            logging.error("No skillId found in xpGains")
            exit(-1)
        print(f"{y}[{w}#{y}]{w}Skill ID: {skillId} {Fore.RESET}")
        print(f"{y}[{w}#{y}]{w}From Language: {fromLanguage} {Fore.RESET}")
        print(f"{y}[{w}#{y}]{w}Learning Language: {learningLanguage} {Fore.RESET}")
        
       
        xp = 0
        for _ in range(lessons):
            try:
                session_data = {
                    'challengeTypes': [
                        'assist', 'characterIntro', 'characterMatch', 'characterPuzzle', 'characterSelect',
                        'characterTrace', 'completeReverseTranslation', 'definition', 'dialogue', 'form',
                        'freeResponse', 'gapFill', 'judge', 'listen', 'listenComplete', 'listenMatch', 'match',
                        'name', 'listenComprehension', 'listenIsolation', 'listenTap', 'partialListen',
                        'partialReverseTranslate', 'readComprehension', 'select', 'selectPronunciation',
                        'selectTranscription', 'syllableTap', 'syllableListenTap', 'speak', 'tapCloze',
                        'tapClozeTable', 'tapComplete', 'tapCompleteTable', 'tapDescribe', 'translate', 'typeCloze',
                        'typeClozeTable', 'typeCompleteTable'
                    ],
                    'fromLanguage': fromLanguage,
                    'isFinalLevel': False,
                    'isV2': True,
                    'juicy': True,
                    'learningLanguage': learningLanguage,
                    'skillId': skillId,
                    'smartTipsVersion': 2,
                    'type': 'SPEAKING_PRACTICE',
                }

                session_response = requests.post(f'https://www.duolingo.com/{date}/sessions', json=session_data, headers=headers)
                if session_response.status_code == 500:
                    print(f"{r}Session Error 500 / No skillId found in xpGains or Missing some element to make a request\nPlease do at least 1 or some lessons in your skill tree\n{Fore.RESET}")
                    logging.error(f"Session Error 500 / No skillId found in xpGains or Missing some element to make a request\nPlease do at least 1 or some lessons in your skill tree\n")
                    continue
                elif session_response.status_code != 200:
                    print(f"{r}Session Error: {session_response.status_code}, {session_response.text}{Fore.RESET}")
                    logging.error(f"Session Error: {session_response.status_code}, {session_response.text}")
                    continue
                session = session_response.json()

                end_response = requests.put(
                    f"https://www.duolingo.com/{date}/sessions/{session['id']}",
                    headers=headers,
                    json={
                        **session,
                        'heartsLeft': 0,
                        'startTime': (time.time() - 60),
                        'enableBonusPoints': False,
                        'endTime': time.time(),
                        'failed': False,
                        'maxInLessonStreak': 9,
                        'shouldLearnThings': True,
                    },
                )

                try:
                    end_data = end_response.json()
                except json.decoder.JSONDecodeError as e:
                    print(f"{r}Error decoding JSON: {e}{Fore.RESET}")
                    print(f"Response content: {end_response.text}")
                    continue

                response = requests.put(f'https://www.duolingo.com/{date}/sessions/{session["id"]}', data=json.dumps(end_data), headers=headers)
                if response.status_code == 500:
                    print(f"{r}Response Error 500 / No skillId found in xpGains or Missing some element to make a request\nPlease do at least 1 or some lessons in your skill tree\nVisit https://github.com/gorouflex/DuoXPy#how-to-fix-error-500---no-skillid-found-in-xpgains for more information{Fore.RESET}")
                    continue
                elif response.status_code != 200:
                    print(f"{r}Response Error: {response.status_code}, {response.text}{Fore.RESET}")
                    continue
                print(f"{y}[{g}!{y}]{w}[{_ + 1}] - {end_data['xpGain']} XP{Fore.RESET}")

                if _ < lessons - 1:
                    print(f"Waiting for {timer} seconds before next lesson...")
                    time.sleep(timer)
            except Exception as e:
                print(f"{r}Error during session: {e}{Fore.RESET}")
                time.sleep(5)
    except Exception as e:
        print(f"{r}Error: {e}{Fore.RESET}")
        logging.error(f"Error: {e}")


def main_menu():
    check_config_integrity()
    check_updates()
    while True:
        clear()
        print(f"""{y}[{b}+{y}]{w}  DuolingoXP bot  - Made by @ohfeel - Version {VERSION} - fork of DuoXPy by @gorouflex
{y}[{w}#{y}]{w} Version:         {VERSION}  
{y}[{b}+{y}]{w} Configurations:
{y}[{w}#{y}]{w} Lessons:         {config['Settings']['LESSONS']}
{y}[{w}#{y}]{w} Token:    {config['Settings']['DUOLINGO_JWT']}
{y}[{w}#{y}]{w} Timer:    {config['Settings']['TIMER']} seconds 
{y}[{b}+{y}]{w} Settings View:
{y}[{w}#{y}]{w} 1. Run Bot 
{y}[{w}#{y}]{w} 2. Update Settings
{y}[{w}#{y}]{w} 3. Quit\n""")
        choice = input(f"{y}[{b}?{y}]{w} Option: ").lower().strip()
        if choice == '1':
            run()
        elif choice == '2':
            update_settings()
        elif choice == '3':
            print(f"{r}Quitting...{Fore.RESET}")
            break
        else:
            print(f"{r}Invalid option. Please try again.{Fore.RESET}")
            input("Press Enter to continue.")

if __name__ == "__main__":
    main_menu()

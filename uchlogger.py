import psutil, sys, time
from pathlib import Path

check = 0
started = 0
a = input("UCH Logger v1.0\n\nType \"help\" without the quotes for help\n\n")

if sys.platform == "win32":
    process = "UltimateChickenHorse.exe"
    log = str(Path.home()) + "/AppData/LocalLow/Clever Endeavour Games/Ultimate Chicken Horse/output_log.txt"
elif sys.platform == "darwin":
    process = "UltimateChickenHorse"
    log = str(Path.home()) + "/Library/Logs/Unity/Player.log"
else:
    process = "UltimateChickenHorse.x86_64"
    log = str(Path.home()) + "/.config/unity3d/Clever Endeavour Games/Ultimate Chicken Horse/Player.log"

def CheckIfRunning():
    if process in (p.name() for p in psutil.process_iter()):
        print("[INFO]: Starting logging...")
        init()
    else:
        print("[ERROR]: Ultimate Chicken Horse is not running\n")
        _input()

def init():
    global f
    global started
    global a
    started = 1
    f = open(log)
    file_changed()

def file_changed():
    global check
    global a
    while True:
        line= f.readline()
        if not line:
            time.sleep(1)
            file_changed()
        else:
            print(line.replace("\n", "", 1))
            if line == "LobbyManagerManager shutting down...\n":
                check = 1
            if line == "[Net] Shutting down GameSparks\n" and check == 1:
                print("[INFO]: Logging finished!\n")
                f.close()
                _input()
                #sys.exit(1)
def _input():
    global a
    a = input("")
    inputcheck()
def inputcheck():
    global a
    global started
    if a == "help":
        print("Commands:\n  help            show this help message\n  about           general information about the program\n  start           start the logging\n  github          open github page in browser\n  exit/quit       exit the application\n")
        _input()
    elif a == "start":
        if started == 0:
            CheckIfRunning()
    elif a == "about":
        print("""       ____          __
|¯| |¯|  __|¯|_|¯|  |  |   ___ ___ ___ ___ ___
| |_| | |__|  _  |  |  |__| . | . | . | -_|  _|
|_____|____|_| |_|  |_____|___|_  |_  |___|_|
                              |___|___|
UCH Logger v1.0
Made by Grim Stride using Python 3.9.0\n""")
        _input()
    elif a == "exit" or a == "quit":
        if started == 1:
            f.close()
        sys.exit(1)
    else:
        print("Unknown command: " + a + "\n")
        _input()

inputcheck()

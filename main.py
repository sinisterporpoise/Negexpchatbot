import pytchat
import time
from datetime import datetime

from termcolor import colored, cprint
from colorama import init, Fore
import sys

init(autoreset=True)


# Capture all chats.
chat = pytchat.create(video_id=sys.argv[1])
filename = 'chatlog'+str(datetime.now())

#------------------------------------------------------
# Open a file with the date time.
#---------------------------------------------------
try:
    f = open(filename, 'w')
except IOError:
    print ('Could not open file.')


# With just one modication, record all chats to the file
           
while chat.is_alive():
    try:
        for c in chat.get().items:
            f.write(f"\n {c.datetime}{c.author.name}{c.message}")
            f.write("")
            if c.author.isChatModerator == True:
                print(
                    f"{Fore.GREEN}{c.datetime} {Fore.RED}[{c.type}] [{c.amountString}] {Fore.RED}[Moderator]{Fore.YELLOW}[{c.author.name}] {Fore.WHITE}{c.message}"
                )
            else:
                print(
                    f"{Fore.GREEN}{c.datetime} {Fore.RED}[{c.type}] [{c.amountString}] {Fore.YELLOW}[{c.author.name}] {Fore.WHITE}{c.message}"
                )
                #time.sleep(1)
    except KeyboardInterrupt:
        stream.terminate()
        break

f.close()

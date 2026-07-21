import psutil
import rich
import sys

from rich import print

def browser_chk():
    needed_apps = ['chrome.exe', 'firefox.exe', 'ollama app.exe']
    browser_stat = list(map(lambda x: x in (i.name() for i in psutil.process_iter()),needed_apps))

    if browser_stat[0] == browser_stat[1]:
        if browser_stat[0] == False:
            print('\nNo Browser is Running. Either Run Chrome or Firefox for the Script to Work')
            sys.exit()
    elif browser_stat[0] != browser_stat[1]:
        if browser_stat[0] == True:
            print('\n[bold yellow]Chrome[/bold yellow] Browser is Running')
        else:
            print('\n[bold orange1]Firefox[/bold orange1] Browser is Running')
    if browser_stat[0] == browser_stat[1]:
        if browser_stat[0] == True:
            print("\nBoth [bold yellow]Chrome[/bold yellow] and [bold orange1]Firefox[/bold orange1] are Running")
    if browser_stat[2] == False:
        print('Ollama is not open. Open the process to start the program')
        sys.exit()
    else:
        print('[blue cyan]Ollama[/blue cyan] is Running')


if __name__ == '__main__':
    browser_chk()
import math
import time
import speedtest
import colorama as colour

def BytesToMega(sizeBytes):
    sizeMegaBytes = round(sizeBytes / 1048576, 2)
    return f"{sizeMegaBytes} Mpbs"

def main():
    # Writing: https://patorjk.com/software/taag
    print(colour.Fore.RED)
    print(colour.Fore.RED + "\t   _____                     __" + colour.Fore.WHITE + "______          __ " + colour.Fore.RED)
    print("\t  / ___/____  ___  ___  ____/ " + colour.Fore.WHITE + "/_  __/__  _____/ /_" + colour.Fore.RED)
    print("\t  \\__ \\/ __ \\/ _ \\/ _ \\/ __  / " + colour.Fore.WHITE + "/ / / _ \\/ ___/ __/" + colour.Fore.RED)
    print("\t ___/ / /_/ /  __/  __/ /_/ / " + colour.Fore.WHITE + "/ / /  __(__  ) /_  " + colour.Fore.RED)
    print("\t/____/ .___/\\___/\\___/\\__,_/ " + colour.Fore.WHITE + "/_/  \\___/____/\\__/  " + colour.Fore.RED)
    print("\t    /_/\n")
    Wifi = speedtest.Speedtest()

    print(colour.Fore.LIGHTYELLOW_EX + "[!] Loading Server List...")
    Wifi.get_servers()
    print("[!] Choosing Best Server...")
    bestSrver = Wifi.get_best_server()
    print(colour.Fore.LIGHTBLACK_EX + f"SERVER: {bestSrver['host']}, {bestSrver['country']}" + colour.Fore.LIGHTYELLOW_EX)
    
    print("[!] Performing Download & Upload Tests...")
    Ping = Wifi.results.ping
    downloadSpeed = Wifi.download()
    uploadSpeed = Wifi.upload()

    print(colour.Fore.LIGHTBLACK_EX + f"PING: {Ping :.2f} ms")
    print(f"DOWNLOAD: {BytesToMega(downloadSpeed)}")
    print(f"UPLOAD: {BytesToMega(uploadSpeed)}" + colour.Fore.RESET)
    time.sleep(5)
    
if __name__ == '__main__':
    main()

from __future__ import print_function
import os

def ask_choice():
    choice = raw_input("Please choose a wifi (leave blank to exit): ")
    if choice == "":
        return -1
    return int(choice)

def is_secured(wifi):
    wifi = wifi.split(":")[1]
    return wifi != ""

def connect_wifi(wifi, secured):
    wifi = wifi.split(":")[0]
    wifi_prompt = wifi
    wifi = wifi.replace(' ', '\ ')
    if secured:
        password = raw_input("Please type password: ")
        command = 'nmcli device wifi connect ' + wifi + ' password ' + password
    else:
        command = 'nmcli device wifi connect ' + wifi
    print("Connecting to " + wifi_prompt + " ...")
    return_code = os.popen(command).read()
    if return_code.split(" ")[0] == "Error":
        print("Something went wrong, maybe password is wrong ?")

def nb_digits(n):
  return len(str(abs(n)))

def print_wifi_list(wifi_list):
    space = "               "
    print("#" + space[1:] + "SSID")
    for i in range (0, len(wifi_list)):
        rows, columns = os.popen('stty size', 'r').read().split()
        print('-' * int(columns))
        print(i, end = "")
        print(space[nb_digits(i):], end = "")
        print(wifi_list[i].split(":")[0])
    print()
def get_wifi_list():
    wifi_list = os.popen('nmcli -f SSID,SECURITY -t device wifi list').read()
    return wifi_list.splitlines()


def main():
    wifi_list = get_wifi_list()
    print_wifi_list(wifi_list)
    choice = ask_choice()
    if choice == -1:
        return
    secured = is_secured(wifi_list[choice])
    connect_wifi(wifi_list[choice], secured)

if __name__ == '__main__':
    main()

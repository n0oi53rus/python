from socket import *

network = input('Input IP address format is  XX.XX.XX. - :')## Write ip address


def is_up(addr):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(1)
    if not s.connect_ex((addr,135)):
        s.close()
        return 1
    else:s.close()
## Запуск
def run():
    print('')
    for ip in range(1,254):
        addr = network + str(ip)
        if is_up(addr):
            print('%s \t - %s' %(addr,getfqdn(addr)))

    print()

if __name__ == '__main__':
    print('''Scanning in process''')

    run()

    input('Done')
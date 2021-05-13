import os

os.system('cls')

print ("\033[1;32;40m  _  __          _               _             ")
print ("\033[1;32;40m | |/ /   ___   | |__     __ _  (_)  _ __      ")
print ("\033[1;32;40m | ' /   / _ \  | '_ \   / _` | | | | '_ \     ")
print ("\033[1;32;40m | . \  | (_) | | |_) | | (_| | | | | | | |  _ ")
print ("\033[1;32;40m |_|\_\  \___/  |_.__/   \__,_| |_| |_| |_| (_)")
print ("\033[1;32;40m                                               ")
ip = input('\033[1;32;40m Type IP Address: ')

print('-' * 60)
os.system('ping {} -t'.format(ip))

print('-' * 60)

input('Press Any Enter To Exit')
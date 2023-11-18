import socket

print(''''


█████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗
██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗
███████║██╔████╔██║██╔████╔██║███████║██████╔╝
██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗
██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝


''')
name = input("what is your name?: ")


try:
    repeat_count = int(input("hello " + name + "! how many times do you want to print your name?: "))
except ValueError:
    print("please enter right number.:")

for _ in range(repeat_count):
    print(name)
print("good bye!")
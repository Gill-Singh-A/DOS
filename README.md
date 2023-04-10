# DOS (Denial of Service)
Sends randomly generated packets to the IP Address of the target with the designated port range through UDP Protocol through multiple threads, hence slowing down the server and causing a DOS Attack.

## Requirements
Language Used = Python3<br />
Modules/Packages used:
* socket (for connecting and sending the packets through UDP Protocol)
* threading (for creating multiple threads, to increase the rate of sending the packets)
* random (for generating random string)
* time (for displaying time in the Command Line Interface)
* string (for generating random string)
* tkinter (for providing a gui interface)
* colorama (for colouring the text in Command Line Interface)
* datetime (for displaying date in the Command Line Interface)

### INPUTS
* Target IP
* Starting Port
* Ending Port
* Threads
* Message Size
* Message Multiplier

### Working
It creates the specified number of threads for each port given. For example, if there are 2 ports (Starting port = 80 and Ending Port = 81) and threads = 100, then it will create a total 200 threads (100 for each port).<br />
It then generates a random string of the size that is specified in Message Size and multiplies that string with the value specified in  message multiplier.<br />
Then each thread connects to the server with the port they're assigned through UDP Protocol.<br />
And finally sends the random string to the server through the socket created.<br /><br />

Note: As this Program is written in Python which is run through an Interpreter, it would be slow and hence won't be that much effective. To make this more efficient, we can use some tools like auto-py-to-exe to convert the '.py' file to '.exe' file.
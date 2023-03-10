from netmiko import ConnectHandler
import json


#User will input device names which will be split using commas.
devices = input("Enter device names separated by commas: ").split(",")
username = input("Enter username: ")
password = input("Enter password: ")
filename = input("Enter file name: ")

#Create empty list named device_lists
device_lists = list()


#This for loop will take each device listed in devices and add them to the device_list variable. It will then be appended to device_lists.
for device in devices: 
    #Removes any leading/trailing characters from the switch name.
    hostname = device.strip()
    device_list = {
        "device_type": "cisco_xe",
        "host": hostname,
        "username": username,
        "password": password,
        #Read timeout allows a command 30 seconds to complete before timing out.
        "read_timeout_override": 30
    }
    device_lists.append(device_list)

#Provides terminal view of the device lists created.     
json_formatted = json.dumps(device_lists, indent=4)
print(json_formatted)

#Variable containing show commands.
show_commands = ["show version", 
                
                 "dir flash:", "dir flash-1:", 
                 "dir flash-2:", 
                "dir flash-3:", "dir flash-4:", 
                "dir flash-5:",
                  "dir flash-6:", "dir flash-7:", 
                  "dir flash-8:", 
                  "dir flash-9:",

                "show boot system switch 1", "show boot system switch 2", "show boot system switch 3", "show boot system switch 4", "show boot system switch 5", 
                 "show boot system switch 6", "show boot system switch 7", "show boot system switch 8", "show boot system switch 9",
                 "show switch detail", "show license summary", "wr"]

#Open file to write command output from Cisco device.
file = open("C:<file path here>" + filename + ".txt", "a")

#Connects to one device at a time using the information provided in the device_lists variable.
for each_device in device_lists:
   connection = ConnectHandler(**each_device)
   print(f'---------- Connecting to {each_device["host"]}')
   
    #Performs the show commands on the device
   for command in show_commands:
        output = connection.send_command(command)
        
        #Writes the show command output to the txt file. Adds the hostname above each show command.
        file.write(each_device["host"] + "\n\n" + command + "\n\n" + output + "\n\n")
   print(f'---------- Disconnecting from {each_device["host"]}')
      
    

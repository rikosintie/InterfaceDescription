# InterfaceDescription
Create Interface Descriptions from CDP Neighbor Output

Most customers want interface descriptions on core switch ports that are connected to edge switches 
and edge switch ports that are connected to access points or other critical devices. When you are 
doing a green field design this is usually pretty easy and you can include the descriptions in your 
spreadsheet data and they are automatically inserted when you run the template.

But there are times when you are in the field and need to create a lot of descriptions. Doing this 
manually is tedious, time consuming and error prone. To work around this I wrote a simple Python 
script to create the interface descriptions. Here are the instructions to use it.

#Quick Start 
Download the script
Log onto the switch and run
'sh run cdp ne det | i Dev|Interface
This will display the device name and interface for each neighbor
Copy the output and save it in a text file called interface.txt in the same folder as the script
Run the script. This will output the code needed on the screen
Copy the code and paste it into the switch
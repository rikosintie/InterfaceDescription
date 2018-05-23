'''
read a file containing the output of sh cdp ne det | i Dev|Interface
Print out the code needed to create an interface description:
interface 'interface name'
des < device name >
exit

Change log
May 5, 2018
Added a try block for opening the file and code to select only lines
with device and interface information. You don't have to clean up the
data file any longer as it only selects lines that start with
Device ID:
Interface:
'''
#create a space between the command line and the output
print()
#create a blank list to accept each line in the file
data = []
# reads a file called interface.txt. If you want a different name change
# it here.
mydatafile = 'interface.txt'
try:
    f = open(mydatafile, 'r')
except FileNotFoundError as fnf_error:
            print(fnf_error)
            sys.exit(0)
else:
    for line in f:
        if line.find('Device ID:') != -1 or line.find('Interface:') != -1:
                data.append(line)
        f.close#There are two lines for each device so subtract 2 from list length.
items = len(data)-2
#initalize the loop counter
counter = 0
while counter <= items:
#read in the first hostname line
	hostname = data[counter]
#remove the Device ID: from the hostname line.
	hostname = hostname[11:]
#remove the newline from the hostname
	hostname = hostname.strip('\n')
#The interface is on the next line
	deviceinterface = data[counter + 1]
#Find the comma and colon in interface line
	comma = deviceinterface.find(',')
	colon = deviceinterface.find(':')
#strip the comma out
	deviceinterface = deviceinterface[0:comma].rstrip(',')
#delete the colon
	deviceinterface = deviceinterface.replace(':','')
#print the information needed to create the interface description
	print(deviceinterface)
	print('des < %s >' %(hostname))
	print('exit')
#increment the counter by two to jump to the next hostname line
	counter = counter + 2
	print()


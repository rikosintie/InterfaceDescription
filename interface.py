'''
read a file containing the output of sh cdp ne det | i Dev|Interface
Print out the code needed to create an interface description: 
interface 'interface name'
des < device name >
exit
'''
#create a space between the command line and the output
print()
#create a blank list to accept each line in the file
listname = []
f = open('interface.txt', 'r')
for line in f:
    listname.append(line)
f.close
#There are two lines for each device so subtract 2 from list length.
items = len(listname)-2
#initalize the loop counter
counter = 0
while counter <= items:
#read in the first hostname line
	hostname = listname[counter]
#remove the Device ID: from the hostname line.
	hostname = hostname[11:]
#remove the newline from the hostname
	hostname = hostname.strip('\n')
#The interface is on the next line
	deviceinterface = listname[counter + 1]
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
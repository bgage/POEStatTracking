import configparser
stats = configparser.ConfigParser()
stats.read('stats.txt')
classes = configparser.ConfigParser()
classes.read('classes.txt')
classSelected = 0
while classSelected == 0:
	cl = input("Select a number 1 Marauder 2 Ranger 3 Witch 4 Duelist 5 Templar 6 Shadow 7 Scion ")
	if cl == '1':
		cl = 'Marauder'
		classSelected = 1
	elif cl == '2':
		cl = 'Ranger'
		classSelected = 1
	elif cl == '3':
		cl = 'Witch'
		classSelected = 1
	elif cl == '4':
		cl = 'Duelist'
		classSelected = 1
	elif cl == '5':
		cl = 'Templar'
		classSelected = 1
	elif cl == '6':
		cl = 'Shadow'
		classSelected = 1
	elif cl == '7':
		cl = 'Scion'
		classSelected = 1
#	else:
#		print "Invalid input"

stats['Base']['class'] = cl
for atb in classes[cl]:
    print(atb, classes[cl][atb])
    stats['Attributes'][atb] = classes[cl][atb]

na = input("Enter a name: ")
stats['Base']['name'] = na


with open('stats.txt', 'w') as configfile:
    stats.write(configfile)

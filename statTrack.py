import configparser
stats = configparser.ConfigParser()
stats.read('stats.txt')
classes = configparser.ConfigParser()
classes.read('classes.txt')
classSelected = 0
classChoices = {1: 'Marauder',
		2: 'Ranger',
		3: 'Witch',
		4: 'Duelist',
		5: 'Templar',
		6: 'Shadow',
		7: 'Scion'
	       }

while classSelected == 0:
    try:
        classInput = input("Select a number 1 Marauder 2 Ranger 3 Witch 4 Duelist 5 Templar 6 Shadow 7 Scion ")
        if int(classInput) in range(1,8):
            cl = classChoices[int(classInput)]
            classSelected = 1
    except (KeyError, ValueError):
        print("Invaild Input")

stats['Base']['class'] = cl
for atb in classes[cl]:
    print(atb, classes[cl][atb])
    stats['Attributes'][atb] = classes[cl][atb]

na = input("Enter a name: ")
stats['Base']['name'] = na


with open('stats.txt', 'w') as configfile:
    stats.write(configfile)

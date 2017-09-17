import configparser
stats = configparser.ConfigParser()
stats.read('stats.txt')
classes = configparser.ConfigParser()
classes.read('classes.txt')
cl = input("Pick a class: ")
stats['Base']['class'] = cl
for atb in classes[cl]:
    print(atb, classes[cl][atb])
    stats['Attributes'][atb] = classes[cl][atb]

na = input("Enter a name: ")
stats['Base']['name'] = na


with open('stats.txt', 'w') as configfile:
    stats.write(configfile)

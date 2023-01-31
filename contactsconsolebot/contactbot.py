from  collections import  defaultdict

contacts = defaultdict(list) # used defeaultdict to make the task easy

def exepting(func): #catching errors
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return 'enter right command'
        except ValueError:
            return 'enter right command'
        except IndexError:
            return 'enter right command'
    return inner

@exepting
def hello():
    return 'Can I help You'

@exepting
def add(name, number): #add contacts to phone book
    return contacts[name].append(number)

@exepting #change phone numbers of contact
def change(name, numbers):
    if name in contacts.keys():
        contacts[name].clear()
        contacts[name].append(numbers)
    else:
        contacts[name].append(numbers)

@exepting #output phone numbers of contact
def phone(name):
    if name in contacts:
        return print (contacts[name])
    return "no such name"

@exepting #Show contacts
def show_all():
    show = ''
    for name, numbers_list in contacts.items():
        for number in numbers_list:
            show += f'name: {name}, contacts: {number},\n'
    return show

@exepting
def exiting():
    return quit()

'''
commands for using same functions
'''
commands = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all,
    "good bye": exiting,
    "close": exiting,
    "exit": exiting
}

'''
do from enter set of commands
'''
@exepting
def extracting_commands(entered_data):
    entered_data.lower().strip()
    command = ''
    for i in commands:
        if entered_data.startswith(i):
            command = i.strip()
            data = entered_data[len(command): ]
    if not command:
        return 'no such command'
    if not data:
        return commands.get(command)()
    data = data.strip().split(' ')
    if len(data)==1:
        return commands.get(command)(data[0])
    elif len(data) == 2:
        return commands.get(command)(data[0], data[1])
    else:
        raise ValueError

def main():
    while True:
        user_date = input("Enter set of command: ")
        result = extracting_commands(user_date)
        if result != None:
            print(result)

if __name__ == '__main__':
    main()
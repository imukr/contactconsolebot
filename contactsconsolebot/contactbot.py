from collections import defaultdict

contacts = defaultdict(list)  # used defeaultdict to make the task easy


def exepting(func): #catching errors
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Please print: name and number'
        except TypeError:
            return 'Wrong command.'
    return inner


@exepting
def hello():
    return 'Can I help You'


@exepting
def add(name, number): #add contacts to phone book
    contacts[name].append(number)
    return f'You added {name} with contact {number}'


@exepting #change phone numbers of contact
def change(name, numbers):
    if name in contacts:
        phones = contacts.get(name)
        if len(phones)>1:
            massege = f'What phone of {" ".join([phone for phone in contacts[name]])} do you want change'
            return massege, name, numbers, phones
        contacts[name].clear()
        contacts[name].append(numbers)
        return f'You changed {name} contact to a {numbers}'
    else:
        contacts[name].append(numbers)
        return f'This contact is not in the phonebook. You append contact {name} with a {numbers}'


def change_existing_number(phone_input, name, numbers):
    global contacts
    phones = contacts[name]
    phones.remove(phone_input)
    phones.append(numbers)
    return f'You change {name} phone {phone_input} on {numbers}'


@exepting #output phone numbers of contact
def phone(name):
    if name in contacts:
        return '\n'.join([phone for phone in contacts[name]])
    return "no such name"


@exepting #Show contacts
def show_all():
    return '\n'.join([f'Name {name}: phone/es {" ".join(numbers)}' for name, numbers in contacts.items()])


@exepting
def exiting():
    return 'Good bye'


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


@exepting
def extracting_commands(entered_data):
    entered_data.lower().strip()
    data=''
    new_command = ''
    for command in commands:
        if entered_data.startswith(command):
            new_command = command.strip()
            data = entered_data[len(command): ]
    if not new_command:
        return ''
    if not data:
        return commands.get(new_command)()
    data = data.strip().split(' ')
    if len(data)==1:
        return commands.get(new_command)(data[0])
    elif len(data) == 2:
        return commands.get(new_command)(data[0], data[1])


def main():
    while True:
        user_date = input("Enter set of command: ")
        result = extracting_commands(user_date)
        if result == 'Good bye':
            break
        if len(result) == 4:
            massage, name, numbers, phones = result
            while True:
                phone_input = input(f'Input phone of {name} what do you want to change: ')
                if phone_input in phones:
                    change_existing_number(phone_input, name, numbers)
                    break
                if phone_input in ['exit', 'good bye']:
                    quit()
                print('Wrong phone number. Chose from list.')
        print(result)


if __name__ == '__main__':
    main()
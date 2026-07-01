# store all events in memory while the program is running
events = []
# store all boxers in memory while the program is running
boxers = []
def add_event():
    '''Add a new event to the events list'''
    print('Adding a new event...')
    title = input('Enter event title: ')
    date = input('Enter event date: ')
    location = input('Enter event location: ')

    event = {'title': title,
          'date': date,
            'location': location,
              'boxers': boxers}
    events.append(event)
def view_events():
    '''View all events in the events list'''
    print('Viewing all events...')
    for event in events:
        print(f"Title: {event['title']}",
               f"Date: {event['date']}",
                 f"Location: {event['location']}")
        print()

def add_boxer():
    '''Add a new boxer to the boxers list'''
    print('Adding a new boxer...')
    boxer_name = input('Enter boxer name:')
    boxer_age = input('Enter age:')
    boxer_weightclass = input('Enter weightclass:')
    boxer_record = input('Enter boxer record:')


    boxer = {'name': boxer_name,
              'age': boxer_age,
              'weight': boxer_weightclass,
              'record': boxer_record}
    boxers.append(boxer)


def view_boxers():
    '''View all boxers in the boxers list'''
    print('Viewing all boxers...')
    for boxer in boxers:
        print(f'Name: {boxer['name']}',
               f'Age: {boxer['age']}',
                 f'Weight class: {boxer['weight']}',
                   f'Record: {boxer['record']}')
        print()

def display_menu():
    '''Display the main menu'''
    print('===Boxing event management system===')
    print('1. Add a new event')
    print('2. View all events')
    print('3. Add a new boxer')
    print('4. View all boxers')
    print('5. Exit')
while True:
    display_menu()
    input_choice = input('choose an option:')
    
    if input_choice == '1':
        add_event()
    elif input_choice == '2':
        view_events()
    elif input_choice == '3':
        add_boxer()
    elif input_choice == '4':
        view_boxers()
    elif input_choice == '5':
        print('Exiting...')
    else:
        print('Invalid choice. please select a number between 1 and 5.')
        break
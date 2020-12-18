def print_menu():
    print('01: PRINCE GEORGE\n'
      '02: RADIUM HOT SPRINGS\n'
      '03: ENGEN\n'
      '04: ELKO')

def source_mill():
    '''
    Generate user input and and return the source mill
    :param user choice
    :return: source mill to pass onto the main program
    '''

    print_menu()

    source_dict = {'01': 'PRINCE GEORGE','02':'RADIUM HOT SPRINGS','03':'ENGEN','04': 'ELKO'}

    # Validate user input with loops
    choice = input('Please make your choice from the menu:\n')
    while choice != '01' and choice != '02' and choice != '03' and choice != '04':
            choice = input('Invalid input. Please try again! \n')

    origin_mill = source_dict[choice]

    return origin_mill


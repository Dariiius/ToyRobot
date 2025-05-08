"""
MAIN | TOY ROBOT TECHNICAL ASSESSMENT 
"""


from robot import Robot


def main():
    """
    MAIN FUNCTION/MENU
    """
    robot = Robot()
    
    while True:
        command = input('Enter a command: ')
        
        if command.startswith('PLACE'):
            try:
                robot.place_robot(command.split()[1])
            except Exception as e:
                print(f'Error: Place command is not valid')
        elif command == 'MOVE':
            robot.move_robot()
        elif command in ['LEFT', 'RIGHT']:
            robot.rotate_robot(command)
        elif command == 'REPORT':
            robot.report()
        elif command == 'SHOW TABLE':
            robot.show_table()
        elif command == 'END':
            print('ENDING SIMULATION')
            break
    

if __name__ == '__main__':
    main()
    
    
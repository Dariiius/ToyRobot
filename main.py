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
        user_input = input('Enter a command: ')
        input_arr = user_input.split()
        command = input_arr[0]
        
        if command == 'PLACE':
            try:
                pos_x, pos_y, direction = input_arr[1].split(',')
                robot.place_robot(pos_x, pos_y, direction)
            except Exception as e:
                print(f'Error: Place command is not valid')
        elif command == 'MOVE':
            robot.move_robot()
        elif command in ['LEFT', 'RIGHT']:
            robot.rotate_robot(command)
        elif command == 'REPORT':
            print(robot.report())
        elif command == 'SHOW':
            robot.show_table()
        elif command == 'END':
            print('ENDING SIMULATION')
            break
    

if __name__ == '__main__':
    main()
    
    
import unittest
from robot import Robot


class TestRobot(unittest.TestCase):
    def test_place_and_report(self):
        robot = Robot()
        robot.place_robot(0, 0, 'NORTH')
        
        self.assertEqual(robot.report(), 'Output: 0,0,NORTH')

    def test_move_north(self):
        robot = Robot()
        robot.place_robot(0, 0, 'NORTH')
        robot.move_robot()
        
        self.assertEqual(robot.report(), 'Output: 0,1,NORTH')

    def test_left_turn(self):
        robot = Robot()
        robot.place_robot(0, 0, 'NORTH')
        robot.rotate_robot('LEFT')
        
        self.assertEqual(robot.report(), 'Output: 0,0,WEST')

    def test_right_turn(self):
        robot = Robot()
        robot.place_robot(0, 0, 'NORTH')
        robot.rotate_robot('RIGHT')
        
        self.assertEqual(robot.report(), 'Output: 0,0,EAST')

    def test_ignore_out_of_bounds(self):
        robot = Robot()
        robot.place_robot(4, 4, 'NORTH')
        robot.move_robot()
        
        self.assertEqual(robot.report(), 'Output: 4,4,NORTH')

    def test_all(self):
        robot = Robot()
        robot.place_robot(1, 2, 'EAST')
        robot.move_robot()
        robot.rotate_robot('LEFT')
        robot.rotate_robot('LEFT')
        robot.move_robot()
        robot.move_robot()
        robot.rotate_robot('RIGHT')
        
        self.assertEqual(robot.report(), 'Output: 0,2,NORTH')


if __name__ == '__main__':
    unittest.main()

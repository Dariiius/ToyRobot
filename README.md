# Toy Robot Simulator

A console-based simulator of a toy robot moving on a 5x5 tabletop. The robot follows a set of commands such as PLACE, MOVE, LEFT, RIGHT, and REPORT.

## Description

This Python application simulates a toy robot that moves on a 5x5 square tabletop. The robot must not fall off the table. It only executes commands after a valid `PLACE` command and safely ignores any that would result in invalid states.

### Supported Commands

- `PLACE X,Y,FACING` — Place the robot on the table at position (X, Y) facing `NORTH`, `SOUTH`, `EAST`, or `WEST`.
- `MOVE` — Move the robot one unit forward in the direction it is currently facing.
- `LEFT` — Rotate the robot 90 degrees left (counter-clockwise).
- `RIGHT` — Rotate the robot 90 degrees right (clockwise).
- `REPORT` — Output the robot’s current position and facing direction.
- `SHOW` (Bonus) — Displays a 2D table in the console.
- `END` — Exits the console application.

The coordinate (0, 0) is the **southwest** corner of the table.

### Limitations

- Only the last added robot can be moved and rotated.
- Robots cannot overlap each other

## 🚀 Getting Started

### Prerequisites

- Python 3.7+

### Installation

1. Clone this repository or download the ZIP.

```bash
git clone https://github.com/Dariiius/ToyRobot.git
```

2. Navigate to the project

```bash
cd ToyRobot
```

3. Run the application in the console

```bash
python main.py
```

### Run Unit Tests

```bash
python -m unittest test_robot.py
```
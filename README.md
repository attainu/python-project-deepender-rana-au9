# ParkingLot
Design a parking lot using Python3 with TDD approach

# Dependencies
You just need Python3. Visit the link https://www.python.org/downloads/ to install Python.

# Description
This repository gives an overview of how we can design a basic parking lot in Python. It creates parking lot with given number of slots. The cars follow Greedy approach while being parked in the slots.

ParkingLot.py script defines the following functions -

1. *create_parking_lot* n 
    >Given n number of slots, create a parking lot with n spaces.
2. *park car_regno* car_color 
    >Parks a vehicle with given registration number and color in the nearest  empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".
3. *status* 
    >Prints the slot number, registration number and color of the parked vehicles.
4. *leave* x 
    >Removes vehicle from slot number x
5. There are few query functions to retrieve slot number from registration number of car, get registration numbers of cars with particular color etc.
6. You can use help command to see all the commands.

**_ParkingLot.py_** can be run through shell or through file containing test cases. An example file run_test_case.txt has been provided in repo.

**_Vehicle.py_** is a separate class where we can define the type of vehicles that can be parked. As of now, it only contains class Car


# Libraries Used
argparse [(click here to know more)](https://docs.python.org/3/howto/argparse.html "About argparse library")

# Setup

To create your own parking lot-
1. Clone the repository
2. Run python ParkingLot.py to run without input test case file. This opens a shell where you can write your commands like -

![Not found](Capture2.png)

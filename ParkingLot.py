import Vehicle
import argparse


class ParkingLot:
	def __init__(self):
		self.capacity = 0
		self.slotId = 0
		self.numOfOccupiedSlots = 0
	#receive capacity from user and create a list of that size and asign -1 to every slot
	def createParkingLot(self,capacity):
		self.slots = [-1] * capacity
		self.capacity = capacity
		return self.capacity
	#return empty slots
	def getEmptySlot(self):
		for i in range(len(self.slots)):
			if self.slots[i] == -1:
				return i
	#park Vehicle if there is any slot available within the capacity
	def park(self,regno,color):
		if regno not in self.slots:
			if self.numOfOccupiedSlots < self.capacity: 
				slotId = self.getEmptySlot()
				self.slots[slotId] = Vehicle.Car(regno,color)
				self.slotId = self.slotId+1
				self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
				return slotId+1
			else:
				return -1
		else:
			print("Already parked")
	#if slotId is present then set -1 in previous index in slots list and remove 1 from numOfOccupiedSlots
	def leave(self,slotId):

		if self.numOfOccupiedSlots > 0 and self.slots[slotId-1] != -1:
			self.slots[slotId-1] = -1
			self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
			return True
		else:
			return False
	#Show all the cars present in parkinglot
	def status(self):

		print("Slot No.\tRegistration No.\tColour")
        
		for i in range(len(self.slots)):
			if self.slots[i] != -1:
				print(str(i+1) + "\t\t" +str(self.slots[i].regno) + "\t\t" + str(self.slots[i].color))
			else:
				continue
	#return list of registration numbers with the  colour given
	def getRegNoFromColor(self,color):

		regnos = []
		for i in self.slots:

			if i == -1:
				continue
			if i.color == color:
				regnos.append(i.regno)
		return regnos
	#return slot number from given registeration number	
	def getSlotNoFromRegNo(self,regno):
		
		for i in range(len(self.slots)):
			if self.slots[i].regno == regno:
				return i+1
			else:
				continue
		return -1
			
	#return list of slot numbers from given color
	def getSlotNoFromColor(self,color):
		
		slotNos = []

		for i in range(len(self.slots)):

			if self.slots[i] == -1:
				continue
			if self.slots[i].color == color:
				slotNos.append(str(i+1))
		return slotNos
	#take input from user as line and according to that perform different functions
	def show(self,line):
		if line.startswith('create_parking_lot'):
			n = int(line.split(' ')[1])
			res = self.createParkingLot(n)
			print('Created a parking lot with '+str(res)+' slots')

		elif line.startswith('park'):
			regno = line.split(' ')[1]
			color = line.split(' ')[2]
			res = self.park(regno,color)
			if res == -1:
				print("Sorry, parking lot is full")
			else:
				print('Allocated slot number: '+str(res))

		elif line.startswith('leave'):
			leave_slotId = int(line.split(' ')[1])
			status = self.leave(leave_slotId)
			if status:
				print('Slot number '+str(leave_slotId)+' is free')

		elif line.startswith('status'):
			self.status()

		elif line.startswith('registration_numbers_for_cars_with_colour'):
			color = line.split(' ')[1]
			regnos = self.getRegNoFromColor(color)
			if len(regnos)==0:
				print("No car found")
			else:	
				print(', '.join(regnos))

		elif line.startswith('slot_numbers_for_cars_with_colour'):
			color = line.split(' ')[1]
			slotNos = self.getSlotNoFromColor(color)
			if len(slotNos) == 0:
				print("No car with this colour")
			else:
				print(', '.join(slotNos))

		elif line.startswith('slot_number_for_registration_number'):
			regno = line.split(' ')[1]
			slotno = self.getSlotNoFromRegNo(regno)
			if slotno == -1:
				print("Not found")
			else:
				print(slotno)

		elif line.startswith('help'):
			print('''Note:-All the commands are case sensitive so please write proper command with proper format.

create_parking_lot N(N is number of slots you want to create):
			To create parking lot with  size N.\n
park VechicleNumber(eg KA-01-HH-1234) VehicleColour(eg White):
			Park a vehicle with vehicle number and colour.\n						
leave slotNo(slotNo is the number which slot you want to remove):
			Empty the slot at given slotNo.\n
status:
			Shows the status if there is any car.\n
registration_numbers_for_cars_with_colour colour:
			Print all the cars with given colour.\n
slot_numbers_for_cars_with_colour colour:
			Print slot number of cars with given colour.\n
slot_number_for_registration_number registrationNumber:
			Print slot number of cars with given registeration number\n
exit:			
			To come out of Parking System

			''')

        

		elif line.startswith('exit'):
			exit(0)


def main():

    
	parkinglot = ParkingLot()
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File")
	args = parser.parse_args()

	print("If you don't know any command then please enter help otherwise continue")
	if args.src_file:
		with open(args.src_file) as f:
			for line in f:
				line = line.rstrip('\n')
				parkinglot.show(line)
	else:
			while True:
				line = input("$ ")
				parkinglot.show(line)

if __name__ == '__main__':
	main()
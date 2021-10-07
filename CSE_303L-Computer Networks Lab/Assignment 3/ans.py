#!/bin/python3
#! @author: @ruhend (Mudigonda Himansh)
#! Assignment 3
#! Stop-and-Wait ARQ Protocol

"""[Stop and Wait ARQ protocol, written in python by Himansh]
	Stop and Wait ARQ protocol  is a method in telecommunications 
	to send information between two connected devices. 
	It ensures that information is not lost due to dropped packets 
	and that packets are received in the correct order.
"""

import sys, select # Will be used to timeout transmissions 

Timeout = 5 # Defining timeout delay

def input(data):
	"""[input function]
		This function is used to convert data to dataBit array
		This would allow us to transmit data bits one after the other
	"""
	dataBitArray = list() # An array to store the dataBit 
	for i in range(len(data)):
		dataBitArray.append(int(data[i])) # Appending data bits into dataBitArray
	print("### DATA TO BE SENT :", data, " ###")
	return dataBitArray # Returning array dataBitArray

def send(dataBit):
	"""[send function]
		A mini-function to send Data Bits
	"""
	print("Sent Bit : ",dataBit) 
	
def senderPlusReceiver(dataBitArray):
	"""[senderPlusReceiver function]
		This function is used to send the data Bits
		Sender -> sends the bits in the array
		Receiver(in this case the user) -> ack the bit received using
			"ack" or
			"Ack" or
			"ACK"
			as the use input
		This function is built in such a way that it combines 
		both programs into one program for better use of resources.

		Therefore this is capable enough to solve both 
		the sender as well as the receiver logic.
	"""
	element = 0
	while element <= len(dataBitArray)-1: # Sending all data bits one after the other using while loop
		send(dataBitArray[element]) 
		i, o, e = select.select( [sys.stdin], [], [], Timeout ) # This would wait for the previously defined timeout seconds for an input from the user
		
		if (i): # if input is received....
			if sys.stdin.readline().strip() == "ack" or sys.stdin.readline().strip() == "Ack" or sys.stdin.readline().strip() == "ACK": # it checks with ACK, Ack, ack. If matches, then it goes on to the next bit
				print(" + Ack received! Sending next Data Bit...")
				element = element + 1
			else: 
				# else, in the case of the input not matching to the previously mentioned 3 accepted ack messages
				# it would count it as corrupted ack, and it would resend the bit, again.
				print(" > Ack Corrupted! Sending again...")
		else:
			# this is the case where there is no ack from the receiver (AKA user in this case)
			# then it waits till the time out is over and then resend the data bit.
			print(" > Ack Lost! Sending again...")
	
	
def main():
	# TEST CASE 1
	data = "10110110" # Data to be transmitted
	dataBitArray = input(data) # Get the DataBitArray
	print("***** Start Of Transmission 1 *****")
	senderPlusReceiver(dataBitArray) # Run Logic Function
	print("*****  End  Of Transmission 1 *****")

	
	# TEST CASE 2
	data = "01101001" # Data to be transmitted
	dataBitArray = input(data) # Get the DataBitArray
	print("***** Start Of Transmission 2 *****")
	senderPlusReceiver(dataBitArray) # Run Logic Function
	print("***** End  Of  Transmission 2 *****")
main()

### End of File ###
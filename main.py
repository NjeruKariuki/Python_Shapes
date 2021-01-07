try:
	import time
	import os
except ImportError as exc:
	print("Error! " + exc)


#variables
dash = '='
space = ' '
star = '*'

global running
running = True

def loading_screen():
	clear_screen()	
	for i in range(10):
		print(space * i + "\nLoading " + dash * i)
		clear_screen()
		time.sleep(.3)

def closing_application():	
	for i in range(10):
		print(space * i + "\nClosing Application! " + dash * i)
		clear_screen()
		time.sleep(.3)

def clear_screen():
	time.sleep(.1)
	os.system("cls")

#this method allows you to view shapes until you press enter
def wait_screen():
	print("\n")
	os.system("pause")

def Welcome_note():	
	print("\tWelcome to Draw_my_f*ckin' shapes with stars!\n")
	print("DRAW MY SHAPES :) \n")
	time.sleep(3)

def first_boot():
	time.sleep(1.5)
	clear_screen()
	Welcome_note()
	loading_screen()

#call this for first boot loading screen
first_boot() 

''' This class defines all methods for all shapes you can draw '''
class Shape:

	def square():
		side = input("Enter length of side: ")
		side = int(side)
		for i in range(side):
			print(space * side + (star+space) * side)

	def pyramid():
		num = input("Enter a number: ")
		num = int(num)
		for i in range(num):
			print(space * (num-1) + star * (i) + star * (i-1))
			num -=1

	def rectangle():
		length = input("Enter length of rectangle: ")
		length = int(length)
		width = input("Enter width of rectangle: ")
		width = int(width)
		for i in range(width):
			print(space * width + (star + space) * length)


	def triangle():
		height = input("Enter height of triangle: ")
		height = int(height)
		spacing = input("Enter spacing of triangle from margin: ")
		spacing = int(spacing)

		for i in range(height):
			print(space * (spacing) + star * (i+1))

	def diamond():
		num = input("Enter a number: ")
		num = int(num)
		middle = (num * 2)-1

		def upper(num):
			for i in range(num):
				print(space * (num) + star * (i) + star * (i-1))
				num -=1

		def lower(num):
			for i in range(num):
				print(space * (i+1) + star * (num-2) + star * (num-1))
				num -=1

		upper(num)
		print(star * middle)
		lower(num)

#drive code
def main():
	time.sleep(2)
	clear_screen()
	print("Shapes: triangle, pyramid, rectangle, square, diamond\n")
	print("\tpress EXIT/exit/99 to close program\n\n")
	choice = input("Enter name of shape you want to draw: ")

	if choice == 'pyramid':
		Shape.pyramid()
		wait_screen()
	elif choice == 'triangle':
		Shape.triangle()
		wait_screen()
	elif choice == 'rectangle':
		Shape.rectangle()
		wait_screen()
	elif choice == 'square':
		Shape.square()
		wait_screen()
	elif choice == 'diamond':
		Shape.diamond()
		wait_screen()
	elif choice == "EXIT" or "exit" or "99":
		closing_application()
		print("Thank you for using my software!\n")
		running = False
		exit(0)
#for looping while running is True
if __name__ == "__main__":
	while  running:
		main()



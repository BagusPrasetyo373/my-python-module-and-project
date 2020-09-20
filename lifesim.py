import mysql.connector as mysql
from mysql.connector import Error
from isvalid import *
from time import sleep
import os
import re

clear = lambda: os.system('cls')

hunger = 0
thirst = 0
money = 0
balance = 0
energy = 0

newplay = False

con_stat = False

try:
	clear()
	db = mysql.connect(host='db4free.net',user='bagusprasetyo16',password='bagus123',database='lifesim')

	if db.is_connected():
		print("Connection Successfull")
		con_stat = True
		cursor = db.cursor(buffered=True)
except Error as e:
	print("Connection Failed, Make Sure To Check Your Internet Connection!")
	con_stat = False

else: pass

def register():

	global newplay
	clear()
	print("Name Is Unregistered Please Type Your Password To Register")
	pasr = str(input("Password: "))

	if len(pasr) < 8:
		clear()
		print("Password is too short min char is 8!")
		sleep(2)
		register()
	elif len(pasr) > 30:
		clear()
		print("Password is too long max char is 30")
		sleep(2)
		register()
	else: 
		cursor.execute("INSERT INTO `account` (`username`, `password`) VALUES ('{}', '{}')".format(nama, pasr))
		cursor.execute("INSERT INTO `status` (`name`) VALUES ('{}')".format(nama))
		cursor.execute("INSERT INTO `finance` (`name`) VALUES ('{}')".format(nama))
		db.commit()
		clear()
		print("account Registered!")
		sleep(2)
		clear()
		print("You are new player, you've earned $500 for help to start your life, good luck!")
		newplay = True
		inGame()
		clear()

def login():
	clear()
	print("Name Is Registered Please Login To Continue")
	pas = str(input("Password: "))

	cursor.execute("SELECT `password` FROM `account` WHERE `password` = '{}'".format(pas))

	if cursor.fetchone() == None:
		clear()
		print("Wrong Password!")
		sleep(2)
		login()
	else:
		clear()
		print("Login Successfull!")
		sleep(2)
		clear()
		newplay = False
		inGame()

def mainMenu():

	global nama

	nama = str(input("Enter Your Name: "))

	if len(nama) == 0:
		clear()
		print("Name Cannot Be Empty!")
		sleep(2)
		mainMenu()

	cursor.execute("SELECT `username` FROM `account` WHERE `username` = '{}'".format(nama))

	if cursor.fetchone() != None:
		login()
	else: register()

def inGame():

	global newplay, hunger, balance, money, thirst, energy

	if newplay == False:
		cursor.execute("SELECT * FROM `status` WHERE `name` = '{}'".format(nama))

		datastat = cursor.fetchone()
		hunger = datastat[1]
		thirst = datastat[2]
		energy = datastat[3]

		cursor.execute("SELECT * FROM `finance` WHERE `name` = '{}'".format(nama))

		datafina = cursor.fetchone()
		money = datafina[1]
		balance = datafina[2]

		newplay = None

	if newplay == True:
		hunger = hunger + 100
		thirst = thirst + 100
		money = money + 500
		balance = balance + 0
		energy = energy + 100
		newplay = None

		cursor.execute("UPDATE `status` SET `hunger` = {}, `thirst` = {}, `energy` = {} WHERE `name` = '{}'".format(hunger, thirst, energy, nama))
		cursor.execute("UPDATE `finance` SET `money` = {}, `balance` = {} WHERE `name` = '{}'".format(money, balance, nama))
		db.commit()

	print("\n\n\n\nLife Simulator v0.0.01[alpha]")

	cmd = str(input("Commands: "))

	if cmd == "sleep":
		clear()
		conf = str(input("Are You Sure Want To Go To Sleep? (y/n)\n"))
		csr = conf.upper()

		if csr == "Y":
			clear()
			for i in range(0,100):
				i += 1
				clear()
				print(f"Sleeping %{i}")
				sleep(0.3)
			clear()
			energy = 100
			if hunger > 0 and thirst > 0:
				hunger = hunger - 10
				thirst = thirst - 10
			print("You Feel Well Rested After Sleeping!")
			inGame()
		elif csr == "N":
			clear()
			inGame()
		else:
			clear()
			print("Invalid Input")
			inGame()
	if cmd == "update":
		clear()
		print("Changelog:")
		print("[20/09/2020]: Energy & Sleep System Added, Bug Fixed")
		print("[19/09/2020]: Game Created, Bank Feature Added, Hunger & Thrist System Added, Food Shop Added, Work Added")
		inGame()

	if cmd == "help":
		clear()
		print("Help/Commands: stat, money/wallet, shop, quit, bank, work")
		inGame()
	if cmd == "stat":
		clear()
		print(f"Hunger: {hunger}")
		print(f"Thrist: {thirst}")
		print(f"Energy: {energy}")
		inGame()
	if cmd == "money" or cmd == "wallet":
		clear()
		print(f"Money: ${money}")
		inGame()
	if cmd == "shop":
		clear()
		print(f"[shop] food")
		inGame()
	if cmd == "shop food":
		clear()
		print("ID Food\tStat Point\tPrice")
		print("1).Bread\t+30[hunger]\t$10")
		print("2).Water\t+10[thirst]\t$3")
		print("0.[Exit]")

		try:
			foodcmd = int(input("Select: "))
			if is_int(foodcmd) == True:
				if foodcmd == 0:
					clear()
					inGame()
				if foodcmd == 1:
					if money > 30:
						if hunger <= 70:
							clear()
							print("You Ate Bread [hunger +30]")
							hunger = hunger + 30
							money = money - 10
							inGame()
						else:
							clear()
							print("You Don't Feel Hungry!")
							inGame()
					else:
						clear()
						print("Not Enough Money!")
						inGame()
				if foodcmd == 2:
					if money > 3:
						if thirst <= 90:
							clear()
							print("You Drink Water [thirst +10]")
							thirst = thirst + 10
							money = money - 3
							inGame()
						else:
							clear()
							print("You Don't Feel Thristy!")
							inGame()
					else:
						clear()
						print("Not Enough Money!")
						inGame()
				else:
					clear()
					print("invalid input!")
					inGame()
		except:
			clear()
			print("Invalid Input")
			inGame()
	if cmd == "quit":
		clear()
		print("Your Progress Has Been Saved!")
		cursor.execute("UPDATE `status` SET `hunger` = {}, `thirst` = {}, `energy` = {} WHERE `name` = '{}'".format(hunger, thirst, energy, nama))
		cursor.execute("UPDATE `finance` SET `money` = {}, `balance` = {} WHERE `name` = '{}'".format(money, balance, nama))
		db.commit()
		clear()
		print("Quiting Please Wait...")
		sleep(5)
		clear()
		exit()
	if cmd == "bank":
		clear()
		print("Bank:\n[bank] deposit\n[bank] withdraw\n[bank] balance")
		inGame()
	if cmd == "bank deposit":
		clear()
		try:
			depoam = int(input("Type How Much Money To Deposit: $"))

			if is_int(depoam) == True:
				if money >= depoam:
					clear()
					money = money - depoam
					balance = balance + depoam
					print(f"You Deposited ${depoam}, Your Balance Is: ${balance}")
					inGame()
				else:
					clear()
					print("You Don't Have That Much Money!")
					inGame()
		except:
			clear()
			print("Input Invalid")
			inGame()
	if cmd == "bank withdraw":
		clear()
		try:
			witham = int(input("Type How Much Money To Withdraw: $"))
		
			if is_int(witham) == True:
				if balance >= witham:
					clear()
					balance = balance - witham
					money = money + witham
					print(f"You Withdrawed ${witham}, Your Balance Is: ${balance}")
					inGame()
				else:
					clear()
					print("You Don't Have That Much Money In Your Balance")
					inGame()
		except:
			clear()
			print("Input Invalid")
			inGame()
	if cmd == "bank balance":
		clear()
		print(f"Your Balance Is: ${balance}")
		inGame()

	if cmd == "work":
		clear()
		print("ID Work\tStat Point\tSalary\tTime")
		print("1).carwash\thunger[-10]thirst[-20]energy[-30]\t$20\t2h")
		print("2).cashier\thunger[-30]thirst[-10]energy[-20]\t$30\t4h")
		print("0.[Exit]")

		try:
			workcmd = int(input("Select: "))

			if is_int(workcmd) == True:
				if workcmd == 1:
					if hunger > 10:
						if thirst > 20:
							if energy > 30:
								clear()
								for i in range(0,100):
									i += 1
									clear()
									print(f"Work %{i}")
									sleep(0.08)
								clear()
								print("Work Summary:")
								print("hunger -10")
								print("thirst -20")
								print("energy -30")
								print("earning +$20")
								hunger = hunger - 10
								thirst = thirst - 20
								money = money + 20
								energy = energy - 30
								inGame()
							else:
								clear()
								print("You Feel Tired, Go Sleep And Work Toomorrow!")
								inGame()
						else:
							clear()
							print("You Feel Thristy, Go Get Some Drinks!")
							inGame()
					else:
						clear()
						print("You Feel Hungry, Go Get Some Foods!")
						inGame()
				if workcmd == 2:
					if hunger > 30:
						if thirst > 10:
							if energy > 20:
								clear()
								for i in range(0,100):
									i += 1
									clear()
									print(f"Work %{i}")
									sleep(0.5)
								clear()
								print("Work Summary:")
								print("hunger -30\nthirst -10\nenergy -20\nearning +$30")
								hunger = hunger - 30
								thirst = thirst - 10
								money = money + 30
								energy = energy - 20
								inGame()
							else:
								clear()
								print("You Feel Tired, Go Sleep And Work Toomorrow")
								inGame()
						else:
							clear()
							print("You Feel Thristy, Go Get Some Drinks!")
							inGame()
					else:
						clear()
						print("You Feel Hungry, Go Get Some Foods!")
						inGame()
				if workcmd == 0:
					clear()
					inGame()
				else:
					clear()
					print("invalid input!")
					inGame()
		except:
			clear()
			print("invalid input")
			inGame()
	else:
		clear()
		print("Invalid Input!")
		inGame()

if con_stat == True: mainMenu()
class Logic_Gate:

	def AND(a, b):
		if a == b:
			return True

		else:
			return False

	def OR(a, b):
		if a == 1 or b == 1:
			return True

		else:
			return False

	def XOR(a, b):
		if a == 1 and b == 0:
			return True

		if b == 1 and a == 0:
			return True

		if a == 1 and b == 1:
			return False

		else:
			return False

	def NOT(i):
		if i == 1:
			return False

		else:
			True

	def NAND(a, b):
		if a == b:
			return False

		else:
			return True

	def NOR(a, b):
		if a == 1 or b == 1:
			return False

		else:
			return True

	def XNOR(a, b):
		if a == 1 and b == 0:
			return False

		if b == 1 and a == 0:
			return False

		if a == 1 and b == 1:
			return True

		else:
			return True

class Circuit:

	def HALF_ADDER(a,b):
		carry_out = False
		if a == 1 and b == 0:
			carry_out = False
			return True

		elif a == 0 and b == 1:
			carry_out = False
			return True

		elif a == 1 and b == 1:
			carry_out = True
			return False

		else:
			carry_out = False
			return False

	def FULL_ADDER(a,b,cin):
		carry_out = False
		if a == 1 and b == 0 and cin == 0:
			carry_out = False
			return True

		elif a == 0 and b == 1 and cin == 0:
			carry_out = False
			return True

		elif a == 1 and b == 1 and cin == 0:
			carry_out = True
			return False

		elif a == 0 and b == 0 and cin == 1:
			carry_out = False
			return True

		elif a == 1 and b == 0 and cin == 1:
			carry_out = True
			return False

		elif a == 0 and b == 1 and cin == 1:
			carry_out = True
			return False

		elif a == 1 and b == 1 and cin == 1:
			carry_out = True
			return True

		else:
			carry_out = False
			return False

	def MULTIPLEXER(a, b, q):
		if a == 1 and b == 0 and q == 0:
			return False

		elif a == 0 and b == 1 and q == 0:
			return True

		elif a == 1 and b == 1 and q == 0:
			return True

		elif a == 0 and b == 0 and q == 1:
			return False

		elif a == 1 and b == 0 and q == 1:
			return True

		elif a == 0 and b == 1 and q == 1:
			return False

		elif a == 1 and b == 1 and q == 1:
			return True

		else:
			return False

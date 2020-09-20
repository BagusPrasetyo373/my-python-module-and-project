#unfinished yet :(

class bit:
	def byte(i):
		return i / 8
	def kilobit(i):
		return i / 1000
	def kilobyte(i):
		return i / 8000
class byte:
	def bit(i):
		return i * 8
	def kilobit(i):
		return i / 125
	def kilobyte(i):
		return i / 1000
	def megabit(i):
		return i / 125000
class kilobit:
	def bit(i):
		return i * 1000
	def byte(i):
		return i * 125
	def kilobyte(i):
		return i / 8
	def megabit(i):
		return i / 1000
	def megabyte(i):
		return i / 8000
if __name__ == "__main__":
	print("~-PyDataConv-~")
	print("description: convert or calculate data for example like x bit to byte etc.")

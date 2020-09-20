#package created by Bagus Prasetyo
# Email : bagusidm373@gmail.com

class Second:
	def sec_to_ms(int):
		if int is None:
			raise ValueError("Int Value is None!")
		res = int * 1000
		return res
	def ms_to_sec(int):
		if int is None:
			raise ValueError("Int Value is None!")
		res = int / 1000
		return res
class Minute:
	def min_to_ms(int):
		if int is None:
			raise ValueError("Int Value is None!")
		res = int * 60000
		return res
	def ms_to_min(int):
		if int is None:
			raise ValueError("Int Value is None!")
		res = int / 60000
		return res
class Hour:
	def hr_to_ms(int):
		if int is None:
			raise ValueError("Int Value is None!")
		res = int * 3600000
		return res
	def ms_to_hr(int):
		if int is None:
			raise ValueError("Int Value is None!")
		res = int / 3600000
		return res

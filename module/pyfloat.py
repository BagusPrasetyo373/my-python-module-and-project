import math
def floatround_round(floatround):
	return round(floatround)
def floatround_to_zero(floatround):
	return round(floatround, 0)
def floatround_floor(floatround):
	return math.floor(floatround)
def floatround_ceil(floatround): #round upwards
	return math.ceil(floatround)
def floatround(x, method):
	return method(x)
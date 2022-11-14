from pprint import pprint
n = 15  # TODO решить с помощью list comprehension и распечатать его
pprint([{"bin": bin(number), "dec": number, "hex": hex(number), "oct": oct(number)} for number in range(0, n+1)])

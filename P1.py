from sys import argv

name, time, salaries, additive = argv

print("Ваша заработная плата:" + str(int(time) * int(salaries) + int(additive)))
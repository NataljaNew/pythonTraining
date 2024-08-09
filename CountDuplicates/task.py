import sys
my_data = list(map(str.strip, sys.stdin))

print(len(my_data)-len(set(my_data)))

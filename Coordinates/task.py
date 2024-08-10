import sys

for pair in sys.stdin:
    x, y = eval(pair)
    print(-90 <= x <= 90 and -180 <= y <= 180)

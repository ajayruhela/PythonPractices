# draw dot pattern
import sys
from math import cos, radians

# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    return ' ' * int(20 * cos(radians(x)) + 20) + 'o'

for i in range(360):
    s = make_dot_string(i)
    print(s)
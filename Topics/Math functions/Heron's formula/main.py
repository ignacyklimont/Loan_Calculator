# put your python code here
import math
side_1 = int(input())
side_2 = int(input())
side_3 = int(input())
p = (side_3 + side_2 + side_1)/2
s = math.sqrt((p*(p - side_1)*(p - side_2)*(p - side_3)))
print(s)




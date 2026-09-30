from typing import List,Tuple

# Unpacking
point1 = [0,0]
point2 = [2,4]

# unpacking of elements 
# x1 point1[0], x2 point2[0]
# y1 point1[1] ,y2 point2[0]

x1,y1 = point1
x2,y2 = point2

slope = (y2-y1)/(x2-x1)
print(x1,x2)
print(y1,y2)
print(slope)


def sum_3_integers(nums:List[int]) -> int:
    x1,x2,x3 = nums
    return x1+x2+x3

def compute_volume(box_dimesnions:Tuple[int, int , int]) -> int:
    width, height, depth = box_dimesnions
    return width*height*depth

print(sum_3_integers([1,2,3]))
print(compute_volume((3,2,3)))






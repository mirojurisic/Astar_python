
from helpers import load_map_40
from student_code import shortest_path
from test import test


map_40 = load_map_40()

path = shortest_path(map_40, 8, 24)
if path == [8, 14, 16, 37, 12, 17, 10, 24]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")   
    
    print(path)

test(shortest_path)

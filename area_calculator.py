lenght = float(input("please enter rug length: "))
width = float(input("please enter rug width: "))
rug_area = lenght * width

room_lenght = float(input("please enter room length: "))
room_width = float(input("please enter room width: "))
room_area = room_lenght * room_width

print(f"area of rug is {rug_area}")
print(f"area of room is {room_area}")


print(f"area of rug is {(rug_area / room_area)* 100}% of the room ")

lenght_2 = float(input("please enter lenght of rectangle: "))
width_2 = float(input("please enter width of rectangle: "))
rectangle_area = lenght_2 * width_2

print(f"area of rectangle is {rectangle_area}")

triangle_base = float(input("please enter base: "))
triangle_height = float(input("please enter height: "))
triangle_area =(triangle_base * triangle_height) *1/2
print (f"area of triangle is {triangle_area}")



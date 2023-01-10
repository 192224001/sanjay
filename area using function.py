def area_circle(r):
     area_circle=(3.14*r*r)
     return(area_circle)
def area_triangle(b,h):
    area_triangle=(1/2*b*h)
    return(area_triangle)
def area_square(a):
    area_square=(a*a)
    return(area_square)
print("1.area of circle")
print("2.area of triangle")
print("3.area of square")
choice=int(input("enter a choice"))
if choice==1:
    r=int(input("enter a radius"))
    print("circle",area_circle(r))
elif choice==2:
    b=int(input("enter a breadth"))
    h=int(input("enter a height"))
    print("triangle",area_triangle(b,h))
elif choice==3:
    a=int(input("enter a area"))
    print("square",area_square(a))

    

    

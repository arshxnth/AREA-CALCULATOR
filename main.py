#Calculating Area of Shapes
def area_calculator():
    print("-----Welcome to Area Calculator-----")
    while True:
        print("Choose which Area you need to Calculate")
        print("\n1.Square")
        print("2.Rectangle")
        print("3.Circle")
        print("4.Exit")

        select=int(input("\nWhat Shape Do You Want to Check the Area For : "))

        if select==1:
            side=float(input("Enter the Side : "))
            area=side**2
            print("The Area of the Square is ",area)  
            
        elif select==2:
            length=float(input("Enter the Length : "))
            breadth=float(input("Enter the Breadth : "))
            area=length+breadth
            print("The Area of the Rectangle is ",area)

        elif select==3:
            radius=float(input("Enter the Radius : "))
            area= 3.14*radius**2
            print("The Area of Circle is ",area)
            
        elif select==4:
            print("Exit Successfully") 
        else:
            print("Error Occured")

area_calculator()
        
            

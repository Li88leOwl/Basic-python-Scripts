#create a dictionary that will let you add an employee and their ID number,status,Gender etc.
#You will need a while loop ot complete this task

employee_id = {}

off = False
while not off:
    name = input("Enter Employee's name: ")
    id = input("Enter ID: ")
    employee_id[name] = id
    print("Employee added successfully")
    print(employee_id)
    add_another = input("Would like to add another employee? Y/N  ").lower()
    if add_another == "y":
        pass
    else:
     off = True


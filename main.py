import datetime
from collections import Counter
def transferring_data(directory):
    """This function is to transfer data from file to dictionaries"""
    #https://www.geeksforgeeks.org/python-datetime-strptime-function/ used this function to format time
    #https://cmdlinetips.com/2016/01/opening-a-file-in-python-using-with-statement/ used with statement to open a file in read mode
    data_of_employees = []
    with open(directory, 'r') as file:
        for line in file:
            employee_ID, username, date_joined, Gender, salary = line.split(', ')
            data_of_employees.append({
                'date_joined': datetime.datetime.strptime(date_joined, "%Y%m%d"),
                'username': username,
                'employee_ID': employee_ID,
                'salary': int(salary),
                'Gender': Gender
            })
    return data_of_employees

def saving_data(directory, data_of_employees):
    """Function that saves data to employees file """
    #https://www.w3schools.com/python/python_file_write.asp used with statement to open the file in write mode
    with open(directory, 'w') as file:
        for info in data_of_employees:
            date = info['date_joined'].strftime("%Y%m%d")
            file.write(f"{info['employee_ID']}, {info['username']}, {date}, {info['Gender']}, {info['salary']}\n")


def Menu_admin():
    print("\nAdmin Menu:")
    print("1. Display Stats")
    print("2. Add Employee")
    print("3. Display All Employees")
    print("4. Change an Employee's Salary")
    print("5. Remove an Employee")
    print("6. Raise an Employee's Salary")
    print("7. Exit")

def Menu_Employee():
    print("\nEmployee Menu:")
    print("1. Check Salary")
    print("2. Exit")

def adding_new_employee(data_of_employees):
    # https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/zfill/python-string-zfill/
    # using the rjust() to format new employee id
    username = input("Enter username of new employee: ")
    new_ID = f"emp{str(len(data_of_employees) + 1).rjust(3, '0')}"
    salary = int(input("Enter the salary: "))
    Gender = input("Enter gender, (male/female): ")
    data_of_employees.append({
        'date_joined': datetime.datetime.now(), # now for formatting joining timegit 
        'username': username,
        'employee_ID': new_ID,
        'salary': salary,
        'Gender': Gender
    })
    print("New employee was added!")
def Main_program():
    data_of_employees = transferring_data("employees.txt")
    numb_of_attempts = 0
    numb_of_max_attempts = 5
    while numb_of_attempts < numb_of_max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == 'admin' and password == 'admin123123':
            print("Welcome,Admin!")
            while True:
                Menu_admin()
                choice = input("Enter choice: ")
                if choice == '1':
                    print('1')
                elif choice == '2':
                    adding_new_employee(data_of_employees)
                elif choice == '3':
                    print('3')
                elif choice == '4':
                    print('4')
                elif choice == '5':
                    print('5')
                elif choice == '6':
                    print('6')
                elif choice == '7':
                    saving_data("employees.txt",data_of_employees)
                    print("Saving Data, Exiting...")
                    break
                else:
                    print("Please select a valid option!")
        elif username == 'admin' and password != 'admin123123':
            print("Invalid password and/or username")

        is_employee = False
        for employee in data_of_employees:
            if employee['username'] == username and password == "":
                    Sex = employee['Gender']
                    if Sex == 'male':
                        notation = 'Mr.'
                    else:
                        notation = 'Ms.'
                    print(f"Hello {notation}{username}!")
                    while True:
                        Menu_Employee()
                        goal = input("Enter goal: ")
                        if goal == '1':
                            print(f"Your salary is ${employee['salary']}")
                        elif goal == '2':
                            print("Terminating System")
                            #https://www.geeksforgeeks.org/python-now-function/ use of now() function
                            #link above in first function for hours,minutes and seconds formatting
                            Timestamp = datetime.datetime.now()
                            Timestamp_formatted = Timestamp.strftime("%Y%m%d %H:%M:%S")
                            with open("login_timestamp.txt", 'a') as file: # using with statement in append mode
                                file.write(f"{username}, {Timestamp_formatted}\n")
                            break
                        else:
                            print("Please select a valid option!")
                    break
        if not is_employee and (username != "admin" or password != 'admin123123'):
            numb_of_attempts += 1
        if numb_of_attempts >= numb_of_max_attempts:
            print("You have reached maximum number of login attempts. Goodbye.")

Main_program()

















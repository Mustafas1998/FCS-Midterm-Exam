import datetime
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
                'Gender': Gender,
            })
    return data_of_employees

def saving_data(directory, data_of_employees):
    """Function that saves data to employees file """
    #https://www.w3schools.com/python/python_file_write.asp used with statement to open the file in write mode
    with open(directory, 'w') as file:
        for info in data_of_employees:
            date = info['date_joined'].strftime("%Y%m%d")
            file.write(f"{info['employee_ID']}, {info['username']}, {date}, {info['Gender']}, {info['salary']}\n")



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
                print("\nAdmin Menu:")
                print("1. Display Stats")
                print("2. Add Employee")
                print("3. Display All Employees")
                print("4. Change an Employee's Salary")
                print("5. Remove an Employee")
                print("6. Raise an Employee's Salary")
                print("7. Exit")
                choice = input("Enter choice: ")
                if choice == '1':
                    statistics(data_of_employees)
                elif choice == '2':
                    new_employee(data_of_employees)
                elif choice == '3':
                    display_employees(data_of_employees)
                elif choice == '4':
                    changing_salary(data_of_employees)
                elif choice == '5':
                    removing_employee(data_of_employees)
                elif choice == '6':
                    raising_salary_by_percentage(data_of_employees)
                elif choice == '7':
                    saving_data("employees.txt",data_of_employees)
                    print("Saving Data, Bye...")
                    break
                else:
                    print("Please select a valid option!")












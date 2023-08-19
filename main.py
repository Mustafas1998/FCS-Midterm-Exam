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






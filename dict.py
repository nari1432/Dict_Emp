#add an employee with domain, name, empid, and email details using user input
# and then print the employee's details. in python

employees = {}

domain = input("Enter domain: ")
name = input("Enter name: ")
empid = input("Enter employee ID: ")
email = input("Enter email: ")
employee_details = {
    "Domain": domain,
    "Name": name,
    "Employee ID": empid,
    "Email": email
}

employees[empid] = employee_details


print("\nEmployee Details:")
for key, value in employee_details.items():
    print(f"{key}: {value}")

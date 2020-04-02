"""
Write a program that calculates and prints the monthly paychecks for an employee.
The net pay is calculated after taking the following deductions:
Absences:   ₱689.66
Lates:      ₱178.75
SSS:        ₱320.00
Philhealth: ₱200.00
HDMF:       ₱536.25
WTAX:       ₱310.23
Salary Loan:₱7000.00
SSS Loan:   ₱3000.00
HDMF Loan:  ₱1500.00
HMO:        ₱3530.13

Your program should prompt the user to input the gross amount and the employee name.
The output will be stored in a file. Format your output to have two decimal places.
"""

gross_amount = input("Gross amount: ")
employee_name = input("Employee name: ")

employee = employee_name + "\n"
employee += "Gross Amount:               ₱ " + gross_amount + "\n"
# This statement creates a temporary variable 'file' and automatically close at the end of statement, even if exceptions occurs.
with open("employeeData.txt", "w") as file:
    file.write(employee)

deductions = """Absences:                   ₱ 689.66
Lates:                      ₱ 178.75
SSS:                        ₱ 320.00
Philhealth:                 ₱ 200.00
HDMF:                       ₱ 536.25
WTAX:                       ₱ 310.23
Salary Loan:                ₱ 7000.00
SSS Loan:                   ₱ 3000.00
HDMF Loan:                  ₱ 1500.00
HMO:                        ₱ 3530.13
"""
total_deductions = 689.66 + 178.75 + 320.00 + 200.00 + 536.25 + 310.23 + 7000.00 + 3000.00 + 1500.00 + 3530.13
net_pay = abs(float(gross_amount) - total_deductions) # The abs function is used to return absolute value of a number.
deductions += "Net Pay:                    ₱ " + "{:.2f}". format(net_pay) # {:.2f} formats a two decimal places

with open("employeeData.out", "w") as file:
    file.write(employee + deductions)

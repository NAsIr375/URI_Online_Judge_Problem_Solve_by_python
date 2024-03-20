employee_number = int(input())
worked_hour = int(input())
received_per_hour = float(input())

s = worked_hour*received_per_hour
print("NUMBER =",employee_number)
print("SALARY = U$ %.2f" %s)
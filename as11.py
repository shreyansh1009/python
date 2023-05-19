
basic_salary = float(input("Enter basic salary: "))


if basic_salary <= 10000:
    hra = 0.2 * basic_salary
    da = 0.8 * basic_salary
elif basic_salary <= 20000:
    hra = 0.25 * basic_salary
    da = 0.9 * basic_salary
else:
    hra = 0.3 * basic_salary
    da = 0.95 * basic_salary


gross_salary = basic_salary + hra + da


print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)

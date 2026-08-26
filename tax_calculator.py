def calculateTaxForContract(tax_percent):
    tax = salary * tax_percent / 100
    insurance = salary * 5/100
    salary = salary - tax - insurance
    print(f"Lương của bạn là {salary} - và thuế là {tax}")
    
while True:
    username = input("Enter your name: ")
    salary = float(input("Enter your salary: "))
    insurance = 0
    tax = 0
    print(f"Welcome user {username}")
    print("Please choose your contract type")
    print("1. Freelance")
    print("2. Full-time with contract")
    print("3. Part-time")
    print("4. Part time with contract")

    choice = int(input("Enter your choice: "))

    if choice == 1 or choice == 3:
        if salary >= 2000000 and choice == 1:
            tax = salary * 10 / 100
            salary = salary - tax
            print(f"Lương của bạn là {salary} - và thuế là {tax}")
        elif salary >= 2000000 and choice == 3:
            percent = 10
            calculateTaxForContract(percent)
    if choice == 2:
        sal_range = int(input("Enter Salary Range:"))
        if sal_range == 1 and salary >= 10000000 and salary < 20000000:
            percent = 10
            calculateTaxForContract(percent)
        elif sal_range == 1 and salary >= 20000000 and salary < 30000000:
            percent = 20
            calculateTaxForContract(percent)
        else:
            percent = 30
            calculateTaxForContract(percent)




                   

num_heads = int(input("Enter the number of heads in the farm: "))
num_feet = int(input("Enter the number of feet in the farm: "))


num_goats = (num_feet - 2*num_heads) / 2
num_chickens = num_heads - num_goats


print("The number of chickens in the farm is:", int(num_chickens))
print("The number of goats in the farm is:", int(num_goats))

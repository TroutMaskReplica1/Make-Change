q = 25
d = 10
n = 5
p = 1

z = input("$ ")

y = float(z) * 100
x = int(y)

print(x//25, "quarters")
x = x % 25
print(x//10, "dimes")
x = x % 10
print(x//5, "nickels")
x = x % 5
print(x//1, "pennies")

dollars = [100,50,20,10,5,1,0.25,0.10,0.05,0.01]
file = float(input("number: "))
task = file
total = []
for x in dollars:
  total.append(task // x)
  task %= x
print(f"{int(total[0])} hundred dollar bill(s)")
print(f"{int(total[1])} fifty dollar bill(s)")
print(f"{int(total[2])} twenty doller bill(s)")
print(f"{int(total[3])} ten doller bill(s)")
print(f"{int(total[4])} five doller bill(s)")
print(f"{int(total[5])} one doller bill(s)")
print(f"{int(total[6])} quarter(s)")
print(f"{int(total[7])} dimes(s)")
print(f"{int(total[8])} nickels(s)")
print(f"{int(total[9])} penny(s)")

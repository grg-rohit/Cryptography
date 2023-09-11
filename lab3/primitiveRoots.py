mod = int(input("Enter the modulo number: "))
list = []
test_list = []
for i in range(1,mod):
  list.append(i)

a = int(input("Enter number to test: "))

check = True

for i in list:
  t = (a**i)%mod
  if t in test_list:
    check = False
    break
  else:
    test_list.append(t)
    check = True
  print(t)
if check == False:
  print(f"{a} is not a primitive root of {mod}.")
else:
  print(f"{a} is a primitive root of {mod}.")
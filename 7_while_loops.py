#while loop in python to check for even and odd numbers
count = 0

while (count <= 10):
    print (f"Counter is currently at {count}")
    if (count%2 == 0):
        print(f"{count} is even")
    else:
        print(f"{count} is odd")
    count += 1
print ("Loop complete")

#While with Break
print("While with Break")
i = 2
while i < 10:
  print(i)
  if i == 6:
    break
  i += 1

#While with continue
print("While with continue")
i = 2
while i < 10:
  i += 1
  if i == 4:
    continue
  print(i)


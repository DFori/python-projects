weight = int(input('enter your weight: '))
type = input("(K)gs or (L)bs: ")
if type == "k" or "k".upper():
    converted = weight / 0.45
    if weight >= 50:
        print("you are fat")
    else:
        print("you are sick like fori")
else:
    converted = weight * 0.45
    print("you are sick like fori")
print(converted)
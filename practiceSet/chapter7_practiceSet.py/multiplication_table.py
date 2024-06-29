num = int(input("Enter a number to get the multiplication table: "))

for i in range (1, 21):
    print(f"{str(num)} x {str(i)} = {str(i*num)}")
def classify_number(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"

#Ask user for an integer and classify the number as even or odd    
num = int(input("Enter a number: "))
print(f"The number {num} is {classify_number(num)}")

#Generate list of even numbers between 1 and 50
even_numbers = [i for i in range(1, 51) if i % 2 == 0]
print(even_numbers)

#Print numbers from 10 to 1 in reverse order using a while loop
count = 10
while count > 0:
    print(count)
    count -= 1


    
number_list = list(input("Enter the values to the list (separated by commas): ").split(","))
number_list = [int(num) for num in number_list]

even_numbers_found = False
odd_sum = 0
tuple_list = tuple(number_list)

for num in number_list:
    if num % 2 == 0:
        even_numbers_found = True
    elif num % 2 != 0:
        odd_sum += num

if even_numbers_found:
    print("Even numbers found in the list.")
else:
    print("No even numbers found.")

print("Sum of odd numbers:", odd_sum)
print("Tuple list:", tuple_list)

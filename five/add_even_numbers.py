total_even=0
for index in range(1,101):
    if index%2==0:
        total_even+=index
print(f"Total of the all even numbers is : {total_even}")
#or
second_total=0
for second_index in range(2,101,2):
    second_index+=second_index
print(total_even)
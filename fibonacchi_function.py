"""Author:Liya Binu
Date:3-12-2024
program to generate fibonacchi numbers """
def generate_fibonacchi(n):
    sequence=[]
    first_number,second_number=0,1
    for _ in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence
print(generate_fibonacchi(10))
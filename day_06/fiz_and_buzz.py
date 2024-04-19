# In the FizzBuzz problem, you will be given an integer, and you need to return a string array where:

#    A. The numbers that are divisible by 3 will be replaced with the word “Fizz”;
#    B. The numbers that are divisible by 5 will be replaced with the word “Buzz”;
#    C. And the numbers that are divisible by both 3 and 5 will be replaced by the word “FizzBuzz”;



def fizzBuzz(n):
    output = []

    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    return output

print(fizzBuzz(20))
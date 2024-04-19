
# Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in the input array.


def missing(num):
    number = set(num)
    length = len(num)

    output = []


# I have started my range from 5 you can start from 1
    for i in range(5, num[-1]): # num[-1] returns last item ot an array
        if i not  in num:
            output.append(i)

    return output


# Take a list of numbers from the user
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(missing(numbers))
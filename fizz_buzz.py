Given a number n, for each integer / in the range from 1 to n inclusive, print one value per line as follows:
If / is a multiple of both 3 and 5. print FizzBuzz.
If i is a multiple of 3 (but not 5), print Fizz.
• If / is a multiple of 5 (but not 3), print Buzz.
• If is not a multiple of 3 or 5, print the value of i.
Function Description
Complete the function fizzBuzz in the editor below.
fizzBuzz has the following parameter(s):
int n: upper limit of values to test (inclusive)
Returns: NONE
Prints:
The function must print the appropriate response for each value / in the set (1, 2, ... n} in ascending order, each on a separate line.


def fizz_buzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result

n = int(input("Enter a number (n): "))
result = fizz_buzz(n)

for item in result:
    print(item)

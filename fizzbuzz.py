def fizzbuzz_convert(number):
    if number % 3 == 0:
        return 'Fizz'
    return number


assert fizzbuzz_convert(1) == 1
assert fizzbuzz_convert(2) == 2
assert fizzbuzz_convert(3) == 'Fizz'
assert fizzbuzz_convert(5) == 'Buzz'
assert fizzbuzz_convert(6) == 'Fizz'
assert fizzbuzz_convert(10) == 'Buzz'
assert fizzbuzz_convert(15) == 'FizzBuzz'
assert fizzbuzz_convert(30) == 'FizzBuzz'

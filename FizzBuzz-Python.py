range

numbers= range(1,101)
Fizz = 0
Buzz = 0
FizzBuzz =0
for numbers in numbers:
    if numbers % 5 == 0 and numbers % 3 == 0:
        FizzBuzz += 1
        (print("🍎🥤 FizzBuzz"))
    elif numbers % 3 == 0:
        Fizz += 1
        print("🍎 Fizz")
    elif numbers % 5 == 0:
        Buzz += 1
        print("🥤 Buzz")
    else:
        print(numbers)

print(f"SCORE:\n🍎Fizz: {Fizz} times\n"
      f"🥤Buzz: {Buzz} times\n🍎🥤FizzBuzz: {FizzBuzz} times ")
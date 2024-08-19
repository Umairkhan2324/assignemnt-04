def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
def main():
    name = input("Enter your name: ")
    num1 = int(input("Enter your first favorite number: "))
    num2 = int(input("Enter your second favorite number: "))
    num3 = int(input("Enter your third favorite number: "))
    numbers = [num1, num2, num3]
    print(f"\nHello, {name}! Let's explore your favorite numbers:")
    even_odd_info = []
    for num in numbers:
        if num % 2 == 0:
            even_odd_info.append((num, "even"))
        else:
            even_odd_info.append((num, "odd"))
    for num, info in even_odd_info:
        print(f"The number {num} is {info}.")
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num**2})")
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number.")
if __name__ == "__main__":
    main()
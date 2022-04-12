def main():
    num = int(input("What is the Number"))

    if num % 15 == 0:
      print("FizzBuzz")
    if num % 5 == 0:
      print("buzz")
    if num % 3 == 0:
      print("Fizz")
    else:
      print(num)

if __name__ =='__main__':
    main()

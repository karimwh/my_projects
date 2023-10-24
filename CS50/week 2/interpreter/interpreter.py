def main():
    user_input = input('Expression : ').strip()

    x , y , z = user_input.split(" ")

    num_1 = float(x)
    num_2 = float(z)

    if y == "+":
        result = num_1+num_2
        print(f"your result is {result}")
    elif y == "-":
        result = num_1-num_2
        print(f"your result is {result}")
    elif y == "*":
        result = num_1*num_2
        print(f"your result is {result}")
    elif y == "/":
        result = num_1/num_2
        print(f"your result is {result}")

main()



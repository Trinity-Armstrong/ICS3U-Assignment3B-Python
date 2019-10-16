#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: October 2019
# This is the greatest number program


def main():
    # This function runs the greatest number program

    # input
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))

    # process
    if first_number > second_number and first_number > third_number:
        print("")
        print("The greatest number is", first_number)
    elif second_number > first_number and second_number > third_number:
        print("")
        print("The greatest number is", second_number)
    elif third_number > first_number and third_number > second_number:
        print("")
        print("The greatest number is", third_number)


if __name__ == "__main__":
    main()

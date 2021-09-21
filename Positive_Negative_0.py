#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This is the Positive / Negative / 0" program


def main():
    # this function tells the user if the interger they input is + , - or 0

    # input
    user_number = int(input("Enter an integer: "))

    # process and output
    if user_number < 0:
        print("{0} is a negative number.".format(user_number))
    elif user_number > 0:
        print("{0} is a positive number.".format(user_number))
    elif user_number == 0:
        print("0 is just zero!")

    print("\nDone.")


if __name__ == "__main__":
    main()

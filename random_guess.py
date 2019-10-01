#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on September 2019
# This program lets user to guess a number and see if it's correct


import random

random = random.randint(1, 9+1)


def main():
    # this function lets user to guess a number and see if it's correct

    # input
    guess_number = int(input("Enter a number between 0 to 9: "))
    print("")

    # process
    if guess_number == random:
        # output
        print("correct, good guess ")
    else:
        print("wrong, better luck next time")


if __name__ == '__main__':
    main()

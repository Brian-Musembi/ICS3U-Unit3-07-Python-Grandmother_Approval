#!/usr/bin/env python3

# Created by Brian Musembi
# Created on May 2021
# This program determines if the grandmother will approve of the user
#     dating her grandchild

import constants


def main():
    # this function will determine if the user is in the needed age range

    print("This program determines if you can date Grandmother's grandchild")
    print("")

    # input
    user_age = input("Input your age as an integer: ")
    print("")

    # process
    try:
        user_age_int = int(user_age)

        if user_age_int > constants.MIN_AGE and \
           user_age_int < constants.MAX_AGE:
            # output
            print("Amazing! Grandmother approves of you"
                  " dating her grandchild.")

        elif user_age_int < constants.MIN_AGE:
            # output
            print("Sorry, you are too young!.")

        elif user_age_int > constants.MAX_AGE:
            # output
            print("Sorry, you are too old!")

    except Exception:
        # output
        print("That's not a number! Try again.")

    finally:
        # output
        print("")
        print("Good luck with your dating!")


if __name__ == "__main__":
    main()

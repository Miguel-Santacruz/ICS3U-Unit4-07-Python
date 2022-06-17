#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Jun 2022
# This program prints numbers from 1000 to 2000


def main():
    # this function prints every value from 1000 - 2000 in sets of five

    original_value = 999
    counter = 1

    while counter <= 1001:
        if counter % 5 == 0:
            print(original_value + counter)
        else:
            print(original_value + counter, end=" ")
        counter += 1

    print("\nDone.")


if __name__ == "__main__":
    main()

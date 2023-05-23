#!/usr/bin/env python
from time import sleep


def get_grade_input(grade_letter):
    value = input(f"Enter your number of {grade_letter} grades: ")
    return int(value) if value else 0


def main():
    a_value = int(5)
    b_value = int(3)
    print(f"""
        |  |  _ |  _  _   _   _   |_  _    |_ |_   _
        |/\| (- | (_ (_) ||| (-   |_ (_)   |_ | ) (-

         __                   __
        / _   _  _   _|  _   |__)  _      _      |_
        \__) |  (_| (_| (-   |    (_| \/ (_) |_| |_
                                      /
              __
             /    _  |  _     |  _  |_  _   _
             \__ (_| | (_ |_| | (_| |_ (_) |


              Each A/E is worth a base of ${a_value}
              Each B/S is worth a base of ${b_value}

Please enter the information as prompted to calculate your total payout!
    """)

    total_classes = int(input("Enter your total number of enrolled classes: "))

    number_a = get_grade_input('A/E')
    number_b = get_grade_input('B/S')
    number_c = get_grade_input('C')
    number_d = get_grade_input('D')
    number_f = get_grade_input('F')

    if number_a + number_b + number_c + number_d + number_f != total_classes:
        print(
            f"\nSorry, you do not have the correct number of grades for {total_classes} classes, fix your error and try again!")
        sleep(2)
        main()
    if number_f > 0:
        print(f"\nSorry, you do not qualify for payout with {number_f} F(s)")
        print(f"\nFailure doesn't pay!")
        exit()

    a_weight = float(5 * (number_a / total_classes))
    b_weight = float(3 * (number_b / total_classes))
    a_payout = round(a_weight * a_value)
    b_payout = round(b_weight * b_value)

    a_weight_trunc = round(a_weight, 2)

    if number_a >= 4:
        print(f"\nGreat job getting {number_a} A/E(s)!")
        print(f"\nYou earned a {a_weight_trunc} mulitplier!")
    elif number_a <= 3:
        print(f"You earned a {a_weight_trunc} mulitplier!")

    print(f"\nYou have earned ${a_payout} per A/E")
    print(f"\nYou have earned ${b_payout} per B/S")

    total_payout = (a_payout * number_a) + (b_payout * number_b)

    print(f"\nYour total payout is ${total_payout}")
    print(f"\nIf you aren't happy with this result, you should try harder next time!\n")
    if number_c >= 1:
        print(
            f"\nYou should also consider dropping {number_c} C(s) next quarter!")
    if number_d >= 1:
        print(
            f"\nYou should also consider dropping {number_d} D(s) next quarter!")

    print(f"\nThanks for using the grade payout calculator!")


if __name__ == "__main__":
    main()

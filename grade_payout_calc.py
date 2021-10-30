#!/usr/bin/env python

def menu():
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


              Each A is worth a base of ${a_value}
              Each B is worth a base of ${b_value}

Please enter the information as prompted to calculate your total payout!
    """)

    total_classes = int(input("Enter your total number of enrolled classes: "))

    number_a = int(input("Enter your number of A grades: "))
    number_b = int(input("Enter your number of B grades: "))
    number_c = int(input("Enter your number of C grades: "))
    number_d = int(input("Enter your number of D grades: "))
    number_f = int(input("Enter your number of F grades: "))

    if number_f > 0:
        print(f"\nSorry, you do not qualify for payout with {number_f} F(s)")
        exit()

    a_weight = float(5 * (number_a / total_classes))
    b_weight = float(5 * (number_b / total_classes))
    a_payout = round(a_weight * a_value)
    b_payout = round(b_weight * b_value)

    a_weight_trunc = round(a_weight, 2)

    if number_a >= 4:
        print(f"\nGreat job getting {number_a} A(s)!")
        print(f"\nYou earned a {a_weight_trunc} mulitplier!")

    print(f"\nYou have earned ${a_payout} per A")
    print(f"\nYou have earned ${b_payout} per B")

    total_payout = (a_payout * number_a) + (b_payout * number_b)
    print(f"\nYour total payout is ${total_payout}")


menu()

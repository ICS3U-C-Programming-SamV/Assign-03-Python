#!/usr/bin/env python3
# Created By: Sam V
# Date: Oct 13th, 2026
# A program that determines a food order
#  Ask the user for the size of the pizza you want to order (large, extra-large).
# You must have a minimum of 2 different sizes.
# Then ask the user for the number of toppings (1, 2, 3, 4).
# You can only ever complete 1 food order at a time.
# The program will then calculate  and display the subtotal, tax, and total of the order.


def main():
    # Constants for pizza prices and tax rate
    LARGE_PIZZA_PRICE = 10.00
    EXTRA_LARGE_PIZZA_PRICE = 15.00
    TOPPING_PRICE = 1.00
    TAX_RATE = 0.13

    user_size = input(
        "Good evening! What size of pizza would you like (large or extra large)? "
    )

    if user_size == "large":
        pizza_price = LARGE_PIZZA_PRICE
    elif user_size in ("extra large", "extra-large", "extra_large:"):
        pizza_price = EXTRA_LARGE_PIZZA_PRICE
    else:
        print("Please choose large or extra large.")
        return

    try:
        number_of_toppings = int(
            input(
                "What sort of toppings would you like? Pepperoni (1), Cheese (2), Sausages (3), or Ham and Pineapple! (4): "
            )
        )
    except ValueError:
        print("Please enter a whole number from 1 to 4.")
        return

    if number_of_toppings not in (1, 2, 3, 4):
        print("Please enter a number from 1 to 4.")
        return

    subtotal = pizza_price + number_of_toppings * TOPPING_PRICE
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()

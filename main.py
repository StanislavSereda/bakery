# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def main():
    menu = {
        'Кава': 25,
        'Чай': 15,
        'Пиріжок': 10,
        'Сендвіч': 20
    }

    order = {}

    while True:
        print("\nМеню:")
        for item, price in menu.items():
            print(f"{item}: {price} грн")

        print("\nВаше замовлення:")
        for item, quantity in order.items():
            print(f"{item}: {quantity}")

        item = input("\nВведіть назву товару або 'кінець', щоб завершити замовлення: ")
        if item.lower() == 'кінець':
            break

        if item in menu:
            quantity = int(input(f"Введіть кількість {item}: "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            price = float(input(f"Введіть ціну за одиницю {item}: "))
            quantity = int(input(f"Введіть кількість {item}: "))
            menu[item] = price
            order[item] = quantity

    total_cost = sum(menu[item] * order[item] for item in order)
    print("\nЗамовлення:")
    for item, quantity in order.items():
        print(f"{item}: {quantity} x {menu[item]} = {menu[item] * quantity} грн")

    print(f"\nЗагальна вартість: {total_cost} грн")


if __name__ == "__main__":
    main()

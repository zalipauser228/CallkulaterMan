def calculator():
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции: +, -, *, /")

    while True:
        try:
            num1 = float(input("Введите первое число: "))
            operation = input("Введите операцию (+, -, *, /): ")
            num2 = float(input("Введите второе число: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 / num2
            else:
                print("Неверная операция. Попробуйте снова.")
                continue

            print(f"Результат: {num1} {operation} {num2} = {result}")

        except ValueError:
            print("Ошибка: введите корректное число.")

        repeat = input("Хотите выполнить еще одну операцию? (да/нет): ").lower()
        if repeat != 'да':
            print("Спасибо за использование калькулятора!")
            break

if __name__ == "__main__":
    calculator()
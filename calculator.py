class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        """Add two numbers"""
        result = x + y
        self.history.append(f'{x} + {y} = {result}')
        return result

    def subtract(self, x, y):
        """Subtract y from x"""
        result = x - y
        self.history.append(f'{x} - {y} = {result}')
        return result

    def multiply(self, x, y):
        """Multiply two numbers"""
        result = x * y
        self.history.append(f'{x} × {y} = {result}')
        return result

    def divide(self, x, y):
        """Divide x by y"""
        if y == 0:
            raise ValueError('Cannot divide by zero')
        result = x / y
        self.history.append(f'{x} ÷ {y} = {result}')
        return result

    def power(self, x, y):
        """Calculate x raised to power y"""
        result = x ** y
        self.history.append(f'{x} ^ {y} = {result}')
        return result

    def square_root(self, x):
        """Calculate square root of x"""
        if x < 0:
            raise ValueError('Cannot calculate square root of negative number')
        result = x ** 0.5
        self.history.append(f'√{x} = {result}')
        return result

    def get_history(self):
        """Return calculation history"""
        return self.history

    def clear_history(self):
        """Clear calculation history"""
        self.history = []

def main():
    calc = Calculator()
    
    while True:
        print('\nPython Calculator')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Power')
        print('6. Square Root')
        print('7. View History')
        print('8. Clear History')
        print('9. Exit')

        choice = input('\nEnter choice (1-9): ')

        if choice == '9':
            print('Goodbye!')
            break

        if choice == '7':
            history = calc.get_history()
            if not history:
                print('No calculations in history')
            else:
                print('\nCalculation History:')
                for entry in history:
                    print(entry)
            continue

        if choice == '8':
            calc.clear_history()
            print('History cleared')
            continue

        try:
            if choice == '6':
                x = float(input('Enter number: '))
                result = calc.square_root(x)
            else:
                x = float(input('Enter first number: '))
                y = float(input('Enter second number: '))

                if choice == '1':
                    result = calc.add(x, y)
                elif choice == '2':
                    result = calc.subtract(x, y)
                elif choice == '3':
                    result = calc.multiply(x, y)
                elif choice == '4':
                    result = calc.divide(x, y)
                elif choice == '5':
                    result = calc.power(x, y)
                else:
                    print('Invalid choice')
                    continue

            print(f'Result: {result}')

        except ValueError as e:
            print(f'Error: {str(e)}')
        except Exception as e:
            print(f'An error occurred: {str(e)}')

if __name__ == '__main__':
    main()
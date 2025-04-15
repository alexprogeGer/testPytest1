class Calculator:

    def plus(self, a, b):

        return a + b

    def minus(self, a, b):
        return a - b

    def divide(self, a, b):
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError('тип данных у "a" или "b" не является int или float!')

            if b == 0:
                raise ZeroDivisionError('нельзя делить на ноль!')

            return a / b
        except TypeError as e:
            print(f"Type error: {e}")
            raise
        except ZeroDivisionError as e:
            print(f'ZeroDivisionError: {e}')
            raise

        except Exception as e:
            print(f'Непредвиденная ошибка: {e}')
            raise

    def multiply(self, a, b):
        return a * b








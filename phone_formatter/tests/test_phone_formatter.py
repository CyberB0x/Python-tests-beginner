import unittest
from formatter.phone_formatter import format_phone_number


class TestPhoneNumberFormatter(unittest.TestCase):
    def test_standard_format(self):
        print("\nТест: стандартный формат")
        input_num = "+49 152 1234567"
        expected = "+491521234567"
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertEqual(result, expected)

    def test_with_symbols(self):
        print("\nТест: символы (скобки и тире)")
        input_num = "+49 (152)-123-45-67"
        expected = "+491521234567"
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertEqual(result, expected)

    def test_with_multiple_spaces(self):
        print("\n Тест: множественные пробелы")
        input_num = "+49  152  123  4567"
        expected = "+491521234567"
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertEqual(result, expected)

    def test_extra_plus(self):
        print("\n Тест: лишние плюсы")
        input_num = "++49+1521234567"
        expected = "+491521234567"
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertEqual(result, expected)

    def test_without_plus(self):
        print("\n Тест: без плюса в начале")
        input_num = "491521234567"
        expected = "+491521234567"
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertEqual(result, expected)

    def test_empty_string(self):
        print("\n Тест: пустая строка")
        input_num = ""
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertIsNone(result)


    def test_only_symbols(self):
        print("\n Тест: только символы без цифр")
        input_num = "()-+= "
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertIsNone(result)

    def test_too_short_number(self):
        print("\n Тест: слишком короткий номер")
        input_num = "+49 123"
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertIsNone(result)

    def test_too_long_number(self):
        print("\n Тест: слишком длинный номер")
        input_num = "+49 123456789123456789123456"
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertIsNone(result)

    def test_exact_min_length(self):
        print("\nТест: ровно минимальная длина (10 цифр)")
        input_num = "+491234567890"
        expected = "+491234567890"
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertEqual(result, expected)

    def test_exact_max_length(self):
        print("\nТест: ровно максимальная длина (15 цифр)")
        input_num = "+491234567890123"
        expected = "+491234567890123"
        result = format_phone_number(input_num)
        print(f"Ввод: {input_num} -> Вывод: {result}")
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(TestPhoneNumberFormatter))



import unittest
from main import encoding


class MyTestCase(unittest.TestCase):
    def test_alphabet1(self):
        expected = "bcde"
        result = encoding(1, "abcd")
        print(result + "|" + expected)
        self.assertEqual(expected, result)

    def test_alphabet2(self):
        expected = "опзбдс"
        result = encoding(-1, "привет")
        print(result + "|" + expected)
        self.assertEqual(expected, result)

    def test_alphabet3(self):
        expected = "АрбуЗ"
        result = encoding(33, "АрбуЗ")
        print(result + "|" + expected)
        self.assertEqual(expected, result)

    def test_alphabet4(self):
        expected = "SpAm"
        result = encoding(2, "QnYk")
        print(result + "|" + expected)
        self.assertEqual(expected, result)

    def test_alphabet5(self):
        expected = "Кхзчх цхнжтхижщг и Ипспцлкпе,шихзхкфъе дфэпстхцлкпе, схщхчъе ухнлщ члкжсщпчхижщг сжнквр."
        result = encoding(7, "Добро пожаловать в Википедию,свободную энциклопедию, которую может редактировать каждый.")
        print(result + "|" + expected)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

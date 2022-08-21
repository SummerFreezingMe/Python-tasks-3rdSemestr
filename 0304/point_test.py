import unittest
import point as p

from main import max_square, file_input


class MyTestCase(unittest.TestCase):
    def test_square1(self):
        result = max_square(file_input("input.txt"))
        expected_result = [p.Point(-9.0, -9.0), p.Point(13.0, 0.0), p.Point(-1.0, 10.0)]
        for i in range(len(result)):
            print(result[i].__str__() + "|" + expected_result[i].__str__())
            self.assertEqual(result[i].__str__(), expected_result[i].__str__())  # add assertion here

    def test_square2(self):
        result = max_square(file_input("input2.txt"))
        expected_result = [p.Point(0.0, 2.0), p.Point(0.0, 0.0), p.Point(1.0, -1.0)]
        for i in range(len(result)):
            print(result[i].__str__() + "|" + expected_result[i].__str__())
            self.assertEqual(result[i].__str__(), expected_result[i].__str__())

    def test_square3(self):
        result = max_square(file_input("input3.txt"))
        expected_result = [p.Point(0.0, 2.0), p.Point(1.0, -1.0), p.Point(70.0, 70.0)]
        for i in range(len(result)):
            print(result[i].__str__() + "|" + expected_result[i].__str__())
            self.assertEqual(result[i].__str__(), expected_result[i].__str__())

    def test_square4(self):
        result = max_square(file_input("input4.txt"))
        expected_result = [p.Point(6.0, 6.0), p.Point(-4.0, 4.0), p.Point(0.0, 0.0)]
        for i in range(len(result)):
            print(result[i].__str__() + "|" + expected_result[i].__str__())
            self.assertEqual(result[i].__str__(), expected_result[i].__str__())

    def test_square5(self):
        result = max_square(file_input("input5.txt"))
        expected_result = [p.Point(33.0, 4.0), p.Point(-28.6, 66.5), p.Point(-19.0, 0.0)]
        for i in range(len(result)):
            print(result[i].__str__() + "|" + expected_result[i].__str__())
            self.assertEqual(result[i].__str__(), expected_result[i].__str__())


if __name__ == '__main__':
    unittest.main()

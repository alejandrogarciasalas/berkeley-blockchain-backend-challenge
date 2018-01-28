from balanced import isBalanced
import unittest

def run_check(text):
    lst = [s.strip() for s in text.splitlines()]
    data = ""
    for i in range(len(lst)):
        result = isBalanced(lst[i])
        if i != len(lst) - 1:
            data += result + '\n'
        else:
            data += result

    return data

class TestBalanced(unittest.TestCase):

    def test0(self):
        with open('inputs/input00.txt', 'r') as myfile:
            input_data = myfile.read()
        with open('outputs/output00.txt', 'r') as myfile:
            output_data = myfile.read().strip()

        self.assertEqual(run_check(input_data), output_data)

    def test1(self):
        with open('inputs/input01.txt', 'r') as myfile:
            input_data = myfile.read()
        with open('outputs/output01.txt', 'r') as myfile:
            output_data = myfile.read().strip()

        self.assertEqual(run_check(input_data), output_data)

    def test2(self):
        with open('inputs/input02.txt', 'r') as myfile:
            input_data = myfile.read()
        with open('outputs/output02.txt', 'r') as myfile:
            output_data = myfile.read().strip()

        self.assertEqual(run_check(input_data), output_data)

if __name__ == '__main__':
    unittest.main()

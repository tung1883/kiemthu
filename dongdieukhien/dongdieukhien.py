import unittest


def standard_blood_pressure(age):
    if age <= 0:
        return "Error: Minimum age is 1"
    if age > 65:
        return "Error: Maximum age is 65"
    if age <= 20:
        return 90 + int(age / 5)

    return 120 + int((age - 20) / 5)


class ControlFlowTesting(unittest.TestCase):
    def test_1(self):
        self.assertEqual(standard_blood_pressure(-1),
                         "Error: Minimum age is 1")

    def test_2(self):
        self.assertEqual(standard_blood_pressure(67),
                         "Error: Maximum age is 65")

    def test_3(self):
        self.assertEqual(standard_blood_pressure(15), 93)

    def test_4(self):
        self.assertEqual(standard_blood_pressure(21), 120)


if __name__ == '__main__':
    unittest.main()

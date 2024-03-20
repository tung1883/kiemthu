import unittest


def standard_blood_pressure(age):
    if age <= 0:
        return "Error: Minimum age is 1"
    if age > 65:
        return "Error: Maximum age is 65"
    if age <= 20:
        return 90 + int(age / 5)

    # age > 20
    return 120 + int((age - 20) / 5)


class BloddPressureBoundaryTesting(unittest.TestCase):
    def test_min(self):
        self.assertEqual(standard_blood_pressure(1), 90)

    def test_max(self):
        self.assertEqual(standard_blood_pressure(65), 129)

    def test_norm(self):
        self.assertEqual(standard_blood_pressure(32), 122)

    def test_inside_min(self):
        self.assertEqual(standard_blood_pressure(3), 90)

    def test_inside_max(self):
        self.assertEqual(standard_blood_pressure(63), 128)

    def test_outside_min(self):
        self.assertEqual(standard_blood_pressure(-1),
                         "Error: Minimum age is 1")

    def test_outside_max(self):
        self.assertEqual(standard_blood_pressure(67),
                         "Error: Maximum age is 65")


class BloddPressureDecisionTable(unittest.TestCase):
    def test_too_small_value(self):
        self.assertEqual(standard_blood_pressure(-5),
                         "Error: Minimum age is 1")

    def test_normal_value(self):
        self.assertEqual(standard_blood_pressure(30), 122)

    def test_too_big_value(self):
        self.assertEqual(standard_blood_pressure(67),
                         "Error: Maximum age is 65")


if __name__ == '__main__':
    unittest.main()

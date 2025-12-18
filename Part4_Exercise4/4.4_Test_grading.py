import unittest
from grading import grade_student

    # TODO:
    # - Write tests for typical values:
    #   * 95 -> "A"
    #   * 85 -> "B"
    #   * 75 -> "C"
    #   * 65 -> "D"
    #   * 30 -> "F"
    # - Write tests for boundary values:
    #   * 90 -> "A", 89 -> "B"
    #   * 80 -> "B", 79 -> "C"
    #   * 70 -> "C", 69 -> "D"
    #   * 60 -> "D", 59 -> "F"
    # - Write tests that check ValueError for:
    #   * score < 0
    #   * score > 100
    # - Use assertEqual for grades and assertRaises for invalid scores.
    #
    # write your tests here
class TestGradeStudent(unittest.TestCase):
    def test_grade_student(self):
        self.assertEqual(grade_student(95),"A")
        self.assertEqual(grade_student(85),"B")
        self.assertEqual(grade_student(75),"C")
        self.assertEqual(grade_student(65),"D")
        self.assertEqual(grade_student(30),"F")
        self.assertEqual(grade_student(90),"A")
        self.assertEqual(grade_student(89),"B")
        self.assertEqual(grade_student(80),"B")
        self.assertEqual(grade_student(79),"C")
        self.assertEqual(grade_student(70),"C")
        self.assertEqual(grade_student(69),"D")
        self.assertEqual(grade_student(60),"D")
        self.assertEqual(grade_student(59),"F")
        with self.assertRaises(ValueError):
            grade_student(-1)
            grade_student(101)

if __name__ == "__main__":
    unittest.main()

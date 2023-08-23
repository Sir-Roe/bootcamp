from lastloganwb import solution
from unittest import TestCase, main


class WhiteboardTest(TestCase):

    def test_a(self):
        self.assertTrue(solution(160, [20, 30, 110, 40, 50]))

    def test_b(self):
        self.assertFalse(solution(160, [80, 110, 40]))

    def test_c(self):
        self.assertFalse(solution(120,[60,70,20,40]))

    def test_d(self):
        self.assertTrue(solution(120,[60,60]))

    def test_e(self):
        self.assertTrue(solution(120,[40,55,15,80]))
if __name__ == '__main__':
    main()
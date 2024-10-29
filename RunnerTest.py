import logging
import unittest
from unittest import TestCase
from rt_with_exceptions import Runner

class RunnerTest(TestCase):
    def test_walk(self):
        try:
            logging.info(f'"test_walk" выполнен успешно', exc_info=True)
            test_w = Runner("Test walk", speed=-5)
            for i in range(10):
                test_w.walk()
            self.assertEqual(test_w.distance, 50)
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}", exc_info=True)

    def test_run(self):
        try:
            logging.info(f'"test_run" выполнен успешно', exc_info=True)
            test_r = Runner(10)
            for i in range(10):
                test_r.run()
            self.assertEqual(test_r.distance, 100)
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}", exc_info=True)

    def test_challenge(self):
        test_1 = Runner("runner1")
        test_2 = Runner("runner2")
        for i in range(10):
            test_1.walk()
            test_2.run()
        self.assertNotEqual(test_1.distance, test_2.distance)

if __name__ == '__main__':
    unittest.main()






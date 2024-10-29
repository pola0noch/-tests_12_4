# Домашнее задание по теме "Логирование"

import logging
import unittest
from rt_with_exceptions import Runner, Tournament
from RunnerTest import RunnerTest


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        filemode="w",
                        filename="runner_tests.log",
                        encoding="UTF-8",
                        format="%(asctime)s - %(levelname)s - %(message)s")

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

import unittest
import task


class TestNestedDict(unittest.TestCase):
    def test_pluck(self):
        d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
        self.assertEqual(task.pluck(d, 'a.b'), 5)
        self.assertEqual(task.pluck([], 'a.b'), None)
        self.assertEqual(task.pluck(d, 'a.b.c'), None)

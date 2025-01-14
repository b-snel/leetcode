from collections import deque
import unittest

class MovingAverage:

    def __init__(self, size: int):
      self.queue = deque()
      self.sum = 0
      self.size = size
      
    def next(self, val: int) -> float:
      if len(self.queue) == self.size:
        self.sum -= self.queue.popleft()
      self.sum += val
      self.queue.append(val)
      return self.sum / len(self.queue)

class TestMovingAverage(unittest.TestCase):
    def test_moving_average(self):
        # Initialize with window size 3
        moving_average = MovingAverage(3)
        
        # Test first value
        self.assertAlmostEqual(moving_average.next(1), 1.0)
        
        # Test second value
        self.assertAlmostEqual(moving_average.next(10), 5.5)
        
        # Test third value
        self.assertAlmostEqual(moving_average.next(3), 4.66667, places=5)
        
        # Test fourth value (window should start sliding)
        self.assertAlmostEqual(moving_average.next(5), 6.0)

if __name__ == '__main__':
    unittest.main()


# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
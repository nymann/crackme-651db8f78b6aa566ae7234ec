from math import isqrt
from random import randint
from random import shuffle


class SegmentGenerator:
    def __init__(self, segment_length: int) -> None:
        self._upper_limit = 360
        self.segment_length = segment_length

    def generate(self, min_sum: int) -> str:
        lowest_possible = sum(ord("A") for _ in range(self.segment_length))
        target_sum: int = self.next_prime(start=max(min_sum, lowest_possible))
        letter_avg = int(target_sum / self.segment_length)
        result: list[int] = [letter_avg for _ in range(self.segment_length)]
        initial_sum = sum(result)
        total_slack = target_sum - initial_sum
        for i in range(len(result))[:-1]:
            slack = randint(0, min(ord("Z") - result[i], total_slack))
            result[i] += slack
            total_slack -= slack
        result[-1] += total_slack
        shuffle(result)
        return "".join(chr(c) for c in result)

    def next_prime(self, start: int) -> int:
        for i in range(start, self._upper_limit):
            if self.is_prime(i):
                return i
        raise Exception("No primes found within limit")

    def is_prime(self, n: int) -> bool:
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = isqrt(n)
        for i in range(5, limit + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

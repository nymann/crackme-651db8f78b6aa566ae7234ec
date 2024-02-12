from crackme_651db8f78b6aa566ae7234ec.segment_generator import SegmentGenerator


class KeyGenerator:
    def __init__(self) -> None:
        self.segment_generator = SegmentGenerator(4)
        self.seen: set[str] = set()

    def generate(self) -> str:
        min_sum = 0
        result: list[str] = []
        for _ in range(4):
            segment = self.segment_generator.generate(min_sum + 1)
            result.append(segment)
            min_sum = sum(ord(c) for c in segment)
        res = "-".join(result)

        if res in self.seen:
            return self.generate()
        self.seen.add(res)
        return res

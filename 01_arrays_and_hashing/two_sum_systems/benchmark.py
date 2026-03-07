"""
Two Sum: Benchmark brute force O(n^2) vs hash map O(n)

Goal: See where Big-O theory meets reality.
- Hash maps have overhead: hashing, memory allocation, cache misses
- Brute force has great cache locality (sequential array access)
- There's a crossover point where the hash map starts winning

Run: python benchmark.py
"""

import random
import time
from typing import List


def two_sum_brute(nums: List[int], target: int) -> tuple:
    """O(n^2) nested loop — but cache-friendly sequential access."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return (-1, -1)


def two_sum_hashmap(nums: List[int], target: int) -> tuple:
    """O(n) single pass — but pays for hashing + dict overhead."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return (-1, -1)


def generate_test_case(n: int) -> tuple:
    """Generate an array of n random ints with a guaranteed solution at the end."""
    nums = [random.randint(-10_000, 10_000) for _ in range(n)]
    # Place the answer near the end so both algorithms do similar work
    nums[-2] = 99_999
    nums[-1] = 100_001
    target = 200_000
    return nums, target


def benchmark(func, nums, target, runs=5) -> float:
    """Return the median time in ms over multiple runs."""
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        func(nums, target)
        elapsed = (time.perf_counter() - start) * 1000
        times.append(elapsed)
    times.sort()
    return times[len(times) // 2]  # median


def main():
    sizes = [10, 100, 1_000, 10_000, 100_000]

    print(f"{'n':>10} | {'Brute (ms)':>12} | {'HashMap (ms)':>12} | {'Winner':>10} | {'Speedup':>8}")
    print("-" * 65)

    for n in sizes:
        nums, target = generate_test_case(n)

        # Skip brute force for very large n (would take minutes)
        if n <= 10_000:
            brute_ms = benchmark(two_sum_brute, nums, target, runs=3)
        else:
            brute_ms = float("inf")

        hash_ms = benchmark(two_sum_hashmap, nums, target, runs=5)

        if brute_ms == float("inf"):
            winner = "HashMap"
            speedup = "N/A"
        elif brute_ms < hash_ms:
            winner = "Brute"
            speedup = f"{hash_ms / brute_ms:.1f}x"
        else:
            winner = "HashMap"
            speedup = f"{brute_ms / hash_ms:.1f}x"

        brute_str = f"{brute_ms:.4f}" if brute_ms != float("inf") else "skipped"
        print(f"{n:>10} | {brute_str:>12} | {hash_ms:>12.4f} | {winner:>10} | {speedup:>8}")

    print()
    print("Key observations:")
    print("  - At small n, brute force can win due to lower overhead")
    print("  - Hash map overhead: hashing, dict resizing, pointer chasing (cache misses)")
    print("  - Brute force benefit: sequential memory access = CPU cache friendly")
    print("  - The crossover point is where Big-O starts to dominate constant factors")


if __name__ == "__main__":
    main()

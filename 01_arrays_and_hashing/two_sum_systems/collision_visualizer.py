"""
Hash Table Collision Visualizer

Goal: Make hash collisions visceral — see how different hash functions,
table sizes, and collision strategies affect distribution and clustering.

Run: python collision_visualizer.py

What to look for:
  - How load factor affects collision rate
  - Clustering patterns in open addressing vs even spread in chaining
  - How a bad hash function creates hotspots
"""

import random


# --- Hash Functions ---

def hash_modulo(key: int, table_size: int) -> int:
    """Simple modulo — the baseline. Works well when table_size is prime."""
    return key % table_size


def hash_multiply(key: int, table_size: int) -> int:
    """Knuth's multiplicative hash. Better distribution than plain modulo."""
    A = 0.6180339887  # (sqrt(5) - 1) / 2
    return int(table_size * ((key * A) % 1))


def hash_bad(key: int, table_size: int) -> int:
    """Intentionally bad: only uses last digit. Creates obvious hotspots."""
    return key % 10 % table_size


HASH_FUNCTIONS = {
    "modulo": hash_modulo,
    "multiplicative": hash_multiply,
    "bad (mod 10)": hash_bad,
}


# --- Collision Strategies ---

def insert_chaining(table: list, key: int, idx: int) -> int:
    """Chaining: append to the list at the index. Returns collision count."""
    collisions = len(table[idx])  # every existing item is a collision
    table[idx].append(key)
    return 1 if collisions > 0 else 0


def insert_open_addressing(table: list, key: int, idx: int, table_size: int) -> int:
    """Linear probing: find the next empty slot. Returns number of probes."""
    probes = 0
    while table[idx] is not None:
        probes += 1
        idx = (idx + 1) % table_size
    table[idx] = key
    return probes


# --- Visualization ---

def visualize_table(table: list, strategy: str, table_size: int) -> None:
    """Print the hash table as a horizontal bar chart."""
    max_width = 60

    if strategy == "chaining":
        max_count = max(len(bucket) for bucket in table)
        for i, bucket in enumerate(table):
            count = len(bucket)
            bar_len = int((count / max(max_count, 1)) * max_width)
            bar = "#" * bar_len
            label = f"  ({count})" if count > 0 else ""
            print(f"  [{i:>3}] {bar}{label}")
    else:
        for i, slot in enumerate(table):
            marker = "#" if slot is not None else "."
            print(f"  [{i:>3}] {marker}", end="")
            if (i + 1) % 20 == 0 or i == table_size - 1:
                print()


def run_experiment(keys: list, table_size: int, hash_name: str, hash_func, strategy: str) -> None:
    """Run one experiment and print results."""
    n = len(keys)
    load_factor = n / table_size

    print(f"\n{'=' * 70}")
    print(f"  Hash: {hash_name} | Strategy: {strategy} | "
          f"Table size: {table_size} | Keys: {n} | Load factor: {load_factor:.2f}")
    print(f"{'=' * 70}")

    total_collisions = 0

    if strategy == "chaining":
        table = [[] for _ in range(table_size)]
        for key in keys:
            idx = hash_func(key, table_size)
            total_collisions += insert_chaining(table, key, idx)
    else:
        table = [None] * table_size
        for key in keys:
            idx = hash_func(key, table_size)
            total_collisions += insert_open_addressing(table, key, idx, table_size)

    visualize_table(table, strategy, table_size)

    collision_rate = total_collisions / n * 100
    print(f"\n  Collisions: {total_collisions}/{n} ({collision_rate:.1f}%)")

    if strategy == "chaining":
        lengths = [len(b) for b in table]
        max_chain = max(lengths)
        empty = lengths.count(0)
        print(f"  Longest chain: {max_chain} | Empty slots: {empty}/{table_size}")


def main():
    random.seed(42)
    keys = [random.randint(0, 10_000) for _ in range(50)]

    print("HASH TABLE COLLISION VISUALIZER")
    print("Each '#' represents an occupied slot or chain length.")
    print("Watch how distribution changes with different hash functions and strategies.")

    # Experiment 1: Compare hash functions with chaining
    print("\n\n>>> PART 1: Comparing hash functions (chaining, table_size=16)")
    for name, func in HASH_FUNCTIONS.items():
        run_experiment(keys, table_size=16, hash_name=name, hash_func=func, strategy="chaining")

    # Experiment 2: Chaining vs open addressing
    print("\n\n>>> PART 2: Chaining vs Open Addressing (modulo hash, table_size=64)")
    run_experiment(keys, table_size=64, hash_name="modulo", hash_func=hash_modulo, strategy="chaining")
    run_experiment(keys, table_size=64, hash_name="modulo", hash_func=hash_modulo, strategy="open_addressing")

    # Experiment 3: Load factor impact
    print("\n\n>>> PART 3: Load factor impact (modulo hash, chaining)")
    for table_size in [100, 50, 20, 10]:
        run_experiment(keys, table_size=table_size, hash_name="modulo", hash_func=hash_modulo, strategy="chaining")

    print("\n\nKey takeaways:")
    print("  - Bad hash functions create hotspots regardless of table size")
    print("  - Open addressing shows clustering — collisions cause more collisions")
    print("  - Higher load factor = more collisions = slower lookups")
    print("  - This is why real hash maps resize (typically at load factor 0.75)")
    print("  - 'O(1) lookup' assumes good hash function + low load factor")


if __name__ == "__main__":
    main()

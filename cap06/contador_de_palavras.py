from collections import Counter
from re import split

BANNER = "-" * 35


def format_print(counter, is_reverse=False):
    lst = counter.items()
    print("[Unique Words: %d]" % len(lst))
    print("%-16s | %16s" % ("Word", "Count"))
    print(BANNER)
    for word, count in lst:
        print("%-16s | %16d" % (word, count))


def count_words(filename):
    counter = Counter()
    with open(filename, "rU") as f:
        for line in f:
            line = line.strip().lower()
            if not line:
                continue
            counter.update(x for x in split("[^a-zA-Z']+", line) if x)
    return counter


format_print(count_words("sarcozy.txt"), is_reverse=False)
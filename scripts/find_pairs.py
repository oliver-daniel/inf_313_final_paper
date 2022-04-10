#### Preamble ####
# Purpose: Given a series of filenames corresponding to TXT-based corpora of words,
# with one word on each line, filter out all invalid words (here anything other than 5+
# lowercase letters), then find all pairs of valid words that create Split Decisions,
# i.e., pairs of equal length which differ by exactly two consecutive characters.
# Authors: Oliver Daniel
# Date: TODO
# Contact: via Quercus or email
# License: WTFPL
# Prerequisites:
# - Python 3.9.x

import sys
from pathlib import Path
import csv
import itertools as it
import re

pattern = re.compile(r'[a-z]{5,}')
in_dir = Path(__file__).parent.parent / 'in'

def get_wordlist(corpus):
    with open(in_dir / 'corpus' / f'{corpus}.txt', 'r') as f:
        treated = (ln.strip() for ln in f)
        return [ln for ln in treated if re.fullmatch(pattern, ln)]

def matching_pairs(wordlist):
    for x, y in it.combinations(wordlist, r=2):
        if len(x) != len(y): continue

        differences = [i for i, (a, b) in enumerate(zip(x, y)) if a != b]

        if len(differences) == 2:
            start, end = differences
            if end != start + 1: continue

            yield {
                'length': len(x),
                'x': x,
                'y': y,
                'start': start + 1,
                'end': end + 1,
                'split_x': x[start:end + 1],
                'split_y': y[start:end + 1]
            }

def batch_write_to_file(corpus, BATCH_SIZE = 1000): 
    fieldnames = ['length', 'x', 'y', 'start', 'end', 'split_x', 'split_y']
    wordlist = get_wordlist(corpus)

    with open(in_dir / 'cache' / f'{corpus}.csv', 'w+') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        batch = []

        writer.writeheader()

        for i, row in enumerate(matching_pairs(wordlist)):
            if i % BATCH_SIZE == 0:
                print(i, row['x'][0])
                writer.writerows(batch)
                batch.clear()
            batch.append(row)

        # last batch
        writer.writerows(batch)
        print('Total:', i)

if __name__ == '__main__':
    corpora = sys.argv[1:]
    
    for corpus in corpora:
        print(f"Now creating word pairs for corpus {corpus}...")

        try:
            batch_write_to_file(corpus)
        except FileNotFoundError:
            raise
"""
test_file.py
production ready text file analyzer providing 
 -Total word count 
 -Most common words (top N, case insensitive, punctuation ignored)
Author : ceaser 
"""
import re
from collections import Counter 
from pathlib import Path
from typing import Iterator, Dict, List, Tuple
WORD_RE = re.compile(r"\b[\w']+\b")
def tokenize(text: str) -> List[str]:
    """
    convert raw text to lowercase alphanumeric tokens 
    keep apostrophes inside words(eg., "don't")
    """
    return WORD_RE.findall(text.lower())
def stream_tokens(path: Path) -> Iterator[str]:
    """
    Memory efficient generator yielding tokens line by line 
    suitable for large files
    """
    with path.open('r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            yield from tokenize(line)
def analyze(path:Path, top_n: int= 10) -> Tuple[int, List[Tuple[str, int]]]:
    """
    analyze text file and return:
      - total word count 
      - top_n most common words with frequencies 
    """  
    counter= Counter()
    total= 0
    for token in stream_tokens(path):
        counter[token] += 1
        total += 1
    most_common = counter.most_common(top_n)
    return total, most_common

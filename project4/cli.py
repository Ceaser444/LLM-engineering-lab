""" command line interface for the text analyzer """
from typing import List
import argparse
import sys
from pathlib import Path
from text_analyzer import analyze
def main(argv:List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description = "Analyze a text file: word count and most common word."
    )
    parser.add_argument("file", type=Path , help= "Path to text file")
    parser.add_argument(
        "-n",
        "--top",
        type=int,
        default = 10,
        help="Number of top words to display (default=10)"
    )
    args= parser.parse_args(argv)
    if not args.file.is_file():
        print(f"Error: '{args.file}' does not exist or is not a file", file=sys.stderr)
        sys.exit(1)
    total, common = analyze(args.file, top_n = args.top)
    print(f"Total words: {total:,}")
    print("\nMost common words:")
    for rank, (word,freq) in enumerate(common, 1):
        print(f"{rank:2}. {word:<15} {freq}")   
if __name__ == "__main__":
    sys.argv = ['cli.py', 'text.txt']
    main()      

#!/usr/bin/python3
import sys

def print_range(a, b):
    """
    Prints numbers from a to b inclusive.
    Handles cases where a is greater than b.
    """
    if a > b:
        # Step backward if a is greater than b
        for i in range(a, b - 1, -1):
            print(i, end=" " if i != b else "")
    else:
        # Step forward if a is less than or equal to b
        for i in range(a, b + 1):
            print(i, end=" " if i != b else "")
    print()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./main.py <start> <end>")
        sys.exit(1)
    
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    print_range(start, end)

#!/usr/bin/python3

"""
Script that markdown html using python
"""

import sys
import os
import markdown

# Checks for number of arguments
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    # Checks if input file exists
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read Markdown file and convert to HTML
    with open(input_file, "r") as f:
        text = f.read()
    html = markdown.markdown(text)

    # Write HTML to output file
    output_file = sys.argv[2]
    with open(output_file, "w") as f:
        f.write(html)

    # Exit with success
    sys.exit(0)

#!/usr/bin/env python3
#
# pylint: disable=missing-docstring,trailing-whitespace,invalid-name

import re
import sys
import argparse
import requests

# This magic spell lets me erase the current line.
# I can use this to show for example "Downloading..."
# and then "Downloaded" on the line where
# "Downloading..." was.
ERASE_LINE = '\x1b[2K'

def main():
    parser = argparse.ArgumentParser(description="Download videos from facebook from your terminal")

    parser.add_argument('url', action="store")
    parser.add_argument('resolution', action="store", nargs="?")

    args = parser.parse_args()

    print("Fetching source code...", end="\r", flush=True)
    request = requests.get(args.url)
    sys.stdout.write(ERASE_LINE)
    
    print(f"\033[92m✔\033[0m Fetched source code")

    print("Downloading video...", end="\r", flush=True)

    file_name = str(re.findall(r"videos\/(.+?)\"", request.text)[-1].replace("/", "")) + f"_{'sd_src' if args.resolution == 'sd' else 'hd_src'}.mp4"

    try:
        request = requests.get(re.findall(f"{'sd_src' if args.resolution == 'sd' else 'hd_src'}:\"(.+?)\"", request.text)[0])
    except IndexError:
        sys.stdout.write(ERASE_LINE)
        print("\033[91m✘\033[0m Video could not be downloaded")
        sys.exit()

    # Write the content to the file
    with open(file_name, "wb") as f:
        f.write(request.content)

    sys.stdout.write(ERASE_LINE)
    print(f"\033[92m✔\033[0m Video downloaded: {file_name}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import re
import sys
import random
import argparse
import requests

good = "\033[92m✔\033[0m"

# This magic spell lets me erase the current line.
# I can use this to show for example "Downloading..."
# and then "Downloaded" on the line where
# "Downloading..." was.
ERASE_LINE = '\x1b[2K'

# This extracts the video url
def extract_url(html, quality):
    """
    html       -    the html code of the webpage where the video is located
    quality    -    the quality of the video that should be downloaded (SD or HD)
    """

    # Here we are using an if-then-else onliner statement.
    # It might look a little confusing at first, but it makes a lot of sense
    # once you get an understanding of it.
    # Read this if you are a little confused: https://stackoverflow.com/a/2802748/9215267
    return re.findall(f"{'sd_src' if quality == 'sd' else 'hd_src'}:\"(.+?)\"", html)[0]


def main():
    """
    This function takes no arguments.
    """
    parser = argparse.ArgumentParser(description="Download videos from facebook from your terminal")

    parser.add_argument('url', action="store")
    parser.add_argument('resolution', action="store", nargs="?")

    args = parser.parse_args()

    print("Fetching source code...", end="\r", flush=True)
    request = requests.get(args.url)
    sys.stdout.write(ERASE_LINE)
    print(good, "Fetched source code")

    file_url = extract_url(request.text, args.resolution)

    # Generates a random number with will be the file name
    path = f"{str(random.random())[3:12]}.mp4"
    print("Downloading video...", end="\r", flush=True)
    # Downloads the video
    request = requests.get(file_url)
    
    with open(path, "wb") as f:
        f.write(request.content)

    sys.stdout.write(ERASE_LINE)
    print(f"{good} Video downloaded: {path}")

if __name__ == "__main__":
    main()

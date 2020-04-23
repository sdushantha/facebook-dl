#!/usr/bin/env python3
#
# pylint: disable=missing-docstring,trailing-whitespace,invalid-name
#
# By Siddharth Dushantha (sdushantha) 2020
#
# Notice: If you are on Windows, the output of this script might
#         look a little messy and that is because command prompt
#         does not support escape sequences.
#

import re
import sys
import argparse
import requests

# This magic spell lets me erase the current line.
# I can use this to show for example "Downloading..."
# and then "Downloaded" on the line where
# "Downloading..." was.
ERASE_LINE = '\e[2K'

def main():
    parser = argparse.ArgumentParser(description="Download videos from facebook from your terminal")

    parser.add_argument('url', action="store")
    parser.add_argument('resolution', action="store", nargs="?")

    args = parser.parse_args()

    print("Fetching source code...", end="\r", flush=True)
    request = requests.get(args.url)
    print(ERASE_LINE, end="\r", flush=True)
    
    print("\e[92m✔\e[0m Fetched source code")

    # Create the file name by extracting the video ID from html and then add
    # "hd" or "sd" depending on the quality of the resolution that is being downloaded.
    #
    # To decide whether to use "hd or "sd" we are using an if-then-else
    # one-liner statement. It might look a little confusing at first, but it
    # makes a lot of sense once you get an understanding of it.
    # Read this if you are a little confused: https://stackoverflow.com/a/2802748/9215267
    file_name = str(re.findall(r"videos\/(.+?)\"", request.text)[-1].replace("/", "")) + f"_{'sd' if args.resolution == 'sd' else 'hd'}.mp4"
    
    print("Downloading video...", end="\r", flush=True)

    try:
        request = requests.get(re.findall(f"{'sd_src' if args.resolution == 'sd' else 'hd_src'}:\"(.+?)\"", request.text)[0])
    except IndexError:
        print(ERASE_LINE, end="\r", flush=True)
        print("\e[91m✘\e[0m Video could not be downloaded")
        sys.exit()

    # Write the content to the file
    with open(file_name, "wb") as f:
        f.write(request.content)

    print(ERASE_LINE, end="\r", flush=True)

    # You might be wondering why in this line the ansi code starts with
    # \033, but all other ones starts with \e.
    # This is because \e for some bizzar reason does not work with f-strings.
    # I did try doing a quick Google search, but did not find anything so thats
    # why I am equally confused as you are to why \e wont work.
    # If you would like to learn more about \033 and \e take look at
    # this link: https://unix.stackexchange.com/a/89817/342070
    print(f"\033[92m✔\033[0m Video downloaded: {file_name}")

if __name__ == "__main__":
    main()

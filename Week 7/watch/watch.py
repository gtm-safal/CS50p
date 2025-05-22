import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

    #<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    match = re.search(r'^(?:<iframe )(?:.+)?src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s)
    if match:

        return "https://youtu.be/"+match.group(1)
    else:
        return None


if __name__ == "__main__":
    main()

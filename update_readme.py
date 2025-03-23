import json
import random
from datetime import datetime

README_PATH = "README.md"
QUOTE_PATH = "quotes.json"
SECTION_HEADER = "<!-- daily-quote -->"


def pick_quote():
    with open(QUOTE_PATH, "r") as f:
        quotes = json.load(f)
    return random.choice(quotes)


def update_readme():
    quote = pick_quote()
    # timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    with open(README_PATH, "r") as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        if line.strip() == SECTION_HEADER:
            # Skip the next line (old quote), replace with new one
            i += 1
            if i < len(lines) and lines[i].strip().startswith("📌"):
                i += 1  # skip the old quote line
            new_lines.append(f"📌 *{quote}*\n")
        else:
            i += 1

    with open(README_PATH, "w") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    update_readme()

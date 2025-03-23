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
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    with open(README_PATH, "r") as f:
        lines = f.readlines()

    new_lines = []
    replaced = False

    for line in lines:
        if SECTION_HEADER in line:
            new_line = f"{SECTION_HEADER}\n📌 *{quote}* — updated {timestamp}\n"
            new_lines.append(new_line)
            replaced = True
        else:
            new_lines.append(line)

    if not replaced:
        new_lines.append(f"\n{SECTION_HEADER}\n📌 *{quote}* — updated {timestamp}\n")

    with open(README_PATH, "w") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    update_readme()

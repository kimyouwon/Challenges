import os

FLAG_PATH = "/flag.txt"

try:
    with open(FLAG_PATH, "r") as f:
        FLAG = f.read().strip()
except:
    FLAG = "GH{this is real flag?}"

mid = len(FLAG) // 2
HASH = FLAG[:mid]
BROWN = FLAG[mid:]

def hashbrown():
    return HASH, BROWN
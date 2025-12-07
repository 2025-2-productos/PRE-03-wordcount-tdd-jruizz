def split_into_words(lines):
    words = []
    for line in lines:
        words.extend(line.strip(",.!?") for line in line.split())
    return words

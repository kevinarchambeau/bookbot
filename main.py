def main():
    path = "books/frankenstein.txt"
    file_contents = read_file(path)
    wordCount = word_count(file_contents)
    letterDict = number_of_letters(file_contents)
    print_report(path, wordCount, letterDict)


def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_count(stringToCount):
    words = stringToCount.split()
    return len(words)

def number_of_letters(stringToCount):
    letters = {}
    
    for letter in stringToCount:
        lowerCase = letter.lower()
        if lowerCase not in letters:
            letters[lowerCase] = 1
        else:
            letters[lowerCase] += 1

    return letters

def print_report(file, word_count, letterDict):
    print(f"Word and letter report for: {file}")
    print(f"{word_count} word(s) in document")

    letterKeyList = list(letterDict.keys())
    letterKeyList.sort()
    for key in letterKeyList:
        if key.isalpha():
            print(f"The '{key}' character was found {letterDict[key]} times")


main()
def main():
    with open('books/frankenstein.txt') as file:
        file_content = file.read()
    # print(file_content)
    dict = character_count(file_content)
    report(file_content, dict)

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowered_text = text.lower()
    char = {}
    for character in lowered_text:
        if character.isalpha():
            if character in char:
                char[character] += 1
            else:
                char[character] = 1
    return char
    # for key in char:
    #     print(key, ':', char[key])

def report(file, dict):
    print('---- Begin report of books/frankenstein.txt ----')
    print(str(word_count(file))+' words found in the document\n')
    for char, occurences in dict.items():
        print(f"The '{char}' character was found {occurences} times")
    print('\n---- End report ---- \n')

main()
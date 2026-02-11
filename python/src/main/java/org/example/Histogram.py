from operator import itemgetter
def generate_character_histogram(word):
    char_count_map = {}

    for current_char in list(word.lower()):
        if current_char.isalpha():
            if current_char in char_count_map:
                char_count_map[current_char]+=1
            else:
                char_count_map[current_char]=1
    return dict(sorted(char_count_map.items(),key=itemgetter(0)))

print(generate_character_histogram('Otto'))
print(generate_character_histogram("Hello Micha"))
print(generate_character_histogram("Python challenges, Your Python Training"))
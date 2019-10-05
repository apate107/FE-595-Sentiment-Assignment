import operator
from textblob import TextBlob


def get_characteristics(character):
    """Extracts the adjectives (descriptors) of a given character"""
    # Use TextBlob to find the adjectives that precede the first noun
    blob = TextBlob(character)
    tags = blob.tags
    noun_index = [i for i, tag in enumerate(tags) if tag[1] == 'NN']
    if noun_index:
        return [tag[0] for tag in list(filter(lambda x: x[1] == 'JJ', tags[0:noun_index[0]]))]

    # If the sentence wasn't in the expected form, just take the two adjectives after "He's/She's a(n)"
    return list(TextBlob(character).tokens[3:5])


def main():
    """Runs through all characters and generates count of most common descriptors"""
    # Import all characters
    characters = open("output\\male_all.txt", "r").read().splitlines()
    characters += open("output\\female_all.txt", "r").read().splitlines()

    characteristic_count = {}
    for character in characters:
        characteristics = get_characteristics(character)
        for tag in characteristics:
            if tag in characteristic_count:
                characteristic_count[tag] += 1
            else:
                characteristic_count[tag] = 1

    # Write out top 10 characteristics to file
    open("output\\common_tags.txt", "w+").writelines([tag + ': ' + str(count) + '\n' for tag, count in
                                                      sorted(characteristic_count.items(),
                                                             key=operator.itemgetter(1),
                                                             reverse=True)[0:10]])

    return 0


if __name__ == '__main__':
    main()
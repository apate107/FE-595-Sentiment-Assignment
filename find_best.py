from textblob import TextBlob


def main():
    best_male, best_female = '', ''

    males = open("male_all.txt", "r").read().splitlines()
    females = open("female_all.txt", "r").read().splitlines()

    # Get male sentiment
    male_scores = [TextBlob(character).sentiment.polarity for character in males]
    best_male = males[male_scores.index(max(male_scores))]

    # Get female sentiment
    female_scores = [TextBlob(character).sentiment.polarity for character in females]
    best_female = females[female_scores.index(max(female_scores))]

    # Print out best characters
    print(best_male + ' ' + best_female + ' They fight crime!')


if __name__ == '__main__':
    main()

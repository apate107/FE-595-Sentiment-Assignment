from textblob import TextBlob


def find_n_extreme(characters, n, best):
    return sorted(characters, key=lambda x: TextBlob(x).sentiment.polarity, reverse=best)[0:n]


def main():
    males = open("output\\male_all.txt", "r").read().splitlines()
    females = open("output\\female_all.txt", "r").read().splitlines()

    # Create story of best characters
    print('Story of best characters:')
    print(find_n_extreme(males, 1, True)[0] + ' ' + find_n_extreme(females, 1, True)[0] + ' They fight crime!')

    # Now write to files top 10 best/worst male/female characters
    open("output\\top_female.txt", "w+").writelines('\n'.join(find_n_extreme(females, 10, best=True)))

    open("output\\top_male.txt", "w+").writelines('\n'.join(find_n_extreme(males, 10, best=True)))

    open("output\\bottom_female.txt", "w+").writelines('\n'.join(find_n_extreme(females, 10, best=False)))

    open("output\\bottom_male.txt", "w+").writelines('\n'.join(find_n_extreme(males, 10, best=False)))

    return 0


if __name__ == '__main__':
    main()

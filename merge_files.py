import os


def read_file(fname, start):
    lines = []
    with open(fname, "r") as f:
        lines = f.read().splitlines()
    f.close()

    # Format and do a couple of checks on the lines because there are some lines that include the next sentence in it
    result = []
    for line in lines:
        if line == '' or line.find(start) == -1:
            continue
        line = line[line.find(start):]  # Some files had numbers beginning at each line
        if start == "He's" and line.find("She's") >= 0:
            line = line[0:line.find("She's")]
        elif start == "She's" and line.find("They") >= 0:
            line = line[0:line.find("They")]
        result.append(line + '\n')

    return result


def main():
    # First import all data and write to a master file
    with open("male_all.txt", "w+") as m, open("female_all.txt", "w+") as f:
        for fname in os.listdir(os.getcwd() + '\\data'):
            # Since male/he are within the words female/she, check for a female file otherwise default to male file
            if fname.lower().find("female") >= 0 or fname.lower().find("she") >= 0:
                f.writelines(read_file(os.getcwd() + '\\data\\' + fname, "She's"))
            else:
                m.writelines(read_file(os.getcwd() + '\\data\\' + fname, "He's"))
    m.close()
    f.close()


if __name__ == '__main__':
    main()

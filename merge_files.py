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
        line = line[line.find(start):].strip()  # Some files had numbers beginning at each line
        if start == "He's" and line.find("She's") >= 0:
            line = line[0:line.find("She's")]
        elif start == "She's" and line.find("They") >= 0:
            line = line[0:line.find("They")]
        if line[-1] != '.' and line[-2] != '.':
            line += '.'
        result.append(line + '\n')

    return result


def main():
    # First import all data and write to a master file
    with open("output\\male_all.txt", "w+") as m, open("output\\female_all.txt", "w+") as f:
        for fname in os.listdir(os.getcwd() + '\\data'):
            # Since male/he are within the words female/she, check for a female file otherwise default to male file
            if fname.lower().find("female") >= 0 or fname.lower().find("she") >= 0:
                f.writelines(read_file('data\\' + fname, "She's"))
            else:
                m.writelines(read_file('data\\' + fname, "He's"))
    m.close()
    f.close()

    return 0


if __name__ == '__main__':
    main()
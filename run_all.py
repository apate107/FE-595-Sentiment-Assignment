import merge_files, sort_characters, most_common
import argparse
import webbrowser
import sys, os

def main(args):
    merge_files.main()
    sort_characters.main()
    most_common.main()

    parser = argparse.ArgumentParser(description = "Run \'They Fight Crime\' sentiment anlaysis.")
    parser.add_argument('-o', action='store_true', default=False, help='Open all resultant files after running?')
    args = parser.parse_args(args)

    if args.o:  # Open all files
        for fname in os.listdir(os.getcwd() + '\\output'):
            webbrowser.open('output\\' + fname)

    return 0

if __name__ == '__main__':
    main(sys.argv[1:])

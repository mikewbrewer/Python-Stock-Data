from extract_data import extract_data
from plot_data import plot_data
from sys import argv



def main(_argv):
    extract_data(_argv)
    plot_data(_argv)


if __name__ == '__main__':
    main(argv)

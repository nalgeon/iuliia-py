import sys
import iuliia


def main():
    if len(sys.argv) < 2:
        print("usage: iuliia SOURCE")
        exit(1)
    source = sys.argv[1]
    result = iuliia.translate(source, scheme=None)
    print(result)


if __name__ == "__main__":
    main()

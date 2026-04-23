import sys
from dl.core import handle_command

def main():
    args = sys.argv[1:]

    if not args:
        print("Use: dl --help")
        return

    handle_command(args)

if __name__ == "__main__":
    main()
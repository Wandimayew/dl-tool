import sys
from dl.core import handle_command

def main():
    args = sys.argv[1:]

    if not args:
        print("DL Tool - use --help")
        return

    try:
        handle_command(args)
    except KeyboardInterrupt:
        print("\n❌ Cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
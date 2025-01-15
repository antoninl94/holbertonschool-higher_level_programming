#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argCount = len(sys.argv) - 1
    if len(sys.argv) == 1:
        print(f"{argCount} arguments.")
    elif len(sys.argv) == 2:
        print(f"{argCount} argument:")
        for i, arg in enumerate(sys.argv[1:], start = 1):
            print(f"{i}: {arg}")
    else:
        print(f"{argCount} arguments:")
        for i, arg in enumerate(sys.argv[1:], start = 1):
            print(f"{i}: {arg}")

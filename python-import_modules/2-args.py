#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argCount = len(sys.argv) - 1
    if len(sys.argv) == 1:
        print(f"{argCount} arguments.")
    else:
        print(f"{argCount} arguments:")
    for i, arg in enumerate(sys.argv[1:]):
        i += 1
        print(f"{i}: {arg}")

def is_valid(s: str) -> bool:
    stack = []
    valid_symbols = ["(", ")", "{", "}", "[", "]"]
    symbol_map = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char not in valid_symbols:
            continue
        if char in symbol_map.values():
            stack.append(char)
        elif char in symbol_map.keys():
            if not stack or stack[-1] != symbol_map[char]:
                return False
            stack.pop()

    return len(stack) == 0


def main():
    string = input("Enter a string: ")
    is_string_valid = is_valid(string)
    if is_string_valid:
        print("The string is valid.")
    else:
        print("The string is invalid.")


if __name__ == "__main__":
    main()

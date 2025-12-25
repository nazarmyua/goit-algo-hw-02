from collections import deque


def is_palindrome(phrase: str) -> bool:
    phrase_deque = deque(phrase)

    while len(phrase_deque) > 1:
        if phrase_deque.popleft() != phrase_deque.pop():
            return False
    return True


def run():
    phrase = input("Enter phrase: ")
    if is_palindrome(phrase):
        print("The phrase is a palindrome.")
    else:
        print("The phrase is not a palindrome.")


def main():
    run()


if __name__ == "__main__":
    main()

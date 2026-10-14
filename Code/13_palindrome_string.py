
def is_palindrome(text):
    text = text.lower()
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return text == reversed_text


print(is_palindrome("madam"))

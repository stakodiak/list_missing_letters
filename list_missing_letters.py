"""
Lists letters missing from attempted pangrams.
"""


def listMissingLetters(s):
    """
    Returns a string with all the letters of the English alphabet,
    alphabetically that are not in the input string. This function
    is case-insenstive.

    @param s: A string to be analyzed.
    @return: A string alphabetically listing all the letters missing
             from the input string.
    """
    a = ord("a")
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    # Every letter in the input string is removed from our list
    # of the entire alphabet.
    for letter in s:
        letter_index = ord(letter.lower()) - a
        # Non-letters are ignored
        if letter_index >= 0 and letter_index < 26:
            alphabet[letter_index] = ""

    #The remaining letters are returned as a single string.
    return "".join(alphabet)

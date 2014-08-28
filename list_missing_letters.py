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
    import string
    return filter(lambda c: c not in s.lower(),
                  string.ascii_lowercase)

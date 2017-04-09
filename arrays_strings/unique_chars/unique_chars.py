class UniqueChars(object):

    def has_unique_chars(self, text):

        if text is None:
            return False

        return len(set(text)) == len(text)

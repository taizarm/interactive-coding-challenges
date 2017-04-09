class UniqueChars(object):

    def has_unique_chars(self, text):

        if text is None:
            return False

        chars = []
        for char in text:
            if char in chars:
                return False
            chars.append(char)

        return True

class Permutations(object):

    def get_letters_dict(self, str):
        letters = {}

        for i in str:
            letters[i] = letters.get(i, 0) + 1

        return letters

    def is_permutation(self, str1, str2):

        if all([str1, str2]):

            dict1 = self.get_letters_dict(str1)
            dict2 = self.get_letters_dict(str2)

            return dict1 == dict2

        return False

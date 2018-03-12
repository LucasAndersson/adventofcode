def is_valid_passphrase(passphrase):
    words = passphrase.split(' ')

    for word1 in words:
        if words.count(word1) > 1:
            return False

        chars1 = list(word1)

        for word2 in words:
            if word1 == word2:
                continue

            chars2 = list(word2)
            chars1.sort()
            chars2.sort()

            if chars1 == chars2:
                return False

    return True


def count_valid_passphrases(file_name):
    with open(file_name) as file:
        passphrases = file.readlines()
        counter = 0

        for passphrase in passphrases:
            if is_valid_passphrase(passphrase.rstrip('\n')):
                counter += 1

    return counter

print(count_valid_passphrases("day4.txt"))

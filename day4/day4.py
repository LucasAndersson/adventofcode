def is_valid_passphrase(passphrase):
    words = passphrase.split(' ')

    for word in words:
        if words.count(word) > 1:
            return False

    return True


def count_valid_passphrases():
    with open("day4.txt") as file:
        passphrases = file.readlines()
        counter = 0

        for passphrase in passphrases:
            if is_valid_passphrase(passphrase.rstrip('\n')):
                counter += 1

    return counter


print(count_valid_passphrases())

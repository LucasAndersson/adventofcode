def find_exit(offsets):
    i = 0
    steps = 0

    while 0 <= i < len(offsets):
        offset = offsets[i]

        if offset >= 3:
            offsets[i] = offset - 1
        else:
            offsets[i] = offset + 1

        steps += 1
        i += offset

    return steps


def main():
    with open("input") as file:
        offsets = [int(line.rstrip("\n")) for line in file]
        print(find_exit(offsets))


main()

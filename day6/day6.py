class Result:
    def __init__(self, cycles, states_len, banks):
        self.cycles = cycles
        self.states_len = states_len
        self.banks = banks


def redistribute_blocks(banks):
    states = []
    cycles = 0

    while True:
        blocks = max(banks)
        index = banks.index(blocks)
        banks[index] = 0

        while blocks > 0:
            if index + 1 < len(banks):
                index += 1
            else:
                index = 0

            banks[index] += 1
            blocks -= 1

        cycles += 1

        if banks in states:
            return Result(cycles, len(states), banks)

        states.append(list(banks))


def main():
    result = redistribute_blocks([11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11])
    print(result.cycles)

    result = redistribute_blocks(result.banks)
    print(result.states_len)


main()

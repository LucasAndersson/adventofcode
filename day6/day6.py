import sys


def redistribute_blocks(banks, states, cycles):
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
        return cycles

    states.append(list(banks))

    return redistribute_blocks(banks, states, cycles)


def main():
    print(redistribute_blocks([0, 2, 7, 0], [], 0))
    sys.setrecursionlimit(10000)
    print(redistribute_blocks([11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11], [], 0))

    # state1 = [0, 2, 7, 0]
    # states = [list(state1)]
    # print(state1)
    # state2 = redistribute_blocks(state1)
    # states.append(list(state2))
    # print(state2)
    # state3 = redistribute_blocks(state2)
    # states.append(list(state3))
    # print(state3)
    # state4 = redistribute_blocks(state3)
    # states.append(list(state4))
    # print(state4)
    # state5 = redistribute_blocks(state4)
    # states.append(list(state5))
    # print(state5)
    # state6 = redistribute_blocks(state5)
    # states.append(list(state6))
    # print(state6)
    # print()
    # print(states)


main()

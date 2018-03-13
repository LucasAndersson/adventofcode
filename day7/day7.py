class Program:
    def __init__(self, name, weight, children, parent=None):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = parent

    def __str__(self):
        return "(name={}, weight={}, children={}, parent={})".format(self.name, self.weight, str(self.children),
                                                                     self.parent)

    def __repr__(self):
        return self.__str__()


def main():
    programs = {}

    with open("input") as f:
        for line in f:
            line = line.rstrip("\n")
            args = line.split(' ')
            name = args[0]
            weight = args[1].replace('(', '').replace(')', '')
            children = []

            for i in range(3, len(args)):
                children.append(args[i].replace(',', ''))

            program = Program(name, weight, children)
            programs[program.name] = program

    for name in programs.keys():
        program = programs[name]

        if len(program.children) == 0:
            continue

        for child_name in program.children:
            child = programs[child_name]
            child.parent = program.name

    for name in programs.keys():
        if programs[name].parent is None:
            print(programs[name])


main()

__author__ = 'Kyle DeRosa'


def T9_spelling(in_name, out_name, T9_dict):

    with open(in_name, "r") as infile, open(out_name, "w") as outfile:
        N = int(infile.readline())
        print(str(N) + ' cases to process \n')
        for case_index in range(0, N):
            line = infile.readline()
            previous = T9_dict[line[0]]
            out_line = previous
            for i in range(1, len(line) - 1):
                if T9_dict[line[i]][0] == previous[0]:
                    out_line += " " + T9_dict[line[i]]
                else:
                    out_line += T9_dict[line[i]]
                previous = T9_dict[line[i]]

            out_line = "Case #" + str(case_index + 1) + ": " + out_line + "\n"
            outfile.write(out_line)


if __name__ == "__main__":

    T9 = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4',
          'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66',
          'o': '666', 'p': '7', 'q': '77', 'r': '777', 's': '7777', 't': '8', 'u': '88',
          'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999', ' ': '0'}

    print('small file')
    T9_spelling("C-small-practice.in", "C-small-practice.out", T9)
    print('large file')
    T9_spelling("C-large-practice.in", "C-large-practice.out", T9)


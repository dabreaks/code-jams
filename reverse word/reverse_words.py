__author__ = 'Kyle DeRosa'


def reverse_words(in_name, out_name):

    with open(in_name, "r") as infile, open(out_name, "w") as outfile:
        N = int(infile.readline())
        print(str(N) + ' cases to process \n')
        for case_index in range(0, N):
            words = infile.readline()
            words = words.split()
            out_line = "Case #" + str(case_index+1) + ": " + " ".join(words[::-1]) + "\n"
            outfile.write(out_line)

if __name__ == "__main__":

    print('small file')
    reverse_words("B-small-practice.in", "B-small-practice.out")
    print('large file')
    reverse_words("B-large-practice.in", "B-large-practice.out")



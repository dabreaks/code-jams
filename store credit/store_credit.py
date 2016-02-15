__author__ = 'Kyle DeRosa'

# Problem

# You receive a credit C at a local store and would like to buy two items.
# You first walk through the store and create a list L of all available items.
# From this list you would like to buy two items that add up to the entire value of the credit.
# The solution you provide will consist of the two integers indicating the positions of the items in your list
# (smaller number first).

# Input

# The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:


# One line containing the value C, the amount of credit you have at the store.
# One line containing the value I, the number of items in the store.
# One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
# Each test case will have exactly one solution.
# Output

# For each test case, output one line containing "Case #x: "
# followed by the indices of the two items whose price adds up to the store credit.
# The lower index should be output first.

#Limits

#5 ? C ? 1000
#1 ? P ? 1000

#Small dataset

#N = 10
#3 ? I ? 100

#Large dataset

#N = 50
#3 ? I ? 2000


def store_credit(in_name, out_name):

    with open(in_name, "r") as infile, open(out_name, "w") as outfile:
        N = int(infile.readline())
        print(str(N) + ' cases to process \n')
        for case_index in range(0, N):
            C = int(infile.readline())
            I = int(infile.readline())
            items = infile.readline()
            items = items.split()
            print(str(I) + ' items \n')
            for i in range(0, len(items)-1):
                for j in range(i+1, len(items)):
                    total = int(items[i]) + int(items[j])
                    if total == C:
                        purchase = "Case #" + str(case_index + 1) + ": " + str(i+1) + ' ' + str(j+1) + "\n"
                        outfile.write(purchase)


if __name__ == "__main__":

    print('small file')
    store_credit("A-small-practice.in", "A-small-practice.out")
    print('large file')
    store_credit("A-large-practice.in", "A-large-practice.out")

# code-jams
google code jams that are over where it's okay for me to put things here?

---

### T-9

#### Problem

The Latin alphabet contains 26 characters and telephones only have ten digits on the keypad. We would like to make it easier to write a message to your friend using a sequence of keypresses to indicate the desired characters. The letters are mapped onto the digits as shown below. To insert the character B for instance, the program would press 22. In order to insert two characters in sequence from the same key, the user must pause before pressing the key a second time. The space character ' ' should be printed to indicate a pause. For example, 2 2 indicates AA whereas 22 indicates B.

#### Input

The first line of input gives the number of cases, N. N test cases follow. Each case is a line of text formatted as desired_message
Each message will consist of only lowercase characters a-z and space characters ' '. Pressing zero emits a space.

#### Output

For each test case, output one line containing "Case #x: " followed by the message translated into the sequence of keypresses.

#### Limits

1 ? N ? 100.

--- 

### reverse words

#### Problem

Given a list of space separated words, reverse the order of the words. Each line of text contains L letters and W words. A line will only consist of letters and space characters. There will be exactly one space character between each pair of consecutive words.

#### Input

The first line of input gives the number of cases, N.
N test cases follow. For each test case there will a line of letters and space characters indicating a list of space separated words. Spaces will not appear at the start or end of a line.

#### Output

For each test case, output one line containing "Case #x: " followed by the list of words in reverse order.

---

### store credit

#### Problem

You receive a credit C at a local store and would like to buy two items. You first walk through the store and create a list L of all available items. From this list you would like to buy two items that add up to the entire value of the credit. The solution you provide will consist of the two integers indicating the positions of the items in your list (smaller number first).

#### Input

The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:

One line containing the value C, the amount of credit you have at the store.
One line containing the value I, the number of items in the store.
One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
Each test case will have exactly one solution.

#### Output

For each test case, output one line containing "Case #x: " followed by the indices of the two items whose price adds up to the store credit. The lower index should be output first.

Limits

5 ? C ? 1000
1 ? P ? 1000

---
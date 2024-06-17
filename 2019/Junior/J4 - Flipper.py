def run_length_encoding(input_lines):
    for line in input_lines:
        i = 0
        while i < len(line):
            count = 1
            while i + 1 < len(line) and line[i] == line[i+1]:
                i += 1
                count += 1
            print(count, line[i], end=' ')
            i += 1
        print()

# Test the function with the sample input
#run_length_encoding(["+++===!!!!", "777777......TTTTTTTTTTTT", "(AABBC)", "3.1415555"])
n = int(input(""))
inputs = []
for _ in range(0, n):
    inputs.append(input(""))

run_length_encoding(inputs)

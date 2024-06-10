# Read input
books = input()

# count numbers of L and M
num_L = books.count('L')
num_M = books.count('M')
num_S = books.count('S')

# get sub_string basing on the numbers of L and M
sub_L = books[:num_L]
sub_M = books[num_L:num_M + num_L]
sub_S = books[num_L+num_M:]

print(sub_L.count("M") + sub_L.count("S") + max(sub_M.count("S"), sub_S.count("M")))

book = {}
pages = int(input(""))
for page in range(pages):
    num_options, *destinations = input().split()
    if int(num_options) == 0:
        book[page + 1] = [0]
    else:
        book[page + 1] = [int(i) for i in destinations]
#print(book)
#print(pages, "pages")
# use BFS (breatdh first search) to find all paths
#       1
#    2      3
#4      5       6
queue = [] #FIFO(fist in first out) Op1 put into queue, Op2 pop from queue
queue.append([1])

visited = {1}
paths = []
#use loop to access basing on the book dict

while len(queue) > 0:
    path = queue.pop(0)
    # get the page
    for page in book[path[-1]]:
        if page == 0:
            paths.append(path)
        elif page not in visited:
            visited.add(page)
            queue.append(path + [page])
# after two iterations, queue is [[1,2], [1,3]]
if len(visited) == len(book):
    print("Y")
else:
    print("N")
print(len(paths[0]))

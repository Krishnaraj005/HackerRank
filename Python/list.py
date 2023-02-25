# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
# Example

# N = 4
# append 1
# append 2
# insert 3 1
# print

# append 1: Append 1 to the list, arr = [1].
# append 2: Append 2 to the list, arr = [1, 2].
# insert 3 1: Insert 3 at index 1,arr = [1, 3, 2].
# print: Print the array.
# Output:

# [1, 3, 2]

# Sample input 0:

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample output 0:

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        s = list(input().split())
        if s[0]=='insert':
            l.insert(int(s[1]),int(s[2]))
        if s[0]=='remove':
            l.remove(int(s[1]))
        if s[0]=='append':
            l.append(int(s[1]))
        if s[0]=='sort':
            l.sort()
        if s[0]=='pop':
            l.pop()
        if s[0]=='reverse':
            l.reverse()     
        if s[0]=='print':
            print(l)

import heapq

# Creating a heap
h = [10, 20, 15, 30, 40]
heapq.heapify(h)

# Find the 3 largest elements
maxi = heapq.nlargest(3, h)
print("3 largest elements:", maxi)

# Find the 3 smallest elements
min = heapq.nsmallest(3, h)
print("3 smallest elements:", min)
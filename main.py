##################################################       Over All O(E^2)          #############################################################
import pandas as pd
import time

start_time = time.time()
df = pd.read_csv('twitter.csv')  # O(E) Where n is The Length of Input
df.columns = ['A', 'followed']  # O(k) Where K is No.Of Columns in File
df.drop_duplicates(subset=None, inplace=True)  # The worst-case running time with this approach is O(E2)
followedList = df['followed'].tolist()  # O(E) where E is the number of rows in the dataframe

ListDict = dict()
# frequency Array
for i in followedList:  # The worst-case running time with O(EV)
    if i in ListDict:
        ListDict[i] += 1
    else:
        ListDict[i] = 1

sortedDict = {k: v for k, v in sorted(ListDict.items(), key=lambda v: v[1], reverse=True)}  # O(V log V) Heap Sort


def Top_followed(n):  # O(k) & Worst case is O(V)
    query = dict()
    count = 0
    for key, value in sortedDict.items():  # O(k) & Worst case is O(V)
        if (n == 0):
            break
        query[key] = value
        n -= 1
        count += 1
        print(count, " ) ID :", key, " Has followers : ", query[key])
    print('------------------------------------------\n')


Top_followed(1)
# while True:  # O(k)
#     print("Please Enter Operation U need : ")
#     print("1-Show N records .\n"
#           "2-Show the first three top influncer.\n")
#     while True:
#         try:
#             inp = int(input("Your Choice : "))
#             break
#         except ValueError:
#             print('Oops ..!! Invalid entry')
#
#     if inp == 1:
#         while True:
#             try:
#                 x = int(input('please enter no. U need : '))
#                 break
#             except ValueError:
#                 print('Oops ..!! Invalid entry')
#         Top_followed(x)
#     elif inp == 2:
#         Top_followed(3)
print("time elapsed: {:.2f}s".format(time.time() - start_time))
##########################

# import pandas as pd
# import time
#
# start_time = time.time()
# file = pd.read_csv("twitter.csv")
# file_name = "twitter.csv"
# file = "twitterr.csv"
#
# df = pd.read_csv(file_name, sep=",")
# df.drop_duplicates(subset=None, inplace=True)
#
# # Write the results to a different file
# df.to_csv(file, index=False)
# file = pd.read_csv("twitterr.csv")
# file.columns = ['x', 'y']
# followers = file['y'].tolist()
#
# #
# arrDict = {}
# # frequency Array
# for i in followers:  # O(n)
#     if i in arrDict:
#         arrDict[i] += 1
#     else:
#         arrDict[i] = 1
#
# first = second = third = 0
#
# for i in arrDict:  # O(n)
#     if (arrDict[i] > first):
#
#         third = second
#         second = first
#         first = arrDict[i]
#     elif (arrDict[i] > second):
#         third = second
#         second = arrDict[i]
#     elif (arrDict[i] > third):
#         third = arrDict[i]
# temp_first = temp_second = temp_third = 0
# newDict = {}
# for key, val in arrDict.items():
#     if val == first:
#         temp_first = key
#         newDict[key] = first
#     if val == second:
#         temp_second = key
#         newDict[key] = second
#     if val == third:
#         temp_third = key
#         newDict[key] = third
# if temp_first > 0:
#     print("Top influencer", key, " & No. of followers is ", first)
# if temp_second > 0:
#     print("second influencer", key, " & No. of followers is ", second)
# if temp_third > 0:
#     print("third influencer", key, " & No. of followers is ", third)
# print("time elapsed: {:.2f}s".format(time.time() - start_time))

##############################

# import csv
#
# filename = 'twitterr.csv'
# with open(filename, 'r') as p:
#     # reads csv into a list of lists
#     # my_list = list(list(rec) for rec in csv.reader(p, delimiter=','))
#     my_list = [list(map(int, rec)) for rec in csv.reader(p, delimiter=',')]
# # my_list = numpy.random.uniform(0,1,size=(4,4))
# import numpy
# numpy_arr = numpy.array(((1527, 1369,   86,   86),(573 , 590 , 709,  709)))
# my_list= tuple(map(tuple,numpy_arr)) # as list
# converted_arr = map(tuple,numpy_arr) #as array
# print(converted_arr)


# print(my_list)
# print(len(arrDict.keys()))
# print(arrDict.keys())


# class Graph:
#     # Constructor
#     def __init__(self, edges, n):
#         # allocate memory for the adjacency list
#         self.adjList = [[] for _ in range(n)]
#
#         # add edges to the directed graph
#         for (src, dest) in edges:
#             # allocate node in adjacency list from src to dest
#             self.adjList[src].append(dest)
#
#
# # Function to print adjacency list representation of a graph
# def printGraph(graph):
#     for src in range(len(graph.adjList)):
#         # print current vertex and all its neighboring vertices
#         for dest in graph.adjList[src]:
#             print(f'({src} —> {dest}) ', end='')
#         print()
#
#
# if __name__ == '__main__':
#     # Input: Edges in a directed graph
#     edges = my_list
#
#     # No. of vertices (labelled from 0 to 5)
#     n = arrDict.keys()
#
#     # construct a graph from a given list of edges
#     graph = Graph(edges, n)
#
#     # print adjacency list representation of the graph
#     printGraph(graph)

###############################


# Function
# to
# add
# edges
# import csv
#
# filename = 'twitterr.csv'
# with open(filename, 'r') as p:
#     # reads csv into a list of lists
#     # my_list = list(list(rec) for rec in csv.reader(p, delimiter=','))
#     my_list = [list(map(int, rec)) for rec in csv.reader(p, delimiter=',')]
#     print(my_list)


# def addEdge(adj, u, v):
#     adj[u].append(v)
#
#
# # Function to print adjacency list
# def adjacencylist(adj, V):
#     for i in range(0, V):
#         print(i, "->", end="")
#
#         for x in adj[i]:
#             print(x, " ", end="")
#
#         print()
#
#
# # Function to initialize the adjacency list
# # of the given graph
# def initGraph(V, edges, noOfEdges):
#     adj = [0] * len(arrDict.keys())
#
#     for i in range(0, len(adj)):
#         adj[i] = []
#
#     # Traverse edges array and make edges
#     for i in range(0, noOfEdges):
#         # Function call to make an edge
#         addEdge(adj, edges[i][0], edges[i][1])
#
#     # Function Call to print adjacency list
#     adjacencylist(adj, V)
#
#
# # Driver Code
#
# # Given vertices
# V = len(arrDict.keys())
#
# # Given edges
# edges = my_list
#
# noOfEdges = len(my_list)
#
# # Function Call
# initGraph(V, edges, noOfEdges)

#################################


# list1 = list(arrDict.values())
#
#
# def Nmaxelements(list1, N):
#     followers_list = []
#     followering_list = []
#
#     for i in range(0, N):
#         max1 = 0
#
#         for j in range(len(list1)):
#             if list1[j] > max1:
#                 max1 = list1[j]
#
#         list1.remove(max1)
#         followers_list.append(max1)
#
#     return followers_list
#
#
# x = int(input("Enter N : "))
# print(Nmaxelements(list1, x))
# # print(max(arrDict.values()))
# # print(len(arrDict.values()))
# print("time elapsed: {:.2f}s".format(time.time() - start_time))


##############################


# # Adjascency List representation in Python
#
#
# # Python program to print topological sorting of a DAG
# from collections import defaultdict
#
#
# # Class to represent a graph
#
#
# class Graph:
#     def __init__(self, vertices):
#         self.graph = defaultdict(list)  # dictionary containing adjacency List
#         self.V = vertices  # No. of vertices
#
#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     # A recursive function used by topologicalSort
#     def topologicalSortUtil(self, v, visited, stack):
#
#         # Mark the current node as visited.
#         visited[v] = True
#
#         # Recur for all the vertices adjacent to this vertex
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 self.topologicalSortUtil(i, visited, stack)
#
#         # Push current vertex to stack which stores result
#         stack.append(v)
#
#     # The function to do Topological Sort. It uses recursive
#     # topologicalSortUtil()
#     def topologicalSort(self):
#         # Mark all the vertices as not visited
#         visited = [False] * self.V
#         stack = []
#
#         # Call the recursive helper function to store Topological
#         # Sort starting from all vertices one by one
#         for i in range(self.V):
#             if visited[i] == False:
#                 self.topologicalSortUtil(i, visited, stack)
#
#         # Print contents of the stack
#         print(stack[::])  # return list in reverse order
#
#
# # Driver Code
# g = Graph(6)
# g.addEdge(5, 2)
# g.addEdge(5, 0)
# g.addEdge(4, 0)
# g.addEdge(4, 1)
# g.addEdge(2, 3)
# g.addEdge(3, 1)
#
# print("Following is a Topological Sort of the given graph")
#
# # Function Call
# g.topologicalSort()
#
# # This code is contributed by Neelam Yadav

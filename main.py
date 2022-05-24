###################################################       Over All O(E^2)          #############################################################
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


# Top_followed(1)
while True:  # O(k)
    print("Please Enter Operation U need : ")
    print("1-Show N records .\n"
          "2-Show the first three top influncer.\n")
    while True:
        try:
            inp = int(input("Your Choice : "))
            break
        except ValueError:
            print('Oops ..!! Invalid entry')

    if inp == 1:
        while True:
            try:
                x = int(input('please enter no. U need : '))
                break
            except ValueError:
                print('Oops ..!! Invalid entry')
        Top_followed(x)
    elif inp == 2:
        Top_followed(3)
# print("time elapsed: {:.2f}s".format(time.time() - start_time))


##########################

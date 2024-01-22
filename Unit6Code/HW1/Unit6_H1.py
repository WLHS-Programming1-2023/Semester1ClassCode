
def zip(list1,list2):
    # [1,2,3] [4,5,6]
    # [(1,4),(2,5),(3,6)]
    final_list = []
    for i in range(len(list1)):
        final_list.append((list1[i],list2[i]))
    return final_list



def unzip(list):
    #[(1,4),(2,5),(3,6)]
    #([1,2,3],[4,5,6])
    length = len(list)
    list1 = []
    list2 = []
    for i in range(length):
        list1.append(list[i][0])
        list2.append(list[i][1])
    return (list1,list2)

def main():
    list1 = [1,2,3]
    list2 = [4,5,6]
    list3 = zip(list1,list2)
    print(list3)
    tuple1 = unzip(list3)
    print(tuple1)

if __name__ == "__main__":
    main()
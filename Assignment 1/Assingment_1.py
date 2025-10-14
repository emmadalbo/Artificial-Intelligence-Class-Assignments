"""Module providing solutions to Problems 1-5 in Assignment 1."""

###Problem 1###
def is_triangle(tocompare):
    """Compares a number 'tocompare' against all triangular nums, returning False when tri-nums become bigger than 'tocompare'"""""
    n=1
    while True: #calculate multiple triangular numbers starting from smallest- do any match tocompare?
        this_t=(n+1)*(n/2) #formula for triangle number
        if this_t == tocompare:
            return True
        elif this_t > tocompare:
            return False
        n+=1

def triangle_nos(numbers):
    """Initial function to assess if a list of nums is a sequence of triangular nums"""
    #check that numbers is a list
    if isinstance(numbers, list) is False:
        print("ERROR: Not a list")
        return
    for this_number in numbers: #checks each number in our list to be triangular
        if is_triangle(this_number):
            continue
        else:
            return False
    return True
######






###Problem 2###
def l_intersection(list1:list[any], list2:list[any]):
    """Function to find intersection of two sets as lists"""
    if isinstance(list1, list) is False or isinstance(list2, list) is False:
        return "ERROR- input not a list"
    #iterate through lists so each item is considered
    list3= []
    for each1 in list1:
        for each2 in list2:
            if each1 == each2:
                if each1 in list3:#don't add if it's already in list3
                    continue
                else:
                    list3.append(each1)#add if new to list3
    return list3

def l_union(list1:list[any], list2:list[any]):
    """Function  to find union of two sets as lists"""
    if isinstance(list1, list) is False or isinstance(list2, list) is False:
        return "ERROR- input not a list"
    #combine l1 and l2
    list3 = list1 + list2
    #remove duplicates
    i=0
    while i<len(list3):
        count = i+1
        while count<len(list3):
            if list3[i] == list3[count]:#if item is found elsewhere on list, delete
                del list3[count]
            else:
                count += 1
        i+=1
    return list3
######






###Problem 3###
def replace_list_item(mylist, myitem):
    """Function to replace an item on a list with another item (tupled with new updated count)- assumes item is certainly present"""
    k = 0
    while k<len(mylist):
        if mylist[k][0] == myitem:
            break
        k+=1
    new_count = mylist[k][1] + 1
    mylist[k] = (myitem, new_count)
    return mylist

def add_to_tuple(list1):
    """Function to make a list of tuples, depicting frequency of items in list1"""
    list2 = []
    #initialize list2
    this_tuple = (list1[0],1)
    list2.append(this_tuple)
    i=1 #to iterate through list1
    while i<len(list1):
        for current_tuple in list2:
            add_new_tuple = True#flag becomes false
            if current_tuple[0] == list1[i]:#is our item already on list- must change count
                add_new_tuple = False
                list2 = replace_list_item(list2,list1[i])#function to change count by replacing
                break
        if add_new_tuple: #flag wasn't raised as false
            this_tuple = (list1[i], 1)
            list2.append(this_tuple)
        i+=1
    return list2

def occurrences(list1):
    """Initial function to create an occurrences list after an initial list is provided"""
    if isinstance(list1, list) is False:
        print("ERROR- input not a list")
        return
    list2 = add_to_tuple(list1)#make list in any order
    list3 = []#will make list in highest-count order
    while len(list2)>0:
        highest = 0
        counting = 0
        while counting < len(list2):
            if list2[counting][1] > highest:
                highest = list2[counting][1]
                item = list2[counting][0]
            counting += 1
        #add to list3, delete from list2
        list3.append((item, highest))
        list2.remove((item, highest))
    return list3
######






###Problem 4###
def delete_duplicates(mylist):
    """Function to delete any duplicates from a list 'mylist'"""
    i=0
    while i<len(mylist):
        count = i+1
        while count<len(mylist):
            if mylist[i] == mylist[count]:
                del mylist[count]
            else:
                count += 1
        i+=1
    return mylist

def power_set(s: list[any]) -> list[list[any]]:
    """Initial function to create a powerset from given set s"""
    if isinstance(s, list) is False:
        print("ERROR- input not a list")
        return
    slist = [[]]
    s = delete_duplicates(s)
    lengthsi = 1
    amt_of_lengths = len(s)#max length of a sub-list
    while lengthsi<amt_of_lengths+1:#goes through each length amount possible for our sub-lists
        recursing(s, slist, 0, lengthsi,[], amt_of_lengths)
        lengthsi += 1#iterate to next length 
    return slist


def recursing(mys, slist, startingi, lengthsi, this_list, amt_of_lengths):
    """Recursing function to create subsets for the powerset"""
    #recurse for different lengths (lengthsi)
    if lengthsi == len(this_list):#if this_list is complete
        slist.append(this_list[0:lengthsi]) #adds this_list, now finished, to slist
        return #exits this recursion round
    i = startingi#place in the s to begin creating this_list
    while i<amt_of_lengths:
        this_list.append(mys[i])#increase this_list with each index item from s up to length
        recursing(mys, slist, i+1, lengthsi, this_list, amt_of_lengths)
        this_list.pop()#clear last item from this_list
        i+=1
######






###Problem 5###
#Uses function "power_set" from Problem 4
#Uses function "l_union" from Problem 2
#Uses function "l_intersection" from Problem 2
def sort_tau(t):#assumes t is a list of lists, no deeper nesting
    """Function to sort Tau in an appropriate order for easier analysis"""
    i=0
    for each_set in t:
        if len(each_set) > 1:
            each_set.sort()
        i+=1
    t.sort()
    return t

def compare_to_power_set(s, t):
    """Function to ensure items in Tau are in powerset of s"""
    ps = power_set(s)
    if t == [[], s]:
        return 2#cop out- it's our smallest valid topology
    for each_list in t:
        if each_list not in ps:
            print(each_list, "is not in power_set")
            return 0 #fails test
    return 1#passes test

def satisfy_a(s, t):
    """Function to check for satisfaction of topology req. a"""
    #check for null
    null_present = False
    for each_list in t:
        if not each_list:
            null_present = True
    if null_present is False:
        return 0#fails test
    #check for S
    for each_list in t:
        if each_list == s:
            return 1#passes test
    return 0#fails test

def satisfy_b(t):
    """Function to check for satisfaction of topology req. b"""
    i = 0
    while i<len(t)-1:
        part1 = t[i]
        k = i+1
        while k<len(t):
            part2 = t[k]
            current_set = l_intersection(part1, part2)
            if current_set not in t:
                return 0#fails test- intersection of lists is not in Tau
            k+=1
        i+=1
    return 1#passed test of intersection for all U/V

def satisfy_c(t):
    """Function to check for satisfaction of topology req. c"""
    i = 0
    while i<len(t)-1:
        part1 = t[i]
        k = i+1
        while k<len(t):
            part2 = t[k]
            current_set = l_union(part1, part2)
            if current_set not in t:
                return 0#fails test- union of lists is not in t
            k+=1
        i+=1
    return 1#passed test of union for all U/V




def check_topology(S: list[any], Tau:  list[list[any]]) -> bool:
    """Initial function to see if S and Tau define a finite topological space"""
    #sort Tau and all it's lists first
    Tau = sort_tau(Tau)
    #ensure all digits of Tau are in power_set
    hold = compare_to_power_set(S, Tau)
    if hold == 0:
        return False
    elif hold == 2:
        return True
    #check to satisfy a requirement of null and S:
    if satisfy_a(S,Tau) == 0:
        return False
    #check to satisfy b requirement of intersection:
    if satisfy_b(Tau) == 0:
        return False
    #check to satisfy c requirement of union:
    if satisfy_c(Tau) == 0:
        return False
    return True#passed all the tests
######







def main():
    # Example invocations of the functions
    result_triangle_nos = triangle_nos([66, 36, 190])
    result_l_intersection = l_intersection([4, 5, 10, 3], [3, 10, 12])
    result_l_union = l_union([4, 5, 10, 3],[3, 10, 12])
    result_occurrences = occurrences(["a", "a", ["c", ["d"]], ["b"], "a", "c", ["b"]])
    result_power_set = power_set([1,2,2,3])
    result_check_topology1 = check_topology([1,2], [[],[2],[1],[1,2]])
    result_check_topology2 = check_topology([1,2], [[],[1],[1,2]])
    result_check_topology3 = check_topology([1,2], [[1],[2],[1,2]])
    result_check_topology4 = check_topology([1,2,3], [[],[1,3],[2,3],[1,2,3]])
    result_check_topology5 = check_topology([1,2,3], [[],[1],[2],[1,2,3]])

    # Displaying the results
    print("Inputting [66, 36, 190] in triangle_nos gives:", result_triangle_nos)
    print("Inputting [4, 5, 10, 3], [3, 10, 12] in l_intersection gives:", result_l_intersection)
    print("Inputting [4, 5, 10, 3],[3, 10, 12] in l_union gives:", result_l_union)
    print("Inputting ['a', 'a', ['c', ['d']], ['b'], 'a', 'c', ['b']] in occurrences gives:", result_occurrences)
    print("Inputting [1,2,2,3] in power_set gives:", result_power_set)
    print("Inputting S=[1,2] and Tau= [[],[2],[1],[1,2]], which is a topology, in check_topology gives:", result_check_topology1)
    print("Inputting S=[1,2] and Tau= [[],[1],[1,2]], which is a topology, in check_topology gives:", result_check_topology2)
    print("Inputting S=[1,2] and Tau= [[1],[2],[1,2]], which is NOT a topology, in check_topology gives:", result_check_topology3)
    print("Inputting S=[1,2,3] and Tau= [[],[1,3],[2,3],[1,2,3]], which is NOT a topology, in check_topology gives:", result_check_topology4)
    print("Inputting S=[1,2,3] and Tau= [[],[1],[2],[1,2,3]], which is NOT a topology, in check_topology gives:", result_check_topology5)


main()

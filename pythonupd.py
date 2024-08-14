### Advanced Operations on Python Lists

## Task 1 - Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, 
 # where n is a parameter. Analyze the time and space complexity of this operation.

def squares(n):
    return [sqr**2 for sqr in range(1, n+1)] if n > 1 else None

# test
print(squares(100)) 

# The time complexity of this function is linear, O(n), as it literally performs the function n number of times. The space 
# complexity is also linear; it will require space for as many elements will be returned in its list. 



## Task 2 - Implement a function to reverse a sublist within a list from index i to j (inclusive). Analyze the time and space 
 # complexity of this operation

def reverse_sublist(list, i, j):
    if i >= len(list) or j >= len(list) or j <= i:
        return "Invalid Input"
    sublist = list[i:j+1]
    reversed_sublist = sublist[::-1]
    return reversed_sublist

# test
print(reverse_sublist(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'], 4, 8))

# In this function, the sublist is reversed by stepping backwards through its elements. Since we're stepping through the list, the 
# time complexity will scale linearly with however many elements it has. Time complexity is 0(n) and space complexity is also 0(n), 
# since a new list is created and could be any amount of elements from 2 to the full length of the original list.



## Task 3 - Implement a function to merge two sorted lists into a single sorted list. Analyze the time and space complexity of this operation.

def merge_sorted_lists(list_a, list_b):
    tracker_a, tracker_b = 0, 0
    new_list = []
    for i in range(len(list_a) + len(list_b)):
        if tracker_a >= len(list_a):
            return new_list + list_b[tracker_b:]
        elif tracker_b >= len(list_b):
            return new_list + list_a[tracker_a:]
        elif list_a[tracker_a] <= list_b[tracker_b]:
            new_list.append(list_a[tracker_a])
            tracker_a+=1
        else:
            new_list.append(list_b[tracker_b])
            tracker_b+=1
    return new_list

# test
print(merge_sorted_lists([1, 4, 8, 13, 34, 83], [1, 2, 9, 15, 33, 34, 35, 36, 37, 38, 39]))

# Here I utilized two tracker variables and only used one forloop to keep time complexity down; the single forloop iterates 
# through a number of times equal to the total number of elements in the two lists. This gives us a linear time complexity, O(n). 
# The space complexity is constant, since the number of elements passed in is the same number of elements we get out, just in one 
# list instead of two.



### Dictionary Manipulation and Optimization

## Task 1 - Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. 
# Analyze the time and space complexity of this operation.

def merge_dictionaries(dict_a, dict_b):
    for key, value in dict_b.items():
        dict_a[key] = value
    return dict_a

# test
dict_a = {
    "Name" : "James",
    "Dogs" : "Peaches & Wendell",
    "Favorite Movie" : "The Tree of Life",
    "Email" : "jamesmbcarlson@gmail.com"
}
dict_b = {
    "Name" : "James",
    "Favorite Drink" : "Coffee",
    "Favorite Movie" : "Avengers Endgame"
}
print(merge_dictionaries(dict_a, dict_b))

# The time complexity of this function is linear, O(n), as the for loop has to iterate through dict_b's items n number of times. 
# The space complexity of this function is linear, O(n), since the values being added to dict_a depend on what is being added from dict_b. 



## Task 2 - Implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with 
# their values. Analyze the time and space complexity of this operation.

def dict_intersection(dict_a, dict_b):
    intersection = {}
    for key, value in dict_a.items():
        if key in dict_b and dict_b[key] == value:
            intersection[key] = value
    return intersection

# test
print(dict_intersection(dict_a, dict_b))

# The time complexity of this function is linear, O(n), since it is iterating through the key-value pairs of dict_a. The space complexity
# of this function is linear, O(n), since any numbe rof matching key-value pairs could be found between the two dictionaries.



## Task 3 - Implement a function to count the frequency of each unique word in a list using a dictionary. Analyze the time and 
# space complexity of this operation.

def count_words(list):
    words_counter = {}
    for i in range(len(list)):
        if list[i] in words_counter:
            words_counter[list[i]] += 1
        else:
            words_counter[list[i]] = 1

    return words_counter

# test
word_list = ['dog', 'cookie', 'dog', 'beer', 'coffee', 'coffee', 'hat', 'baby', 'dog']
print(count_words(word_list))

# Iterating through a single forloop makes this linear time complexity, O(n). The space complexity is also linear, O(n), since the output
# may take up as much space as there are unique words in the original list.
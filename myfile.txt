                                                              Assignment-2
1.
marks = {"Mayank": 23 , "Harsh" : 42 , "Megha": 23}
print(marks)
sv = sorted(marks.items(),key = lambda x : x[1])#sort by value in ascending
print(sv)
sv = sorted(marks.items(),reverse = True,key = lambda x : x[1])#sort by value in Descending
print(sv)
2.
d1 = {1:"a",2:"b"}
d2 = {3:"c"}
d1.update(d2)
print(d1)
3.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
4.
dic1={1:10, 2:20}
x = int(input()) or input()
print(x in dic1.keys())
5.
dic1={1:10, 2:20}
for i in dic1:
  print(f"{i}:{dic1[i]}")
6.
n = int(input())
print({x:x**2 for x in range(0,n+1)})
7.
n = int(input())
print({x:x**2 for x in range(0,n+1)})
8.
#you can take input ny the user
d1 = {1:"a"}
d2 = {2:"b"}
#using update fxn of dictionary
d1.update(d2)#this helps to merge two dict
print(d1)
9.
dic1={1:10, 2:20}
for i in dic1:
  print(f"{i}:{dic1[i]}")
10.
#first assign a dictionary u can take by user
d1 = {1:2,2:4,3:6}#all items are in integers
#first we take sum of keys
sum_keys = 0
for i in d1:
  sum_keys += i
#then we take sum of values
sum_values = 0
for i in d1:
  sum_values += d1[i]
#for taking sum of all items we add keys and values
sum_items = sum_keys + sum_values
print(sum_items)
11.
#first assign a dictionary u can take by user
d1 = {1:2,2:4,3:6}#all items are in integers
#first we take sum of keys
sum_keys = 0
for i in d1:
  sum_keys *= i
#then we take sum of values
sum_values = 0
for i in d1:
  sum_values *= d1[i]
#for taking sum of all items we add keys and values
sum_items = sum_keys * sum_values
print(sum_items)
12.
dic1 = {
  1:2,
  2:4
}
dic1.pop(1)
print(dic1)
13.
list1 = ['apple', 'banana', 'orange']
list2 = [1, 2, 3]

dictionary = dict(zip(list1, list2))

print(dictionary)
14.
dic1 = {
  2:2,
  1:4
}
dic2 = dict(sorted(dic1.items()))
print(dic2)
15.
my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

max_value = max(my_dict.values())
min_value = min(my_dict.values())

print("Maximum value:", max_value)
print("Minimum value:", min_value)
16.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person = Person("John", 25, "Male")

dictionary = vars(person)

print(dictionary)
17.
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

new_dict = {}

for key, value in my_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value

print("Original dictionary:", my_dict)
print("Dictionary with duplicates removed:", new_dict)
18.
my_dict = {}

if not my_dict:
    print("The dictionary is empty")
else:
    print("The dictionary is not empty")
19.
def combine_dicts(dict1, dict2):
    result_dict = dict(dict1)
    for key, value in dict2.items():
        if key in result_dict:
            result_dict[key] += value
        else:
            result_dict[key] = value
    return result_dict
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'b': 50, 'd': 400}
combined_dict = combine_dicts(dict1, dict2)
print(combined_dict)
20.
def unique_values(dictionary):
    unique_values = set()
    for value in dictionary.values():
        if value not in unique_values:
            unique_values.add(value)
    return unique_values
dictionary = {'a': 100, 'b': 200, 'c': 100, 'd': 300, 'e': 200}
unique_values = unique_values(dictionary)
print(unique_values)
21.
import itertools

def letter_combinations(dictionary):
    # Get the values of each key as a list
    value_lists = dictionary.values()
    # Create all combinations of values
    combinations = itertools.product(*value_lists)
    # Join each combination into a string and return as a list
    return [''.join(combination) for combination in combinations]
dictionary = {'A': ['a', 'b'], 'B': ['c', 'd'], 'C': ['e', 'f']}
combinations = letter_combinations(dictionary)
print(combinations)
22.
def highest_three(dictionary):
    # Get a list of all values in the dictionary
    values = list(dictionary.values())
    # Sort the list of values in descending order
    values.sort(reverse=True)
    # Return the first three values
    return values[:3]
dictionary = {'a': 100, 'b': 200, 'c': 50, 'd': 300, 'e': 150}
highest_three_values = highest_three(dictionary)
print(highest_three_values)
23.
def combine_values(list_of_dicts):
    combined_dict = {}
    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            if key in combined_dict:
                combined_dict[key].append(value)
            else:
                combined_dict[key] = [value]
    return combined_dict
list_of_dicts = [{'a': 1, 'b': 2}, {'a': 3, 'c': 4}, {'b': 5, 'c': 6}]
combined_dict = combine_values(list_of_dicts)
print(combined_dict)
24.
def create_dict_from_string(string):
    # Split the string into a list of words
    words = string.split()
    # Create an empty dictionary
    dictionary = {}
    # Loop through each word in the list
    for word in words:
        # If the word is already a key in the dictionary, increment its value by 1
        if word in dictionary:
            dictionary[word] += 1
        # If the word is not a key in the dictionary, create a new key-value pair with value 1
        else:
            dictionary[word] = 1
    return dictionary
string = "the quick brown fox jumps over the lazy dog"
dictionary = create_dict_from_string(string)
print(dictionary)
25.
def print_dict_as_table(input_dict):
    # Get the length of the longest key in the dictionary
    max_key_length = max(len(str(key)) for key in input_dict.keys())

    # Get the length of the longest value in the dictionary
    max_value_length = max(len(str(value)) for value in input_dict.values())

    # Print the table header
    print('| {:{}} | {:{}} |'.format('Key', max_key_length, 'Value', max_value_length))
    print('-' * (max_key_length + 3) + '|' + '-' * (max_value_length + 3))

    # Print the table rows
    for key, value in input_dict.items():
        print('| {:{}} | {:{}} |'.format(key, max_key_length, value, max_value_length))
dictionary = {'apple': 2, 'banana': 5, 'cherry': 7}
print_dict_as_table(dictionary)
26.
def count_values_by_key(input_dict, key):
    count = 0
    for k, v in input_dict.items():
        if k == key:
            if type(v) == list:
                count += len(v)
            else:
                count += 1
    return count
dictionary = {'a': 1, 'b': [2, 3, 4], 'c': 5, 'd': [6, 7]}
key = 'd'
count = count_values_by_key(dictionary, key)
print('The key "{}" has {} associated values in the dictionary.'.format(key, count))
27.
def list_to_nested_dict(keys, value):
    if len(keys) == 1:
        return {keys[0]: value}
    else:
        return {keys[0]: list_to_nested_dict(keys[1:], value)}

def convert_list_to_nested_dict(input_list):
    nested_dict = {}
    for item in input_list:
        keys = item[:-1]
        value = item[-1]
        current_dict = nested_dict
        for key in keys[:-1]:
            current_dict = current_dict.setdefault(key, {})
        current_dict[keys[-1]] = value
    return nested_dict
input_list = [['a', 'b', 'c', 1], ['a', 'b', 'd', 2], ['a', 'e', 'f', 3]]
nested_dict = convert_list_to_nested_dict(input_list)
print(nested_dict)
28.
def sort_dict_list(dictionary, key):
    dictionary[key] = sorted(dictionary[key])
    return dictionary
dictionary = {'a': ['apple', 'ant', 'artichoke'], 'b': ['banana', 'butter', 'bread']}
key = 'a'
sorted_dict = sort_dict_list(dictionary, key)
print(sorted_dict)
29.
def remove_spaces_from_dict_keys(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_key = key.replace(" ", "")
        new_dict[new_key] = value
    return new_dict
dictionary = {'first name': 'John', 'last name': 'Doe', 'age': 30}
new_dict = remove_spaces_from_dict_keys(dictionary)
print(new_dict)
30.
def get_top_three_items(shop_items):
    sorted_items = sorted(shop_items.items(), key=lambda x: x[1], reverse=True)
    top_three = sorted_items[:3]
    return top_three
shop_items = {'apple': 2.5, 'banana': 1.5, 'orange': 3, 'mango': 2, 'pear': 1}
top_three_items = get_top_three_items(shop_items)
print(top_three_items)
31.
def get_key_value_items(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}")
        print(f"Value: {value}")
        print(f"Item: {key}, {value}\n")
dictionary = {'apple': 2.5, 'banana': 1.5, 'orange': 3, 'mango': 2, 'pear': 1}
get_key_value_items(dictionary)
32.
def print_dict_line_by_line(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
dictionary = {'apple': 2.5, 'banana': 1.5, 'orange': 3, 'mango': 2, 'pear': 1}
print_dict_line_by_line(dictionary)
33.
def check_keys_exist(dictionary, keys):
    for key in keys:
        if key not in dictionary:
            return False
    return True
dictionary = {'apple': 2.5, 'banana': 1.5, 'orange': 3, 'mango': 2, 'pear': 1}
keys = ['apple', 'banana', 'pear', 'watermelon']
if check_keys_exist(dictionary, keys):
    print("All keys exist in the dictionary")
else:
    print("One or more keys do not exist in the dictionary")
34.
def count_items_in_list_values(dictionary):
    count = 0
    for value in dictionary.values():
        if isinstance(value, list):
            count += len(value)
    return count
dictionary = {'apple': [2, 3, 5], 'banana': 1.5, 'orange': [3, 4], 'mango': [2, 7], 'pear': 1}
count = count_items_in_list_values(dictionary)
print(f"The dictionary contains {count} items in list values.")
35.
def replace_values_with_sum(dictionary):
    for key in dictionary:
        if isinstance(dictionary[key], list):
            dictionary[key] = sum(dictionary[key])
    return dictionary
dictionary = {'apple': [2, 3, 5], 'banana': 1.5, 'orange': [3, 4], 'mango': [2, 7], 'pear': 1}
new_dictionary = replace_values_with_sum(dictionary)
print(new_dictionary)









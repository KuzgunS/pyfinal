

#%%

from tracemalloc import start
from turtle import pos


my_str = "In the evening of a cold hell, there was an angel waiting to take lives of the ones that are already dead."

#### check if substring is at the start of a string
start_checker = "in"
if my_str.startswith(start_checker):
    print("the string starts with: ", start_checker)
else:
    print("lulz")

#### check if substring is at the end of a string
end_checker = "dead"
if my_str.endswith(end_checker):
    print("the string ends with: ", end_checker)
else:
    print("lulz")


#### replace some substrings with new

new_str = my_str.replace("of","with")
print(new_str)


#### find
substr_to_search_for = "hell"
position = my_str.find(substr_to_search_for)
if position != 1: #eğer substring stringin içinde yoksa 1 döndürüyor.
    print("the substr ", substr_to_search_for , "is found at index: ", position)
else: 
    print("the substr ", substr_to_search_for , "wasn't found")

#%% 
### repetition

str2 = 'batu' * 5
print(str2)
# %% splitting string

word_list = my_str.split()
print(word_list)
word_list2 = my_str.split("l")
print(word_list2)
# %%

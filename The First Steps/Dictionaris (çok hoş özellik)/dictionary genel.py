
#%% deleting dict elements
my_dict = {
    'xd' : "asdf",
    1 : 2,
    2: 123
}
print(my_dict)

del my_dict['xd']
print(my_dict)


#%% using it with in and not in operators
my_dict2 = {

    'a' : 3,
    1 : 3,
    'bato' : "xdd"
} 

if 'bato' in my_dict:
    print(my_dict2['bato'])

#%% get the number of elements

my_dict = {
    'xd' : "asdf",
    1 : 2,
    2: 123
}

my_dict = {
    'xd' : "asdf",
    1 : 2,
}
print(my_dict)
num_of_items = len(my_dict)
print(num_of_items)

# %% 
my_dict = {
    'xd' : "asdf",
    #["lool" , "xd"] : 2,
    ('i\'m a ','tuple') : ['xdd'] #tuple key olabiliyor
}

print(my_dict)
print(my_dict[('i\'m a ','tuple')])

# %% creating empty dict

my_dict = {}
#or
my_dict2 = dict()

# %%

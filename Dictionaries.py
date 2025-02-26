# A dictionary in python is a colection of key-value pairs. Each key is associated with a value, and can retrive or manipulate data using the key.Unlike lists and tuples, dictionaries are un-ordered and mutable(chaneble).
# CREATING A DICTIONARY
# We can create using {} braces or dict() function.
dict1={
    "key1":"value1",
    "key2":"value2"
}
print(dict1)

dict2={
    "mysore":"regional heritage",
    "banglore":"electronic city"
}
print(dict2)

#Accessing dictionary elements
#by using key, we can access elements of the dictionary.
#EXAMPLE
print(dict2["mysore"]) # output: regional heritage
print(type(dict2)) # output: class dict

# we can also acsess usnig get() function. (to avoid errors)
print(dict2.get("banglore","NOT FOUND"))# output: electronic city
print(dict2.get("mumbai","NOT FOUND"))# output: NOT  FOUND

# Adding and updating dictionary
print(dict2)
dict2["manglore"]="coastal area" # adds new key value pair to dictionary.
print(dict2)
#updating dictionary
print("updating...")
dict2["mysore"]="calm place" # updates the dictionary.
print(dict2)

#Removing elements from dictionary
dict2.pop("mysore") # removes mysore from dictionary
print(dict2)
del dict2["banglore"] # deletes banglore from dict2
print(dict2)
dict2.clear()# clears entire dictionary 
print(dict2)


# Methods in dicionary
print(dict1.keys()) # produce output of keys name
print(dict1.values()) # produce output of values name
print(dict1.items())# prints the key-value pairs items of a dictionary.
dict3={"key3":"value3"}
dict2.update(dict3) # adds new dictionay element to a desired dictionary.
print(dict2)
 

item1={
    "name":"sugar",
    "weight":1,
    "prise":20
}


item2={
    "name":"milk",
    "weight":3,
    "prise":30
}
print(f"total weight is: {item1["weight"]+item2["weight"]} kg") # output :total weight is: 4 kg

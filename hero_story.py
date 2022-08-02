#  Define a dictionary call story1, it should have the following keys:
story1 = {
    "start": "The journey of hero began",
    "middle": "It was a long journey",
    "end": "to be continued"
}
# Print the entire dictionary
print(story1)

#Print the type of your dictionary
print(type(story1))

#Print only the keys
print(story1.keys())

#print only the values
print(story1.values())

# print the individual values using the keys (individually, lots of printi commands)
for key, value in story1.items():
    print(value)

#  Now let's add a new key:value pair.
#     # 'hero': yourSuperHero
story1["hero"] = "to be disclosed in the next version"
print(story1)
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# updating list
ft_list[1] = "World!"

# updating tuple
# - convert tuple to list
temp = list(ft_tuple)
# - change list item
temp[1] = "Germany"
# - convert list back to tuple
ft_tuple = tuple(temp)

# updating set
ft_set.remove("tutu!")
ft_set.add("Wolfsburg")

# updating dictionary
ft_dict["Hello"] = "42Wolfsburg!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

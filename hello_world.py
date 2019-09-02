# 1. TASK: print "Hello World"
print("#1: Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Dave"
print("#2a: Hello", name) # with a comma
print("#2b: Hello " + name) # with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
name = "42"
print("#3a: Hello",name) # with a comma
print("#3b: Hello "  + name)# with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fav_food1 = "sushi"
fav_food2 = "pizza"
print("#4a: I love to eat {} and {}.".format(fav_food1, fav_food2)) # with .format()
print(f"#4b: I love to eat {fav_food1} and {fav_food2}.")
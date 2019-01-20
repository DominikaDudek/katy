# What is the difference between is and ==?
# What will be the result of each statement and why?

print True is 1
print 3 == 2 + 1
print (3 * 3) is 9
print 200 + 57 is 257
print 257 is 257
print 1 + 1 is 2
print 890 is 890


# False bo to nie ten sam obiekt, is zwraca true w momencie kiedy wskazujemy na ten sam obiekt
# True bo przyrownanie 3 do 3 , == sprawdza czy to jest rowne sobie, is czy to te same obiekty
#The operators is and is not test for object identity: x is y is true if and only if x and y are the same object. x is not y yields the inverse truth value.
# is checks that the id of two objects are the same.

# is checks to see if they are the same object, not just equal.
# The small ints are probably pointing to the same memory location for space efficiency

#The answer is twofold:

# *** is checks whether 2 things are the same object, not if they re equal
# *** Python caches integers in the range [-5, 256]

# Z oficjalnej dokumentacji: The current implementation keeps an array of integer objects for all integers between -5 and 256,
# when you create an int in that range you actually just get back a reference to the existing object.
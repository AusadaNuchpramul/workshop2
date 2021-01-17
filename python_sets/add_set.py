thisset = {"apple" , "banana", "cherry"}
thisset.add("orange")
print(thisset)
#{'orange', 'cherry', 'apple', 'banana'}

thisset = {"apple" , "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#{'pineapple', 'banana', 'apple', 'mango', 'papaya', 'cherry'}
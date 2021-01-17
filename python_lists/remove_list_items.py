thislist = ["apple" , "banana", "cherry"]
thislist.remove("banana")
print(thislist)	#Output : ["apple" , "cherry"]

thislist = ["apple" , "banana", "cherry"]
thislist.pop(1)
print(thislist)	#Output : ["apple" ,"cherry"]

thislist = ["apple" , "banana", "cherry"]
thislist.pop( )
print(thislist)	#Output : ["apple" , "banana"]

thislist = ["apple" , "banana", "cherry"]
del thislist[0]
print(thislist)	#Output : ["banana", "cherry"]

thislist = ["apple" , "banana", "cherry"]
thislist.clear( )
print(thislist)	#Output : [ ]
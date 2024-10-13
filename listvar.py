# list in python
#shopping item of fruits : apple, banna ,grapes, cherry
shopping_list=['apple', 'banna', 'grapes', 'cherry']
#so the first item is called we zero index or first item of list
shopping_list.append('bluebarries')#it is add value 
#we don't add apple so we exchange it as oranges
shopping_list[0]='oranges'#it is update value
del shopping_list[1]#it is delete method
print(len (shopping_list))      #it is use for how much lenght of my ietem
#combine list together
shopping_list2=['cheese','butter-jam','bread']
print(shopping_list + shopping_list2)
print(shopping_list*2)
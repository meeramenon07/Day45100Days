import os, time
toDoList = []

#def printList():
  #print()
  #for todoItems in toDoList:
    #print(todoItems)
  #print()
  

def add():
  time.sleep(1)
  os.system("clear")
  item = input("what item to add?")
  date=input("Due date ? ")
  priority=input("is it high,medium or low priority?")
  row = [item,date,priority]
  #if priority =="high":
    #toDoList.append(item)
  #elif priority == "medium":
    #toDoList.insert(0,item)
  #elif priority =='low':
  toDoList.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1. All \n 2. View By Priority ")
  if options == "1":
    for row in toDoList:
      for item in row:
        print(item, end=" | ")
    print()
  else:
    priority = input("What priority? ")
    for row in toDoList:
      if priority in row:
        for item in row:
          print(item, end = " | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  check = input("What item do you want to edit? ")
  checked = False
  for row in toDoList:
    if check in row:
      checked = True
  if not checked:
    print("Could not get it")
    return
  for row in toDoList:
    if check in row:
      toDoList.remove(row)
  item = input("item >")
  date = input("date > ")
  priority = input("priority >")
  row = [item,date,priority]
  toDoList.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  check = input("What you want to remove?")
  for row in toDoList:
    if check in row:
      toDoList.remove(row)
    #print("removed")
    #return

while True:
  menu = input("1. Add \n 2. View \n 3. Edit \n 4. Remove > ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()
  #elif menu == "4":
    #remove()
  #else:
    #break
  time.sleep(1)
  os.system("clear")
  
  
  
      
    


  
    
    
                 

#while True:
  #menu = input("ToDo List Manager\nDo you want to view, add, edit, remove or delete the todo list?\n")
  #if menu=="view":
    #printList()
  #elif menu=="add":
    #todoItem = input("What do you want to add?\n").title()
    #toDoList.append(todoItem)
  #elif menu=="remove":
    #todoItem = input("What do you want to remove?\n").title()
    #check = input("Are you sure you want to remove this?\n")
    #if check[0]=="y":
      #if todoItem in toDoList:
        #toDoList.remove(todoItem)
    #else:
      #print("item not deleted")
  #elif menu=="edit":
    #todoItem = input("What do you want to edit?\n").title()
    #edited = input("What do you want to change it to?\n").title()
    #for i in range(0,len(toDoList)):
      #if toDoList[i]== todoItem:
        #toDoList[i]=edited
  #elif menu=="delete":
    #toDoList = []
  #time.sleep(1)
  #os.system('clear')


#Have a menu that asks if you want to add, #view, move or edit a 'to do'.

#If you choose 'add' then the system #should:

#Prompt you to input what the to do is, #when it is due by and the priority (high, #medium or low).
#Add the 'to do' to the list.
#'View' should give two options:

#View all - shows all 'to dos' with a #pretty print.
#View priority - allows you to search for high, medium or low priority and only see matching tasks.
#'Edit' allows you to change any of the information within one of the 'to dos'.

#'Remove' lets you completely remove a 'to do' when it is 'to done'.

#Example:

#🌟Life Organizer🌟#
#Welcome to the life organizer. Do you #want to add, view, edit or remove a to do? > Add#
#What is the task? > Pay teachers more.#
#When is it due by? > 11/01/2022#
#What is the priority? >  High#
#Thanks, this task has been added.#
#Do you want to see the menu again or# quit? > quit.









#Use a separate subroutine for add, view, edit, and remove.

#Clear the console before viewing a new entry.

#Use a while True loop to call the subroutines and display the menu.


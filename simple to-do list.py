#to do list
#display
#add task
#delete task
#exit

tasks=[]



while True:
    print(" welcome to to-do list")
    print("1. View task")
    print("2. Add Task")
    print("3. Delete task")
    print("4. exit")
    
    choice=int(input("choose your operation: "))
    
    if choice == 1:
        if len(tasks)==0:
            
            print("no tasks yet")
        else:
            print("-------------------Tasks Remainng-------------------- ")
            for i in tasks:
                              
                print(i)
                
            
    elif choice==2:
        task_input=input("enter your task: ")
        tasks.append(task_input)
        print("task added succesfully")
    
    elif choice==3:
        if len(tasks)==0:
            
            print("no tasks to delete")
        else:
            task=input("enter the task to delete: ")
            if task in tasks:
                tasks.remove(task)
                print("task deleted")
            else:
                print("task not found")
               
            
    elif choice==4:
        print("goodbye thanks for using")
        break
    else:
        print("invalid input")
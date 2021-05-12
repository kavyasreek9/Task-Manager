
tasks=[]
task_mgr={}
status=['New/To Do','In progress','Completed']

while(1):
    choice=input('1. Add New Task\n2. Change current task status\n3. Show task statuses\n4. Exit\nEnter your choice: ')
    if(choice=='1'):
        new_task=input('Task: ')
        tasks.append(new_task)
        task_mgr[new_task] = status[0]
    elif(choice=='2'):
        print('Choose one task from below')
        print(tasks)
        task=input()
        if task in tasks:
            task_mgr[task] = status[1]
            num=input('To change the task status, enter 1 for In-progress state, enter 2 for Completed state\n')
            if(num=='2'):
                task_mgr[task] = status[2]
            else:
                task_mgr[task] = status[1]
    elif(choice=='3'):
        print(task_mgr)
    else:
        print('Please enter valid option')
        break

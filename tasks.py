import pandas as pd
from tabulate import tabulate
tasks=[]
task_mgr={}
status=[['New/To Do'],['In progress'],['Completed']]
head=['Task','Status']

def add_task():
    new_task=input('Task: ')
    if new_task not in tasks:
        tasks.append(new_task)
        task_mgr[new_task] = status[0]
    else:
        print('Task already present. Please try entering with different name')

def task_index():
    show_task_status()
    print('Choose one task from above:')
    dict_index=dict(enumerate(tasks,start=1))
    task=dict_index[int(input())]
    return task

def edit_task_status():  
    task=task_index()
    if task in tasks:
        task_mgr[task] = status[1]
        num=input('To change the task status, enter 1 for In-progress state, enter 2 for Completed state\n')
        if(num=='2'):
            task_mgr[task] = status[2]
        else:
            task_mgr[task] = status[1]

def show_task_status():
    taskmgr_df = pd.DataFrame(list(task_mgr.items()),columns=head)
    taskmgr_df.index+=1
    print(tabulate(taskmgr_df,headers=head,tablefmt='grid'))

def delete_task():
    task=task_index()
    tasks.remove(task)
    del task_mgr[task]

while(1):
    if(len(tasks)==0):
        choice=input('1. Add New Task\n2. Exit\nEnter your choice: ')
        if(choice=='1'):
            add_task()
        else:
            break
    else:
        choice=input('1. Add New Task\n2. Change current task status\n3. Show task statuses\n4. Remove a task\n5. Exit\nEnter your choice: ')
        if(choice=='1'):
            add_task()
        elif(choice=='2'):
            edit_task_status()
        elif(choice=='3'):
            show_task_status()
        elif(choice=='4'):
            delete_task()
        else:
            print('Please enter valid option')
            break
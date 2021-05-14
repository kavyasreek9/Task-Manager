import pandas as pd
from tabulate import tabulate
tasks=[]
task_mgr={}
status=['New/To Do','In progress','Completed']
priority='Low'
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
    inp=int(input())
    dict_index=dict(enumerate(tasks,start=1))
    if inp not in dict_index:
        print('Please enter valid task ID')
    else:
        task=dict_index[inp]
        return task

def edit_task_status(): 
    task=task_index()
    if task in tasks:
        task_mgr[task] = status[1]
        num=input('To change the task status, enter 1 for In-progress state, enter 2 for Completed state\n')
        if(num=='2'):
            task_mgr[task] = status[2]
        elif(num=='1'):
            task_mgr[task] = status[1]
        else:
            print('Please enter valid option')

def edit_task_priority():
    #taskmgr_df['Priority']=send_task_priority()
    task=task_index()
    if task in tasks:
        num=input('To change the task priority, enter 1 for "High" state, enter 2 for "Medium" state, enter 3 for "Low" state\n')
        if(num=='1'):
            priority='High'
        elif(num=='2'):
            priority='Medium'
        elif(num=='3'):
            priority='Low'
        else:
            print('Please enter valid option')

# def send_task_priority():
#     taskmgr_df['Priority']='Low'
#     return taskmgr_df['Priority']

def show_task_status():
    taskmgr_df = pd.DataFrame(list(task_mgr.items()),columns=head)
    taskmgr_df.index+=1
    taskmgr_df['Priority']=priority
    print(tabulate(taskmgr_df,tablefmt='fancy_grid',headers=['Task','Status','Priority']))

def delete_task():
    task=task_index()
    if task in tasks:
        tasks.remove(task)
        del task_mgr[task]

while(1):
    
    if(len(tasks)==0):
        choice=input('1. Add New Task\n2. Exit\nEnter your choice: ')
        if(choice=='1'):
            add_task()
        elif(choice=='2'):
            break
        else:
            print('Please enter valid choice')
    else:
        choice=input('1. Add New Task\n2. Change Task Status\n3. Change Task Priority\n4. Show Task Status\n5. Remove a Task\n6. Exit\nEnter your choice: ')
        if(choice=='1'):
            add_task()
        elif(choice=='2'):
            edit_task_status()
        elif(choice=='3'):
            edit_task_priority()
        elif(choice=='4'):
            show_task_status()
        elif(choice=='5'):
            delete_task()
        else:
            print('Please enter valid option')
            break
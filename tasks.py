from tabulate import tabulate
import pandas as pd
tasks=[]
priority={0:'Low',1:'Medium',2:'High'}
task_mgr=[]
To_Do=[]
In_Progress=[]
Completed=[]

def add_task():
    task=input('Enter input task:\n')
    if task in To_Do:
        print('Task Already Present')
    else:
        tasks.append(task)
        To_Do.append(task)
        task_mgr.append([task,'-','-',priority[0]])

def task_index():
    show_task_status()
    print('Choose one task from above:')
    inp=int(input())
    index=dict(enumerate(tasks,start=1))
    if inp not in index:
        print('Please enter valid task ID')
    else:
        task=index[inp]
        return task

def edit_task_status(): 
    task=task_index()
    index=tasks.index(task)
    if task in To_Do:
        num=int(input('To change the task status, enter 1 for In-progress state, enter 2 for Completed state\n'))
        if(num==1):
            To_Do.remove(task)
            In_Progress.append(task)
            for l in task_mgr:
                if task in l:
                    priority_new=l[-1]
                    print('Type of is: ',type(priority_new))
                    l=['-',task,'-',priority_new]
                    task_mgr[index]=l
        elif(num==2):
            To_Do.remove(task)
            Completed.append(task)
            for l in task_mgr:
                if task in l:
                    priority_new=l[-1]
                    l=['-','-',task,priority_new]
                    task_mgr[index]=l
        else:
            print('Please enter valid option')
    elif task in In_Progress:
        num=int(input('To change the task status, enter 1 for Completed state\n'))
        if(num==1):
            In_Progress.remove(task)
            Completed.append(task)
            for l in task_mgr:
                if task in l:
                    priority_new=l[-1]
                    l=['-','-',task,priority_new]
                    task_mgr[index]=l
        else:
            print('Please enter valid option')
    elif task in Completed:
        print('Task is Completed')

def edit_priority(task,num):
    for l in task_mgr:
            if task in l:
                if(num==0):
                    priority_new='Low'
                    l[-1]=priority_new
                elif(num==1):
                    priority_new='Medium'
                    l[-1]=priority_new
                elif(num==2):
                    priority_new='High'
                    l[-1]=priority_new
                else:
                    print('Please enter valid option')

def edit_task_priority():
    task=task_index()
    priority_new=[l[-1] for l in task_mgr if task in l]
    if(priority_new==['Low']):
        num=int(input('To change the task priority, enter 1 for Medium Priority, enter 2 for High Priority\n'))
        edit_priority(task,num)
    elif(priority_new==['Medium']):
        num=int(input('To change the task priority, enter 0 for Low Priority, enter 2 for High Priority\n'))
        edit_priority(task,num)
    elif(priority_new==['High']):
        num=int(input('To change the task priority, enter 0 for Low Priority, enter 1 for Medium Priority\n'))
        edit_priority(task,num)
    else:
        print('Please enter valid option')

def remove_sub_code(task):
    for l in task_mgr:
            if task in l:
                task_mgr.remove(l)

def remove_task():
    task=task_index()
    tasks.remove(task)
    if task in To_Do:
        To_Do.remove(task)
        remove_sub_code(task)
    elif task in In_Progress:
        In_Progress.remove(task)
        remove_sub_code(task)
    elif task in Completed:
        Completed.remove(task)
        remove_sub_code(task)
    else:
        print('Please enter valid option')
    
def show_task_status():
    df=pd.DataFrame(task_mgr,columns=['TODO','In-Progress','Completed','Priority'])
    df.index+=1
    df.sort_values(by='Priority',inplace=True)
    print(tabulate(df,tablefmt='fancy_grid',headers=['TODO','In-Progress','Completed','Priority']))

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
        choice=input('1. Add New Task\n2. Change Task Status\n3. Change Task Priority\n4. Remove a Task\n5. Show Task Status\n6. Exit\nEnter your choice: ')
        if(choice=='1'):
            add_task()
        elif(choice=='2'):
            edit_task_status()
        elif(choice=='3'):
            edit_task_priority()
        elif(choice=='4'):
            remove_task()
        elif(choice=='5'):
            show_task_status()
        else:
            print('Please enter valid option')
            break
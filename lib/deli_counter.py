katz_deli = []

def line(queue):
    if len(queue)==0:
        print("The line is currently empty.")
    else:
        msg = " ".join([str(queue.index(name)+1) + '. '+ name for name in queue])
        print(f"The line is currently: {msg}")
        

def take_a_number(queue,name):
    queue.append(name)
    print(f'Welcome, {name}. You are number {len(queue)} in line.')

def  now_serving(queue):
    if len(queue)==0:
        print('There is nobody waiting to be served!')
    else:
        print(f'Currently serving {queue[0]}.')
        del(queue[0])



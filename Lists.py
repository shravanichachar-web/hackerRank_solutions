if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        # Read the command and split it into a list of words
        command = input().split()
        
        # The first word is always the operation name
        operation = command[0]
        
        # Perform the corresponding list operation
        if operation == 'insert':
            my_list.insert(int(command[1]), int(command[2]))
        elif operation == 'print':
            print(my_list)
        elif operation == 'remove':
            my_list.remove(int(command[1]))
        elif operation == 'append':
            my_list.append(int(command[1]))
        elif operation == 'sort':
            my_list.sort()
        elif operation == 'pop':
            my_list.pop()
        elif operation == 'reverse':
            my_list.reverse()

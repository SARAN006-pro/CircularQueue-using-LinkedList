class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
class CircularQueue:
    def __init__(self) :
        self.front=None
        self.rear=None
    
    def enqueue(self,data):
        newnode=Node(data)
        if not self.front and not self.rear:
            self.front=self.rear=newnode
            self.rear.next=self.front
        else:
            self.rear.next=newnode
            self.rear=newnode
            self.rear.next=self.front
                     
    def dequeue(self):
        if not self.front and not self.rear:
            print("Queue is Empty")
        elif self.front==self.rear:
            print(f"{self.front.data}is deleted.")
            self.front=self.rear=None
        else:
            print(f"{self.front.data}is deleted.")
            self.front=self.front.next
            self.rear.next=self.front
            
    def display(self):
        if not self.front and not self.rear:
            print("Queue is Empty")
        else:
            temp=self.front
            print(f"Elements i Queue: ")
            while temp.next!=self.front:
                print(temp.data,end=" ")
                temp=temp.next
            print(temp.data)
obj=CircularQueue()
while True:
    print("Circular Queue using linked list: ")
    choice=int(input("Enter your choice: "))
    if (choice==1):
        data = int(input())
        obj.enqueue(data)
    elif(choice==2):
        obj.dequeue()
    elif(choice==3):
        obj.display()
    elif(choice==4):
        break    
    else:
        print("Invalid choice")
            
        
            
            
        


        

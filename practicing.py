# Linked list

# Node class
"""With the basic implementation of setting the next node, getting the next node"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node
    
    def __repr__(self):
        return str(self.value)

# Linked list class
class Linked_list:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()

        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
            
        return string_list
    
    def remove_node(self, value):
        current_node = self.get_head_node()

        if current_node.get_value() == value:
            self.head_node = current_node.get_next_node()

        else:
            while current_node:
                next_node = current_node.get_next_node()

                if next_node.get_value() == value:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node   

# ll = Linked_list(20)
# ll.insert_beginning(11)
# ll.insert_beginning(21)
# ll.insert_beginning(15)

# ll.remove_node(15)


# print(ll.get_head_node())
# print(ll.stringify_list())

"""QUEUES"""

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    
    def enqueue(self, new_value):
        if self.has_space():
            item_to_add = Node(new_value)
            print("Adding " + str(item_to_add.get_value()))

            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry no more room, we don't want a queue overflow!!")
    
    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print("Removing " + str(item_to_remove.get_value()))

            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Queue is empty and we don't want a queue underflow")


    def get_size(self):
        return self.size
    
    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()
    
    def is_empty(self):
        if self.get_size() == 0:
            return True
        else:
            return False 

    def peek(self):
        if self.is_empty():
            print("There is nothing to see here")
        else:
            return self.head.get_value()


# q = Queue(10)

# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)

# print(q.has_space())
# q.dequeue()
# print(q.peek())

"""STACKS"""

class Stack:
    def __init__(self, max_size=None):
        self.max_size = max_size
        self.top_item = None
        self.size = 0
    
    def push(self, new_value):
        if self.has_space():
            value_to_add = Node(new_value)
            print("Adding: " + str(value_to_add.get_value()))

            if self.is_empty():
                self.top_item = value_to_add
            else:
                value_to_add.set_next_node(self.top_item)
                self.top_item = value_to_add
            self.size += 1
        else:
            print("There is no space to add {} into the stack, we don't want a stack overflow!".format(new_value))
    
    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()

            self.size -= 1

            return item_to_remove.get_value()
        else:
            print("Stack is empty, we dont want a stack underflow!!")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        else:
            print("Nothing to see here!, have you tried the push function?")

    def get_size(self):
        return self.size
    
    def is_empty(self):
        if self.get_size() == 0:
            return True
        else:
            return False
    
    def has_space(self):
        return self.max_size > self.get_size()

# s = Stack(4)
# s.push(20)
# s.push(25)
# s.push(26)
# s.push(30)

# print(s.peek())

# s.pop()

# print(s.peek())

# s.push(50)
# s.push(400)





































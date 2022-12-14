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








































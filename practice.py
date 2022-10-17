
from Stacks import Stack

N = 6

my_stack = Stack(N)
my_stack.push("Australia")
my_stack.push("India")
my_stack.push("Costa Rica")
my_stack.push("Peru")
my_stack.push("Ghana")
my_stack.push("Indonesia")


while not my_stack.is_empty():

  first_value_added_to_stack = my_stack.pop()
  print(first_value_added_to_stack)

print(first_value_added_to_stack)
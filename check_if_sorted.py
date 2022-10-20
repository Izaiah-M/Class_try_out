test_list = [1, 4, 5, 8, 10]

red_flag = 0
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i - 1]):
        red_flag = 1
    i += 1
      
# printing result
if (not red_flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")
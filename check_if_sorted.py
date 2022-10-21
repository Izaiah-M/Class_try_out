test_list = [1, 4, 8, 5, 10]

red_flag = False
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i - 1]):
        red_flag = True
    i += 1
      
# printing result
if (not red_flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")
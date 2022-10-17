
my_list = [
    ["A94160", "Mukisa Isaiah", "S21B23/007"],
    ["A94161", "Nkata Joshua", "S21B23/008"],
    ["A96447", "Muganga Charles", "J22B23/032"],
    ["A95681", "Najjoba Tracy", "S21B23/016"],
    ["A96447", "Katukunda Rochelle", "S21B23/034"],
    ["Ukraine", "380"],
    ["Tanzania", "255"],
    ["Saint Vincent and the Grenadines", "1-784"],
    ["Afghanistan", "93"],
    ["Fiji", "679"],
    ["Bahamas", "1-242"],
    
]

def search_information(list, l):
    for i in list:
        for j in i:
            if l == j:
                return i
            
            
    return None

print("Value found: " + str(search_information(my_list, "Tanzania")))



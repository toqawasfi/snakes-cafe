def print_menu():
    print("***************************************\n**     welcome to the Snakes Cafe!   **\n**     Please see our menu below.    ** \n**                                   **\n** To quit at any time, type  'quit' **\n***************************************\nAppetizers\n----------\nwings\ncookies\nspring Rolls\n\nEntrees\n-------\nSalmon\nSteak\nMeat Torando\nA Literal Garden\n\nDesserts\n--------\nIce Cream\nCake\npie\n\nDrinks\n------\nCoffee\nTea\nUnicorn Tears")
    print("***********************************\n** What would you like to order? **\n***********************************")

print_menu()

menu=["wings","cookies","spring rolls","salmon","steak","meat torando","a literal garden","ice cream","cake","pie","coffee","tea","unicorn tears"]

def take_order():
    list_of_true_item=[]
    dic_key_valye={}
    keys = ["wings","cookies","spring rolls","salmon","steak","meat torando","a literal garden","ice cream","cake","pie","coffee","tea","unicorn tears"]
    values = []
    
    while True:
        order=input("> ")
        count = 0
        if order.lower() == "quit" :
            break
        if order.lower() in menu:
            list_of_true_item.append(order.lower())
            if order.lower() in list_of_true_item:
                for z in range(len(list_of_true_item)) :
                    if order.lower() == list_of_true_item[z]:
                        count+=1
                        for i in range(len(keys)):
                            if list_of_true_item[z] == keys[i]:
                                dic_key_valye[keys[i]] = count
                list_of_Values=[]
                list_of_keys=[]
                for keyss in dic_key_valye.keys():
                    list_of_keys.append(keyss)
                for values in dic_key_valye.values():
                    list_of_Values.append(values)
                for l in range(len(dic_key_valye)):
                    Final_keys=list_of_keys[l]
                    Final_values=list_of_Values[l]
                    print(f"** {Final_values} order of {Final_keys} have been added to your meal **")
            else:
                count+=1
                print(f"** {count} order of {order} have been added to your meal **")
        elif order.lower() not in menu:
            print(f"sorry, no {order} in our menu")
    print(f"you order is: {dic_key_valye}")
take_order()
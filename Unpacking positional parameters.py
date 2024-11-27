def print_params(a = 1, b = 'строка', c = True) :
    print(a, b, c)
values_list = [7, 6, 5]
values_dict = {"a": 2, "b": True, "c": "Строчка"}
values_list_2 = [93, 55]
values_dict_2 = {"c": True}


#print_params()
#print_params(a = 2)
#print_params(a = "строка", b = 1)
#print_params(b = 25)
#print_params(c = [1,2,3])
#print_params(*values_list)
#print_params(**values_dict)
#print_params(*values_list_2, **values_dict_2)
print_params(*values_list_2, 42)



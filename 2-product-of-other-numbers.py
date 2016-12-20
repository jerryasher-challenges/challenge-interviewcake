# https://www.interviewcake.com/question/python/product-of-other-numbers


def get_products_of_all_ints_except_at_index(l):
    prod = 1
    for n in l:
        prod *= n

    prods = []
    for i in range(len(l)):
        if l[i] != 0:
            prods.append(int(prod / l[i]))
        else:
            prods.append(int(prod))

    return prods

print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
print(get_products_of_all_ints_except_at_index([1, 2, 6, 5, 9]))
print(get_products_of_all_ints_except_at_index([]))
print(get_products_of_all_ints_except_at_index([5]))
print(get_products_of_all_ints_except_at_index([0]))
print(get_products_of_all_ints_except_at_index([0, 0]))
print(get_products_of_all_ints_except_at_index([0, 0, 0]))

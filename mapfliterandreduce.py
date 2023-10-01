# map function
# practice lambda functions first

import functools
store = [
    ("shoes", 300),
    ("pants", 50),
    ("socks", 3890),
    ("caps", 358),
    ("hats", 377),
    ("glasses", 673),
    ("jokey", 839),
    ("rings", 390)

]

# increase the sales prices by 10%


def price(item): return (item[0], item[1]+item[1]*0.01)


new_prices = map(price, store)

# for i in new_prices:
# print(list(i))

# returns:
# ['shoes', 303.0]
# ['pants', 50.5]
# ['socks', 3.03]

# filter()
# get items from store whose character length <5


def length(x): return (len(x[0]) < 5)


new_items = filter(length, store)

# for i in new_items:
#     # print(list(i))

# returns
# ['caps', 358]
# ['hats', 377]

# get all items whose price is between R160 and R500


def price_3(x): return (x[1] >= 160 and x[1] <= 500)


all_items = filter(price_3, store)

# for i in all_items:
#     print(list(i))
# returns
# ['shoes', 300]
# ['caps', 358]
# ['hats', 377]
# ['rings', 390]


# reduce function
letters = ["abcdefghijklmnopqrstuvwxyz"]
letters = letters.pop()
# pop splits the items in a list
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(list(letters))
# string concatenation
def reduced(x, y): return x+y


new_reduced_list = functools.reduce(reduced, letters)
print(new_reduced_list)
# returns original letters
word = ["HELLO", "WORLD"]
print(word[0:1].pop())

list = ["apple", "banana", "cory"]
dict = {"apple":1, "banana":2, "cory":3}
number = []
def calculate_hand(*args):
    count = 0
    for f in args:
        count += int(dict.get(f))
    number.append(count)

for f in list:
    calculate_hand(f)
print(number)
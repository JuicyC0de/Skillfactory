def my_ii_groot(say):
    if say:
        return 'I am Groot'


while True:
    quest = input('Groot listening you: ')
    print(my_ii_groot(quest))
    if not quest:
        break

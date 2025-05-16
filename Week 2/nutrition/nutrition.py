#Creating main function
def main():

    #taking input
    text = input("Item: ").strip().lower()

    data = {
            'apple':'130',
            'avocado':'50',
            'banana':'110',
            'cantaloupe':'50',
            'grapefruit':'60',
            'grape':'90',
            'honeydew':'50',
            'kiwifruit':'90',
            'lemon':'15',
            'lime':'20',
            'nectarine':'60',
            'orange':'80',
            'peach':'60',
            'pear':'100',
            'pineapple':'50',
            'plums':'70',
            'strawberries':'50',
            'sweet cherries':'100',
            'tangerine':'50',
            'watermelon':'80'

    }
    for i in data:
        if text == i:
            print(f'Calories: {data[i]}')

main()

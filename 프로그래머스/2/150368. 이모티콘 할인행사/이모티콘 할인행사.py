from itertools import product
def solution(users, emoticons):
    rates = [10, 20, 30, 40]
    emo_size = len(emoticons)
    answer = [-1, -1]
    rates_product = list(product(rates, repeat = emo_size))
    for item in rates_product:
        sale_price = []
        for i in range(emo_size):
            sale_price.append([emoticons[i] // 100 * (100-item[i]), item[i]])
        
        plus_count = 0
        price_count = 0
        for user in users:
            buy_price = 0
            for sale in sale_price:
                if sale[1] >= user[0]:
                    buy_price += sale[0]

            if buy_price >= user[1]:
                plus_count += 1
            else:
                price_count += buy_price

        if plus_count >= answer[0]:
            if plus_count == answer[0]:
                answer = [plus_count, max(answer[1], price_count)]
            else:
                answer = [plus_count, price_count]
        
                
    return answer
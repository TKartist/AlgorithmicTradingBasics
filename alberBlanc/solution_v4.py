from csv import reader


def calculate_optimal_profit():
    with open("data_v2.csv", "r") as file:
        csv = reader(file)
        next(csv, None)
        buys = []
        myBalance = 0
        for trade in csv:
            volume = int(trade[2])
            price = float(trade[1])
            buyCount = 0
            if volume > 0:  # buy transaction
                buys.append((volume, price, 0))
            else:  # sell transaction
                sellQuantity = abs(volume)
                buys.sort(reverse=True, key=lambda t: (-t[2], t[1]))
                counter = len(buys) - 1
                buyCount = 0
                while (
                    sellQuantity > 0 and counter >= 0
                ):  # loop while there is something to sell and possible buy candidates
                    soldQuantity = min(sellQuantity, buys[counter][0])
                    profit = (price - buys[counter][1]) * soldQuantity
                    if (
                        buys[counter][0] > 0
                        and buys[counter][2] > 0
                        and (buys[counter][2] + profit) > 0
                    ):
                        buys[counter] = (
                            buys[counter][0] - soldQuantity,
                            buys[counter][1],
                            buys[counter][2] + profit,
                        )
                        sellQuantity -= soldQuantity
                        if buys[counter][0] == 0:
                            buyCount += 1
                            myBalance += buys[counter][2]
                        counter -= 1
                        continue
                    if profit <= 0:
                        break
                    if profit > 0:
                        sellQuantity -= soldQuantity
                        buys[counter] = (
                            buys[counter][0] - soldQuantity,
                            buys[counter][1],
                            soldQuantity * (price - buys[counter][1]),
                        )
                        if buys[counter][0] == 0:
                            buyCount += 1
                            myBalance += profit
                        counter -= 1
                        continue
            for i in range(buyCount):
                buys.pop()
        print(myBalance)
        print(buys[len(buys) - 1])
        s = 0
        for i in range(len(buys)):
            if buys[i][2] > 0:
                s += buys[i][0]
        print(s)


calculate_optimal_profit()

from csv import reader


# changes owned position info, how much made, how much left
def updateTuple(sold, profit, originalTuple):
    return (originalTuple[0] - sold, originalTuple[1], originalTuple[2] + profit)


def calculate_optimal_profit():
    with open("data_v2.csv", "r") as file:
        csv = reader(file)
        next(csv, None)
        buys = []
        transactions = []
        maxPrice = 0
        currentPosition = 0
        for trade in csv:
            volume = int(trade[2])
            price = float(trade[1])
            # counts how many buy operation to pop
            buyCount = 0
            counter = len(buys) - 1
            if currentPosition <= 0 or currentPosition > 100000:
                print(buys)
            if volume > 0:  # buy transaction
                # only keep the best (cheapest) 100'000 positions
                if (currentPosition + volume) <= 100000:
                    buys.append((volume, price, 0))
                    currentPosition += volume
                    if price > maxPrice:
                        maxPrice = price
                else:
                    if maxPrice > price:
                        buyCopy = buys.copy()
                        buys.sort(key=lambda t: (-t[2], t[1]))
                        while counter >= 0:
                            if buys[counter][1] < price:
                                buys = buyCopy
                                break
                            popped = buys.pop()
                            currentPosition -= popped[0]
                            counter -= 1
                            if (currentPosition + volume) < 100000:
                                maxPrice = buys[len(buys) - 1][1]
                                buys.append((volume, price, 0))
                                currentPosition += volume
                                break
                    else:
                        continue
            else:  # sell transaction
                sellQuantity = abs(volume)
                # sort buys in descending order of price so it is easier to pop buys with lower prices
                # sort prioritising leftover transactions that aren't complete yet
                buys.sort(reverse=True, key=lambda t: (-t[2], t[1]))
                sold = False

                # loop while there is something to sell and possible buy candidates
                while sellQuantity > 0 and counter >= 0:
                    soldQuantity = min(sellQuantity, buys[counter][0])
                    profit = (price - buys[counter][1]) * soldQuantity
                    # selling if leftover transaction's overall is a profit
                    # or if profit is above 0
                    # or if some quantity of sell transaction were sold and there
                    # is something left to sell
                    if (
                        (
                            buys[counter][0] > 0
                            and buys[counter][2] > 0
                            and (buys[counter][2] + profit) > 0
                        )
                        or profit > 0
                        or sold
                    ):
                        buys[counter] = updateTuple(soldQuantity, profit, buys[counter])
                        sellQuantity -= soldQuantity
                        currentPosition -= soldQuantity
                        if buys[counter][0] == 0:
                            buyCount += 1
                        counter -= 1
                        sold = True
                        continue
                    # if -ve profit or no leftovers ignore sell or none of it was sold
                    break
            # pop sold out (valid) buys and put it into transactions
            for i in range(buyCount):
                transactions.append(buys.pop())
        profit = 0
        for transaction in transactions:
            profit += transaction[2]
        print("Total profit in case of optimal strategy is: ", "{0:.2f}".format(profit))


calculate_optimal_profit()

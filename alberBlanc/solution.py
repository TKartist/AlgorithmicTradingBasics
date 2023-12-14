from csv import reader
import matplotlib.pyplot as py
import math

# # Average price fluctuation has a higher weight on prediction if the cycle is more recent
# # weight is : 0.4, 0.4 * 0.6, 0.4 * 0.6 * 0.6 ...
# # sum of all weights will add up to 1 => naturally to avoid absurd estimations

# def estimatePriceIncrease(prices, cycleLength):
#     size = len(prices)
#     counter = 0
#     weight = 0
#     increase = 0
#     estimate = 0
#     for i in range(size - 1, 1, -1): # access price from latest to oldest
#         if counter == cycleLength: # getting avg price increase over 'cycleLength' timeframes
#             estimate += increase / cycleLength * 0.4 * pow(0.6, weight) # get avg price change in cycle and apply its weight
#             weight += 1
#             counter = 0
#             increase = 0
#         increase += prices[i] / prices[i - 1] # sum all price changes
#         counter += 1
#     if counter > 0: # in case some data were left out
#         estimate += increase / counter * 0.4 * pow(0.6, weight)
#     return estimate


# def calculate_profit(filpath, current_position):
#     beginning_position = current_position
#     with open(filpath, 'r') as read_csv:
#         myBalance = 0
#         csvreader = reader(read_csv)
#         next(csvreader, None) # ignores the header
#         prices = [] # list to save all the prices
#         for trade in csvreader:
#             trade_volume = int(trade[2])
#             price = float(trade[1])
#             prices.append(price)
#             if trade_volume > 0:
#                 actual_trade = min(trade_volume, 100000 - current_position)
#             else:
#                 actual_trade = min(abs(trade_volume), current_position) * -1
#             current_position += actual_trade
#             myBalance -= price * actual_trade
#         # I am assuming, 100 time frames is an enough quantity of time frames to
#         # provide us some information about the price trend
#         cycleLength = 100
#         # We estimate the price increase in the next time frame from the recorded prices and
#         # cycle length
#         predictedIdealPriceChange = estimatePriceIncrease(prices, cycleLength)
#     print("remaining positions: ", current_position)
#     print("balance after recorded transactions: ", myBalance)
#     predictedPrice = predictedIdealPriceChange * prices[len(prices) - 1] # latest recorded price times the estimated change
#     print("most recent known price is: ", prices[len(prices) - 1])
#     print("predicted price in the next time frame is: ", predictedPrice)
#     # Assuming we sell all the remaining positions in this time frame with a estimated price
#     # of price from past data
#     total_profit = current_position * predictedPrice + myBalance
#     print("total profit ignoring the initial capital used to buy the 100'000 positions: ", total_profit)

# calculate_profit("data_v2.csv", 100000)


def priceTrend():
    with open("data_v2.csv", "r") as read_csv:
        csvreader = reader(read_csv)
        next(csvreader, None)  # ignores the header
        prices = []  # list to save all the prices
        indexes = []
        for trade in csvreader:
            prices.append(float(trade[1]))
            indexes.append(int(trade[0]))

    py.plot(indexes, prices)
    py.ylabel("price")
    py.xlabel("timeframe")
    py.show()


# priceTrend()

# priceTrend()
# -ve sell stat
# +ve buy stat
# we sell when the sell price is higher than our buy price.
# we sell no matter what if we held that position for more than certain time frames
# we buy when the price is below the average of past certain prices
# if the price is on a downward trend we reduce the buy to minimum
# stop loss maybe (if price drops drastically from prev price, release)
# we want to keep buying and selling with preferably with no losses and we don't want to keep the position for too long


# def buyNow(prices):
#     limit = min(abs(len(prices) - 21), 0)
#     sum = 0
#     for i in range(len(prices) - 2, limit - 1, -1):
#         sum += prices[i]
#     cycleAvgPrice = sum / 20
#     if prices[len(prices) - 1] < cycleAvgPrice:
#         if prices[limit] * 0.999 > prices[len(prices) - 1]:
#             return False
#         return True
#     return False


# def calculate_ideal_profit():
#     with open("data_v2.csv", "r") as csv:
#         csvreader = reader(csv)
#         next(csvreader, None)  # ignores the header
#         current_position = 0
#         myBalance = 0
#         averageBuyPrice = 0
#         urgency = 0  # higher urgency => reduce standard for sell
#         prices = []
#         buys = 0
#         sells = 0
#         for trade in csvreader:
#             volume = int(trade[2])
#             price = float(trade[1])
#             prices.append(price)
#             urgency += 1
#             if volume > 0:
#                 actual_buy = min(volume, 100000 - current_position)
#                 if buyNow(prices) and current_position == 0:
#                     buys += 1
#                     current_position += actual_buy
#                     averageBuyPrice = price
#                     myBalance -= actual_buy * averageBuyPrice
#                     continue
#                 if buyNow(prices):
#                     buys += 1
#                     circulatingFund = current_position * averageBuyPrice
#                     updatedCirculatingFund = circulatingFund + actual_buy * price
#                     current_position += actual_buy
#                     myBalance -= actual_buy * price
#                     averageBuyPrice = updatedCirculatingFund / current_position
#                     # print(averageBuyPrice)
#             else:
#                 actual_sell = min(abs(volume), current_position)
#                 if (
#                     averageBuyPrice < price
#                     or (urgency > 5 and price == averageBuyPrice)
#                     or urgency > 10
#                     or price < (averageBuyPrice * 0.999)
#                 ):
#                     sells += 1
#                     current_position -= actual_sell
#                     myBalance += price * actual_sell
#                     if current_position == 0:
#                         averageBuyPrice = 0
#                         urgency = 0
#         print(current_position)
#         print(myBalance)
#         print(buys)
#         print(sells)


# calculate_ideal_profit()

# trial 1 : average 10 million loss, so one strategy is definitely not enough and
# we would have to implement different strategy according to the volatility


def movingAverage(
    prices,
):  # check if the current price is above moving average standard(? => don't know if right term)
    s = sum(prices)
    cycleAvgPrice = s / 100  # average price of recent 100 time frames
    if prices[len(prices) - 1] < cycleAvgPrice:
        return True
    return False


def volatilityCalculation(prices):
    sum = prices[0]
    varianceSum = 0
    trend = 0
    for i in range(1, len(prices)):
        sum += prices[i]
        trend += (
            prices[i] - prices[i - 1]
        )  # +ve mean increase trend in price, -ve vice versa
    cycleAverage = sum / len(prices)  # average price
    for i in range(0, len(prices)):
        varianceSum += pow(
            (prices[i] - cycleAverage), 2
        )  # sum of dif between price and average squared
    stdDeviation = math.sqrt(varianceSum / len(prices))  # stand deviation calculation
    volatility = (
        stdDeviation / cycleAverage
    )  # standard deviation in relation to cycleAverage normalized to 1
    return volatility, trend


def calculate_ideal_profit():
    with open("data_v2.csv", "r") as csv:
        csvreader = reader(csv)
        next(csvreader, None)  # ignores the header
        current_position = 0  # amount of positions owned
        myBalance = 0
        lifetime = 0  # after certain lifetime => sell regardless of price
        prices = []
        counter = 0
        for trade in csvreader:
            counter += 1
            volume = int(trade[2])
            price = float(trade[1])
            prices.append(price)
            recent = prices[
                max(len(prices) - 100, 0) : len(prices)
            ]  # most recent at most 100 prices
            volatility, trend = volatilityCalculation(recent)
            if counter > 54500:  # close to closing time so dump
                if volume < 0:
                    sell = min(abs(volume), current_position)
                    current_position -= sell
                    myBalance += sell * price
                continue
            # In case of high volatility
            if volatility > 0.005:
                # sell when price is rising or dropping but volatility is too high
                if (trend > 0 or volatility > 0.01) and volume < 0:
                    sell = min(abs(volume), current_position)  # can't sell if 0
                    current_position -= sell
                    myBalance += sell * price
                if trend < 0 and volume > 0:
                    buy = min(
                        volume, 100000 - current_position
                    )  # can't own more than 100k
                    current_position += buy
                    myBalance -= buy * price
                continue
            # In case of low volatility
            lifetime += 1
            belowMA = movingAverage(recent)
            if volume > 0:
                actual_buy = min(volume, 100000 - current_position)
                if belowMA:  # buy if below MA line
                    current_position += actual_buy
                    myBalance -= actual_buy * price
                continue
            sell = min(abs(volume), current_position)
            #
            if (not belowMA) or lifetime > 3:  # sell if above MA line
                current_position -= sell
                myBalance += price * sell
                if current_position == 0:
                    lifetime = 0
        print(current_position, "remaining positions")
        print(myBalance, "$ profitted using a so called 'ideal' algo")


calculate_ideal_profit()

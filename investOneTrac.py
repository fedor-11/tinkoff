import csv


def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    i = 0
    prices = []
    time = []
    data = []
    for row in reader:
        if i >= 1:
            prices.append(float(row[-1]))
            time.append(row[-2][:4])
            data.append(row[-3])
        i += 1
    l = len(prices)
    i = 0
    max_dif = 0
    index_max = 0
    index_by = 0
    index_sell = 0
    for i in range(l-1):
        if i >= index_max:
            index_max = l - 1 - prices[::-1].index(max(prices[i+1:]))
            if max_dif < prices[index_max] - prices[i]:
                max_dif = prices[index_max] - prices[i]
                index_by = i
                index_sell = index_max
        else:
            if max_dif < prices[index_max] - prices[i]:
                max_dif = prices[index_max] - prices[i]
                index_by = i
                index_sell = index_max
    print(f"by: {data[index_by]} at {time[index_by]}; sell: {data[index_sell]} at {time[index_sell]}")
    print(f"максмальный доход: {max_dif}")

if __name__ == "__main__":
    csv_path = "new.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)

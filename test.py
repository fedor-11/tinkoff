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
    s_max_dif = 0
    index_max = 0
    index_by = 0
    list_index_by = []
    list_index_sell = []
    index_max = l - 1 - prices[::-1].index(max(prices[index_by + 1:]))
    for i in range(l-1):
        if i == index_max:
            s_max_dif += prices[index_max] - prices[index_by]
            list_index_by.append(index_by)
            list_index_sell.append(index_max)
            index_by = index_max + 1
            index_max = l - 1 - prices[::-1].index(max(prices[index_by + 1:]))
        else:
            if prices[i] < prices[index_by]:
                index_by = i

    for j in range(len(list_index_by)):
        print(f"by: {data[list_index_by[j]]} at {time[list_index_by[j]]}; sell: {data[list_index_sell[j]]} at {time[list_index_sell[j]]}")
    print(f"максмальный доход: {s_max_dif}")

if __name__ == "__main__":
    csv_path = "new.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)

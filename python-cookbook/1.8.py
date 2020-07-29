# 1.8 => CALCULATION ON DICTIONARY

# discussion: zip is useful to create tuples from dictionay for corresponding indexed values

stock_prices = {
        'ACME': 3488,
        'HP': 566,
        'FB': 67
}

def get_company_with_max_stock():

    # for dictionary passed value is the 'key' in the dictionary
    # discussion: problem here is the extra look up which is necessary if the value required is the price, not the company name

    return stock_prices[max(stock_prices, key=lambda key: stock_prices[key])]

def get_company_with_max_stock_using_zip():
    return max(zip(stock_prices.values(), stock_prices.keys()))[0]

def zipped():

    # 'zip' returns iterator
    return list(zip(stock_prices.values(), stock_prices.keys()))

print(get_company_with_max_stock())
print(get_company_with_max_stock_using_zip())
print(zipped())


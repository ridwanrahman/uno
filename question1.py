def is_valid_sale(price, item_type, item_quantity, sale_total):
    get_price_of_item = price.get(item_type)
    if get_price_of_item is None:
        '''
        this check can be ignored as all input types
        are assumed to be correct
        '''
        return False
    get_price_of_one = sale_total/item_quantity
    is_price_correct = (get_price_of_one == get_price_of_item)
    return is_price_correct

def flag_invalid_sales(price, sales):
    invalid_sales = []
    for sale in sales:
        item_type = sale[0]
        item_quantity = sale[1]
        item_price = sale[2]
        is_price_correct = is_valid_sale(price, item_type, item_quantity, item_price)
        if not is_price_correct:
            invalid_sales.append(sale)

    return invalid_sales


def generate_sales_report(price, sales):
    new_dict = {}
    invalid_sales = flag_invalid_sales(price, sales)
    for sale in sales:
        item_counter = 0
        errors = 0
        if sale in invalid_sales:
            continue
            # new_dict[sale[0]] = [item_quantity, item_counter, avg_price]
        else:
            if sale[0] not in new_dict:
                item_quantity = sale[1]
                item_counter += 1
                avg_price = sale[2] / item_quantity
                new_dict[sale[0]] = [item_quantity, item_counter, avg_price, errors]
            else:
                item_in_new_dict = new_dict.get(sale[0])
                item_in_new_dict[0] = item_in_new_dict[0] + sale[1]
                item_counter = item_in_new_dict[1] + 1
                item_in_new_dict[1] = item_counter
                avg_price = (sale[2] + item_in_new_dict[1]) / item_counter
                item_in_new_dict[2] = avg_price
                item_in_new_dict[3] = item_in_new_dict[3] + errors
    print(new_dict)

def main():
    price = {"apple": 2.0, "orange": 3.0, "tangerine": 4.0}
    sales = [
        ["apple", 1, 2.0],
        ["apple", 3, 6.0],
        ["orange", 1, 2.0],
        ["carrot", 1, 8.0],
    ]
    # is_valid_sale(price,"orange",1,2.0)
    # flag_invalid_sales(price, sales)
    generate_sales_report(price, sales)
    # print("SALES REPORT")
    # print(generate_sales_report(price, sales))

if __name__ == "__main__":
    main()

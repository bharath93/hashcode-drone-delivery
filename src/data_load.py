#%%
import constants  
import pandas as pd
import numpy as np 

#%%
def read_lines(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()
    
    line_list = [[int(n) for n in line.split()] for line in lines]

    return line_list

def read_products(line_list, prod_start):

    num_products = line_list[prod_start][0]
    prod_weights = line_list[prod_start+1]

    return num_products, prod_weights

def read_warehouse_details(line_list, wh_start):
    num_warehouses = line_list[wh_start][0]

    wh_locations = []
    wh_inventory = []
    row = wh_start + 1
    for wh in range(num_warehouses):
        wh_locations.append(line_list[row])
        wh_inventory.append(line_list[row+1])
        row = row + 2
    
    return wh_locations, wh_inventory, row

def read_orders(line_list, order_start, num_products):
    num_orders = line_list[order_start][0]

    order_locations = []
    order_quantity = []
    row = order_start + 1
    for order in range(num_orders):
        order_locations.append(line_list[row])
        prod_quantities = [0]*num_products
        for prod in line_list[row+2]:
            prod_quantities[prod] += 1
        order_quantity.append(prod_quantities)
        row = row + 3
    
    return num_orders, order_locations, order_quantity



def read_configs(line_list, config_start):
    configs = {}
    configs['num_row'] = line_list[config_start][0]
    configs['num_col'] = line_list[config_start][1]
    configs['num_drones'] = line_list[config_start][2]
    configs['num_turns'] = line_list[config_start][3]
    configs['max_payload'] = line_list[config_start][4]

    return configs


#%%
if __name__ == '__main__':
    list_lines = read_lines(constants.DATA_PATH+'busy_day.in')
    configs = read_configs(list_lines, 0)

    num_products, prod_weights = read_products(list_lines, 1)
    wh_locations, wh_inventory, wh_row_end = read_warehouse_details(list_lines, 3)
    num_orders, order_locations, order_quantity = read_orders(list_lines, order_start=wh_row_end, num_products=num_products)

    orders_df = pd.DataFrame(order_locations, columns=['row', 'column'])
    orders_products = pd.DataFrame(order_quantity, columns=['prod_{}'.format(i) for i in range(num_products)])
    orders_df = pd.concat([orders_df.reset_index(drop=True), orders_products], axis=1)
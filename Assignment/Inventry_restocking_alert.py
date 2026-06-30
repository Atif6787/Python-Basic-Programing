def check_inventory_levels(inventory):
    restock_threshold = 10  # Define a threshold for restocking
    items_to_restock = []

    for item, stock_level in inventory.items():
        if stock_level < restock_threshold:
            items_to_restock.append(item)
    return items_to_restock
    
print("Inventory Restocking Alert")
print("--------------------------")
# Sample inventory data
inventory_data = {
    "laptop": 5,
    "mouse": 15,  
    "keyboard": 8
}

restock_alert = check_inventory_levels(inventory_data)
print("Items that need to be restocked:", restock_alert)
print("--------------------------")
print("End of Inventory Check")
print("--------------------------")
print("Thank you for using the Inventory Restocking Alert System!")


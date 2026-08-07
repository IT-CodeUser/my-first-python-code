# 1. Create a list containing initial item dictionaries
inventory = [
    {"id": 101, "name": "Laptop", "price": 899.99, "in_stock": True},
    {"id": 102, "name": "Mouse", "price": 25.50, "in_stock": True},
    {"id": 103, "name": "Monitor", "price": 199.99, "in_stock": False}
]

# 2. Define a new item as a standalone dictionary
new_item = {
    "id": 104, 
    "name": "Keyboard", 
    "price": 45.00, 
    "in_stock": True
}

# 3. Add the new dictionary to the existing list
inventory.append(new_item)

# 4. Read and display the structured data
print("--- Full Inventory ---")
print(inventory)

print("\n--- Individual Item Details ---")
for item in inventory:
    print(f"Product: {item['name']} | Price: ${item['price']}")

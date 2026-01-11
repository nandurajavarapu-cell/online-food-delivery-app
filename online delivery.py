import time

# Users data
users = {
    "Nandini": {"password": "1234", "address": "Hyderabad", "phone": "8019581071"},
    "Sai": {"password": "5678", "address": "Chennai", "phone": "7093047534"}
}

# Restaurant menu
menu = {
    "Pizza": 200,
    "Burger": 120,
    "Biryani": 250,
    "Sandwich": 100
}

print("🍔 Welcome to Online Food Delivery App 🍕")

# Login
username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username]["password"] == password:
    print("✅ Login successful")
else:
    print("❌ Invalid login")
    exit()

print("\n📋 Menu:")
for item, price in menu.items():
    print(f"{item} - ₹{price}")

order = input("\nEnter food item: ")
quantity = int(input("Enter quantity: "))

if order in menu:
    total = menu[order] * quantity
    print(f"\n🧾 Bill Amount: ₹{total}")
else:
    print("❌ Item not available")
    exit()

confirm = input("Confirm order (yes/no): ")

if confirm.lower() == "yes":
    print("\n📦 Order confirmed")
    time.sleep(1)
    print("👨‍🍳 Preparing food...")
    time.sleep(1)
    print("🚚 Out for delivery...")
    time.sleep(1)
    print("✅ Order delivered successfully!")
else:
    print("❌ Order cancelled")
PRICES = {
    "Palak Paneer": 250, "Chole Bhature": 180, "Masala Dosa": 150, "Vada Pav": 60,
    "Vegetable Dumplings": 220, "Stir-Fried Noodles": 190, "Mapo Tofu (ask for no meat)": 280,
    "Cheese Enchiladas": 350, "Veggie Burrito": 320, "Bean Tostadas": 290,
    "Japchae (Glass Noodles)": 380, "Bibimbap (ask for no meat)": 420, "Kimchi Pancake": 300,

    "Butter Chicken": 380, "Mutton Rogan Josh": 450, "Chicken Biryani": 350,
    "Peking Duck": 800, "Kung Pao Chicken": 330, "General Tso's Chicken": 320,
    "Chicken Fajitas": 400, "Carnitas Tacos": 370, "Shrimp Ceviche": 450,
    "Korean BBQ (Bulgogi)": 500, "Army Stew (Budae Jjigae)": 480, "Fried Chicken (Chimaek)": 350,
    "Lasagna Bolognese": 420, "Shrimp Scampi": 550, "Saltimbocca": 600
}
order_items = []

def process_dish(dish_name):
    price = PRICES.get(dish_name, 0)
    order_items.append((dish_name, price))

def select_dishes(title, dish_list):
    print(f"\n--- {title} ---")
    dish_map = {}
    for i, dish_name in enumerate(dish_list, 1):
        price = PRICES.get(dish_name, 0)
        print(f"{i}: {dish_name} (₹{price})")
        dish_map[i] = dish_name

    print("\nEnter the numbers of the dishes you want, separated by commas (e.g., 1,3,4):")
    selection = input()

    selected_count = 0
    try:
        choices = [int(c.strip()) for c in selection.split(',') if c.strip()]

        for choice in choices:
            if choice in dish_map:
                dish = dish_map[choice]
                process_dish(dish)
                selected_count += 1
            else:
                print(f"Warning: Dish number {choice} is invalid and was skipped.")

    except ValueError:
        print("Invalid input format. Please only enter numbers and commas.")
        return

    print(f"\nAdded {selected_count} item(s) to your cart.")

print()
print("type 1 for veg")
print("type 2 for non veg")
try:
    a = int(input())
except ValueError:
    print("Invalid input. Please enter 1 or 2.")
    exit()

if a==1:
  print("indian-----1")
  print("Chinese----2")
  print("Mexican----3")
  print("Korean-----4")
  print("Mexican----5")
  try:
      ab = int(input())
  except ValueError:
      print("Invalid input for cuisine.")
      exit()

  if ab==1:
    dishes = ["Palak Paneer", "Chole Bhature", "Masala Dosa", "Vada Pav"]
    select_dishes("Indian Dishes", dishes)
  elif ab==2:
    dishes = ["Vegetable Dumplings", "Stir-Fried Noodles", "Mapo Tofu (ask for no meat)"]
    select_dishes("Chinese Dishes", dishes)
  elif ab==3 or ab==5:
    dishes = ["Cheese Enchiladas", "Veggie Burrito", "Bean Tostadas"]
    select_dishes("Mexican Dishes", dishes)
  elif ab==4:
    dishes = ["Japchae (Glass Noodles)", "Bibimbap (ask for no meat)", "Kimchi Pancake"]
    select_dishes("Korean Dishes", dishes)
  else:
    print("Invalid Cuisine Choice for Veg.")

elif a==2:
  print("indian-----1")
  print("Chinese----2")
  print("Mexican----3")
  print("Korean-----4")
  print("Italian----5")

  try:
      ab = int(input())
  except ValueError:
      print("Invalid input for cuisine.")
      exit()

  if ab==1:
    dishes = ["Butter Chicken", "Mutton Rogan Josh", "Chicken Biryani"]
    select_dishes("Indian Dishes", dishes)
  elif ab==2:
    dishes = ["Peking Duck", "Kung Pao Chicken", "General Tso's Chicken"]
    select_dishes("Chinese Dishes", dishes)
  elif ab==3:
    dishes = ["Chicken Fajitas", "Carnitas Tacos", "Shrimp Ceviche"]
    select_dishes("Mexican Dishes", dishes)
  elif ab==4:
    dishes = ["Korean BBQ (Bulgogi)", "Army Stew (Budae Jjigae)", "Fried Chicken (Chimaek)"]
    select_dishes("Korean Dishes", dishes)
  elif ab==5:
    dishes = ["Lasagna Bolognese", "Shrimp Scampi", "Saltimbocca"]
    select_dishes("Italian Dishes", dishes)
  else:
    print("Invalid Cuisine Choice for Non-Veg.")

else:
  print("Invalid input. Please choose 1 or 2.")
  exit()


if order_items:
    total_bill = sum(price for item, price in order_items)

    print("\n" + "="*30)
    print("    **FINAL BILL SUMMARY**")
    print("-" * 30)

    for item, price in order_items:
        print(f"{item.ljust(20)} ₹{price}")

    print("-" * 30)
    print(f"**Total Due:**".ljust(20) + f" **₹{total_bill}**")
    print("="*30)
else:
    print("\nNo items were added to the order. Thank you!")

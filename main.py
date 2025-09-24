# Person 1: Fixed Pricing Configuration

def initialize_pricing():
    # Location Prices 
    location_prices = {
        'Kuala Lumpur': 1.3,     
        'Klang': 1.2,   
        'Shah Alam': 1.1 
    }
    
    # Room Type Prices 
    room_type_prices = {
        'Standard': 50,   # Standard = 50
        'Deluxe': 110,    # Deluxe = 110
        'Suite': 200      # Suite = 200
    }
    
    # Service Rate (Fixed)
    service_rate = 0.1  # Service rate = 0.1 (10%)
    
    # Additional Add-ons (Fixed)
    breakfast_fee_per_night = 20  # Breakfast fee = RM20 per night when selected
    airport_pickup = 30   # Airport pickup = RM30
    extra_bed = 20        # Extra bed = RM20 
    
    # Create pricing configuration dictionary
    pricing_config = {
        'location_prices': location_prices,
        'room_type_prices': room_type_prices, 
        'service_rate': service_rate,
        'breakfast_fee_per_night': breakfast_fee_per_night,
        'airport_pickup': airport_pickup,
        'extra_bed': extra_bed
    }
    
    return pricing_config

# Function to get pricing config for other team members
def get_pricing_config():
    return initialize_pricing()

# Person 2: user base choice

def display_welcome():
    print("=" * 50)
    print(" Welcome to the Airbnb Booking System ")
    print("=" * 50)

def get_location_choice(pricing_config):
    location_prices = pricing_config['location_prices']
    print("\nAvailable Locations:")
    for idx, location in enumerate(location_prices.keys(), 1):
        print(f"{idx}. {location}")
     
    while True:
        try:
            choice = int(input("Choose a location (number): "))
            if 1 <= choice <= len(location_prices):
                location = list(location_prices.keys())[choice-1]
                return location
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Please enter a number, not text.")

def get_room_type_choice(pricing_config):
    room_type_prices = pricing_config['room_type_prices']
    print("\nRoom Types:")
    for idx, room_type in enumerate(room_type_prices.keys(), 1):
        print(f"{idx}. {room_type} - RM{room_type_prices[room_type]}/night")

    while True:
        try:
            choice = int(input("Choose a room type (number): "))
            if 1 <= choice <= len(room_type_prices):
                room_type = list(room_type_prices.keys())[choice-1]
                return room_type
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Please enter a number, not text.")

def get_number_of_nights():
    while True:
        try:
            nights = int(input("\nEnter number of nights: "))
            if nights > 0:
                return nights
            else:
                print("Number of nights must be at least 1.")
        except ValueError:
            print("Please enter a valid number.")

# Person 3 - Calculation Function

def calculate_price(location, room, nights, pricing):
    # Extract prices from pricing dictionary
    location_price = pricing['location_prices'][location]
    room_price = pricing['room_type_prices'][room]
    service_rate = pricing['service_rate']

    # Base price 
    base_price = (location_price * room_price) * nights

    # Service fee 
    service_fee = base_price * service_rate

    return base_price, service_fee

 # Person 4: Add-ons Selection

def get_add_ons(pricing_config, nights):
    addon_map = {
        1: ("Breakfast", pricing_config['breakfast_fee_per_night'], "per_night"),
        2: ("Airport Pickup", pricing_config['airport_pickup'], "one_time"),
        3: ("Extra Bed", pricing_config['extra_bed'], "per_night"),
    }

    print("\nAvailable Add-ons:")
    print(f"1. Breakfast (RM{pricing_config['breakfast_fee_per_night']} per night)")
    print(f"2. Airport Pickup (RM{pricing_config['airport_pickup']} one-time)")
    print(f"3. Extra Bed (RM{pricing_config['extra_bed']} per night)")
    print("0. Done selecting add-ons")

    selected = []
    selected_names = set()
    total_cost = 0

    while True:
        raw = input("Choose an add-on (number, 0 to finish): ").strip()
        # Allow typos like ' 1 ', block non-numeric
        if not raw.isdigit():
            print("Please enter a valid number (0, 1, 2, or 3).")
            continue

        choice = int(raw)
        if choice == 0:
            break

        if choice not in addon_map:
            print("Invalid choice. Please select a valid option (0-3).")
            continue

        name, price, mode = addon_map[choice]
        if name in selected_names:
            print(f"You've already added {name}.")
            continue

        # compute cost based on mode
        if mode == "per_night":
            add_cost = price * nights
        else:  # one_time
            add_cost = price

        selected.append(name)
        selected_names.add(name)
        total_cost += add_cost
        print(f"✅ {name} added. (+RM{add_cost:.2f})")

    return selected, total_cost
    
# Person 5: Calculate Add-ons, Subtotal, Total with Discount

def calculate_total_price(nights, base_price, service_fee, addons_cost):
    # Calculate the subtotal
    subtotal = base_price + service_fee + addons_cost
    
    # Apply a discount if the number of nights is greater than 3
    if nights > 3:
        discount = 0.1 * subtotal  # 10% discount
        discounted_subtotal = subtotal - discount
        print(f"\n A 10% discount is applied for staying more than 3 nights: RM {discount:.2f}")
        return discounted_subtotal, discount
    else:
        return subtotal, 0  # No discount if nights <= 3

# Person 6: Display All Outputs (Final Receipt Style)

def display_summary(location, room_type, nights, addons, base, fee, addons_cost, subtotal, discount):
    print("\n" + "=" * 50)
    print("              📋 BOOKING SUMMARY")
    print("=" * 50)
    print(f"🏙️  Location       : {location}")
    print(f"🛏️  Room Type      : {room_type}")
    print(f"🌙 Nights         : {nights}")
    print(f"➕ Add-ons        : {', '.join(addons) if addons else 'None'}")
    print("-" * 50)
    print(f"💰 Base Price     : RM {base:.2f}")
    print(f"💼 Service Fee    : RM {fee:.2f}")
    print(f"🍽️ Add-ons Cost   : RM {addons_cost:.2f}")
    if discount > 0:
        print(f"🎉 Discount (10%) : -RM {discount:.2f}")
    print("-" * 50)
    print(f"💵 TOTAL PRICE    : RM {subtotal:.2f}")
    print("=" * 50)
    print("✅ Thank you for booking with us!")

# Main Program (Integration with existing code)
if __name__ == "__main__":
    pricing = get_pricing_config()
    display_welcome()

    location = get_location_choice(pricing)
    room_type = get_room_type_choice(pricing)
    nights = get_number_of_nights()

    addons, addons_cost = get_add_ons(pricing, nights)

    base, fee = calculate_price(location, room_type, nights, pricing)

    # Call your Part 5 function to calculate the total
    subtotal, discount = calculate_total_price(nights, base, fee, addons_cost)
   # Person 6: Display final output
    display_summary(location, room_type, nights, addons, base, fee, addons_cost, subtotal, discount)

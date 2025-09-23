# person 1: Fixed Pricing Configuration

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
    
    # # Additional Add-ons (Fixed)
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

# person 2: user base choice

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

 # main           

if __name__ == "__main__":
<<<<<<< HEAD
    # Initialize pricing when module is run directly
    pricing_config = initialize_pricing()

# Person 3 - Calculation Function

def calculate_price(location, room, nights, pricing):
    """
    Calculate base price and service fee
    location (str) : chosen location (example: 'KL')
    room (str)     : chosen room type (example: 'Deluxe')
    nights (int)   : number of nights booked
    pricing (dict) : all pricing details from Person 1
    """

    # Extract prices from pricing dictionary
    location_price = pricing['location_prices'][location]
    room_price = pricing['room_type_prices'][room]
    service_rate = pricing['service_rate']

    # Base price = (location price + room price) * nights
    base_price = (location_price + room_price) * nights

    # Service fee = base price * service rate
    service_fee = base_price * service_rate

    return base_price, service_fee


if __name__ == "__main__":
    pricing = get_pricing_config()

    print("=== Welcome to Project Promoters Booking System ===")
    
    # Location input with validation
    print("Available Locations:", ", ".join(pricing['location_prices'].keys()))
    while True:
        location = input("Enter location (KL / Klang / Shah Alam): ").title()
        if location in pricing['location_prices']:
            break
        else:
            print("Invalid location! Please try again.")

    # Room type input with validation
    print("Available Room Types:", ", ".join(pricing['room_type_prices'].keys()))
    while True:
        room = input("Enter room type (Standard / Deluxe / Suite): ").title()
        if room in pricing['room_type_prices']:
            break
        else:
            print("Invalid room type! Please try again.")

    # Nights input with validation
    while True:
        try:
            nights = int(input("Enter number of nights: "))
            if nights > 0:
                break
            else:
                print("Number of nights must be more than 0.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Call Person 3 function
    base, fee = calculate_price(location, room, nights, pricing)

    # Display result
    print("\n--- Booking Summary ---")
    print("Location:", location)
    print("Room Type:", room)
    print("Nights:", nights)
    print("Base Price: RM", base)
    print("Service Fee: RM", round(fee, 2))
    print("Total Price: RM", round(base + fee, 2))
=======
    pricing_config = get_pricing_config()
    display_welcome()
    location = get_location_choice(pricing_config)
    room_type = get_room_type_choice(pricing_config)
    nights = get_number_of_nights()
>>>>>>> 474c500c95474880d4fdbc1cf3efc130f76d8f26

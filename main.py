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
    pricing_config = get_pricing_config()
    display_welcome()
    location = get_location_choice(pricing_config)
    room_type = get_room_type_choice(pricing_config)
    nights = get_number_of_nights()

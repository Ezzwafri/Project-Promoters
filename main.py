# Person 1 - Hotel Booking System: Fixed Pricing Configuration
# This module sets up all the fixed pricing parameters for the hotel booking system

def initialize_pricing():
    """
    Initialize all fixed pricing parameters
    Based on the flowchart requirements
    """
    # Location Prices 
    location_prices = {
        'KL': 113,      # Kuala Lumpur = 113
        'Klang': 108,   # Klang = 108  
        'Shah Alam': 111 # Shah Alam = 111
    }
    
    # Room Type Prices 
    room_type_prices = {
        'Standard': 50,   # Standard = 50
        'Deluxe': 110,    # Deluxe = 110
        'Suite': 200      # Suite = 200
    }
    
    # Service Rate (Fixed)
    service_rate = 0.1  # Service rate = 0.1 (10%)
    
    # Breakfast Fee (Fixed)
    breakfast_fee_per_night = 20  # Breakfast fee = RM20 per night when selected
    
    # Additional Add-ons (Fixed)
    airport_pickup = 30   # Airport pickup = RM30
    extra_bed = 20        # Extra bed = RM20 per night
    
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
    """
    Function for other team members to get the pricing configuration
    """
    return {
        'location_prices': {'KL': 113, 'Klang': 108, 'Shah Alam': 111},
        'room_type_prices': {'Standard': 50, 'Deluxe': 110, 'Suite': 200},
        'service_rate': 0.1,
        'breakfast_fee_per_night': 20,
        'airport_pickup': 30,
        'extra_bed': 20
    }

if __name__ == "__main__":
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
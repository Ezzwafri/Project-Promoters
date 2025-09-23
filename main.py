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
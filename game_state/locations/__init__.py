from game_state.locations.pallet_town.childhood_house.bedroom import create_bedroom
from game_state.locations.pallet_town.childhood_house.ground_floor import create_ground_floor

def create_locations():
    return {
        "childhood bedroom": create_bedroom(),
        "ground floor": create_ground_floor()
    }

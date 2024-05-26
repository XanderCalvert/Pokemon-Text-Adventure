from game_state.location import GameObject, Location

def create_bedroom():
    bed = GameObject(
        name="Bed",
        description="It's your bed. It's unmade, as usual.",
        interactions={"look": "It's just your bed.", "use": "You lie down for a quick nap."}
    )

    bedroom = Location(
        name="Childhood Bedroom",
        description="You are in your childhood bedroom. There are posters on the wall and a bed in the corner.",
        objects=[bed]
    )

    return bedroom

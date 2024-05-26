from game_state.location import GameObject, Location

def create_ground_floor():
    sink = GameObject(
        name="Sink",
        description="It's a kitchen sink. It's clean and shiny.",
        interactions={"look": "The sink is clean.", "use": "You wash your hands in the sink."}
    )

    mum = GameObject(
        name="Mum",
        description="It's your mum. She looks happy to see you.",
        interactions={"look": "Your mum is here, always supportive.", "talk": "Mum: 'Have a great day, dear!'"}
    )

    ground_floor = Location(
        name="Ground Floor",
        description="You are on the ground floor of your house. The kitchen is here, and your mum is nearby.",
        objects=[sink, mum]
    )

    return ground_floor

class GameObject:
    def __init__(self, name, description, interactions):
        self.name = name
        self.description = description
        self.interactions = interactions

    def interact(self, action):
        if action in self.interactions:
            return self.interactions[action]
        else:
            return "Oak's words echoed... \"There's a time and place for everything but not now!\""

class Location:
    def __init__(self, name, description, objects):
        self.name = name
        self.description = description
        self.objects = {obj.name.lower(): obj for obj in objects}

    def look_around(self):
        return self.description

    def look_at(self, object_name):
        obj = self.objects.get(object_name.lower())
        if obj:
            return obj.description
        else:
            return "You don't see that here."

    def interact_with(self, object_name, action):
        obj = self.objects.get(object_name.lower())
        if obj:
            return obj.interact(action)
        else:
            return "You don't see that here."

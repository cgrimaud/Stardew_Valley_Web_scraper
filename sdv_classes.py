
class CommunityCenterRoom:
    room_id = 1
    def __init__(self, name, bundles = [], completed = False):
        self.name = name
        self.bundles = bundles
        self.completed = completed
        self.room_id = CommunityCenterRoom.room_id
        CommunityCenterRoom.room_id += 1


class Bundle:
    bundle_id = 1
    def __init__(self, name, amt_to_complete, room, items = [], completed = False):
        self.name = name
        self.items = items
        self.amt_to_complete = amt_to_complete
        self.room = room
        self.completed = completed
        self.bundle_id = Bundle.bundle_id
        Bundle.bundle_id += 1



class Item:
    item_id = 1
    def __init__(self, name, completed = False):
        self.name = name
        self.completed = completed
        self.item_id = Item.item_id
        Item.item_id += 1

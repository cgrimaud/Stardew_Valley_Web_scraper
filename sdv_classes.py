
class CommunityCenterRoom:
    room_id = 1
    def __init__(self, name, bundles = [], completed = False):
        self.name = name
        self.bundles = bundles
        self.completed = completed
        self.room_id = CommunityCenterRoom.room_id
        CommunityCenterRoom.room_id += 1

    def get_name(self):
        return self.name

    def get_room_id(self):
        return str(self.room_id)

    def get_bundles(self):
        content = "\n"
        for bundle in self.bundles:
            content += bundle.get_name() + "\n"
        return content

    def append_bundle(self, bundle):
        self.bundles += [bundle]
        

    def __str__(self):
        return "{}\n***{}***{}".format(
            self.get_room_id(), 
            self.name, 
            self.get_bundles()
        )



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

    def get_name(self):
        return self.name
        
    def get_items(self):
        content = "\n"
        for item in self.items:
            content += item.get_name() + "\n"
        return content
    
    def get_amt_to_complete(self):
        return self.amt_to_complete

    def get_room_name(self):
        return self.room

    def get_bundle_id(self):
        return str(self.bundle_id).zfill(2)

    def __str__(self):
        return "{}\n***{}({})***\n{}{}".format(
            self.get_bundle_id(), 
            self.name, 
            self.amt_to_complete,
            self.room,
            self.get_items()
        )


class Item:
    item_id = 1
    def __init__(self, name, completed = False):
        self.name = name
        self.completed = completed
        self.item_id = Item.item_id
        Item.item_id += 1

    def __str__(self):
        return "{}".format(self.name)

    def get_name(self):
        return self.name
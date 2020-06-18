
class CommunityCenterRoom:
    room_id = 1
    def __init__(self, name, bundles = []):
        self.name = name
        self.bundles = bundles
        self.room_id = CommunityCenterRoom.room_id
        CommunityCenterRoom.room_id += 1

    def get_name(self):
        return self.name

    def get_room_id(self):
        return str(self.room_id)

    def get_bundles(self):
        content = []
        for bundle in self.bundles:
            content.append(bundle)
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
    def __init__(self, name, items, amt_to_complete, room):
        self.name = name
        self.items = items
        self.amt_to_complete = amt_to_complete
        self.room = room
        self.bundle_id = Bundle.bundle_id
        Bundle.bundle_id += 1

    def get_name(self):
        return self.name
        
    def get_items(self):
        content = []
        for item in self.items:
            content.append(item)
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
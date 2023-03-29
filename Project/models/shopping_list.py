class Shopping_List:
    def __init__(self, date_created, name, date_shopped=None, selections=[], id=None):
        self.date_created = date_created
        self.name = name
        self.date_shopped = date_shopped
        self.selection = selections
        self.id = id
        # selection is a list of Selections, which is an Item along with
        # other potential values - for example whether it's been
        # picked up or not. i.e. 
        # selection = [Selection1, Selection2]
        # Selection1 = (Milk_object, 1, False)
        # Selection2 = (Egg_object, 6, True)
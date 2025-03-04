from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=0):
        super().__init__(condition=condition)
        self.category = "Clothing"
    

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        item_condition = super().condition_description()

        return item_condition
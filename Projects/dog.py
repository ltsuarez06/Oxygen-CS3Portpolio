class Locker:
    def __init__(self, locker_number, owner, status):
        self.locker_number = locker_number
        self.owner = owner
        self.status = status

    def assign_locker(self, name):
        self.owner = name
        self.status = "occupied"

    def release_locker(self, name):
        self.owner = name
        self.status = "available" 

    def display_info(self):
        self.display_info()
        

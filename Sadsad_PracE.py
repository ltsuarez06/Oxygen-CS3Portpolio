def __init__(self, locker_number, owner, status):
    self.locker_number = locker_number
    self.owner = owner
    self.status = status

    def assign_locker(self, owner):
        if self.status == "available":
            self.owner = owner
            self.status = "occupied"
            return True
        else:
            return False

        def release_locker(self):  
            if self.status == "occupied":
                self.owner = None
                self.status = "available"
                return True

            def display_locker_info(self):
                return f"Locker Number: {self.locker_number}, Owner: {self.owner}, Status: {self.status}"       

            
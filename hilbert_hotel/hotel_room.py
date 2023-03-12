class HotelRoom:

    limits = {'Single': 1, 'Double': 2, 'King': 2, 'Shufra Deshufra': 3}

    """
        A class representing a hotel room.

       Attributes:
           Class attributes:
           limits (dict): A dictionary containing the maximum number of beds allowed for each room type.
            
           Instance attributes:
           room_type (str): The type of the room, such as 'Single', 'Double', 'King', or 'Shufra Deshufra'.
           room_number (int): The room number.
           floor (int): The floor number where the room is located.
           available (bool): A flag indicating whether the room is currently available.
           current_beds (int): The current number of beds in the room.

       Methods:
           reserve_room(self) -> None: Reserves the room.
           release_room(self) -> None: Releases the room.
           add_bed(self) -> None: Adds a bed to the room if the current number of beds is less than the maximum limit.
           remove_bed(self) -> None: Removes a bed from the room if the current number of beds is greater than one.
           max_beds_limit(self) -> int: Returns the maximum number of beds allowed for the room type.
           
    
    """
    
    def __init__(self, room_type, room_number, floor):
        self.room_type = room_type
        self.room_number = room_number
        self.floor = floor
        self.available = True
        self.current_beds = 0

    def __str__(self):
        return f"Room Number: {self.room_number}\nFloor: {self.floor}\nAvailable: {self.available}\n" \
               f"Current number of beds: {self.current_beds}"

    def reserve_room(self):
        self.available = False
        self.current_beds += 1

    def release_room(self):
        self.available = True
        self.current_beds = 0

    def add_bed(self):
        if self.current_beds < self.max_beds_limit():
            self.current_beds += 1

    def remove_bed(self):
        if self.current_beds > 1:
            self.current_beds -= 1

    def max_beds_limit(self):
        return HotelRoom.limits[self.room_type]

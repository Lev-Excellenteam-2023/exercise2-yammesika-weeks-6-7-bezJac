import random
from hotel_room import HotelRoom


class HotelBuilder:
    """
          A class that builds a hotel.
          (Helper Class for HilbertHotel Class)
          Attributes:
              None

          Methods:
              build_hotel: Builds a hotel with the specified number of floors and total rooms.
                           There are (total rooms // floors) per floor, so total rooms may decrease.
              generate_room: Generates a HotelRoom object with a random room type, a floor, and room number.
      """

    @staticmethod
    def build_hotel(floors, total_rooms):
        rooms_per_floor = total_rooms // floors
        return [HotelBuilder.generate_room(floor * 100 + room, floor) for floor in range(1, floors + 1) for room in
                range(rooms_per_floor)]

    @staticmethod
    def generate_room(floor, room_number):
        return HotelRoom(random.choice(['Single', 'Double', 'King', 'Shufra Deshufra']), floor, room_number)


class HilbertHotel:
    """
        A class representing Hilbert's hotel (finite number of rooms)

        Attributes:
            rooms (list): A list of HotelRoom objects representing all the rooms in the hotel.
    """

    def __init__(self, floors, total_rooms):
        self.rooms = HotelBuilder.build_hotel(floors, total_rooms)

    def __str__(self):
        return ''.join(str(room) + '\n' for room in self.rooms)

    def search_room(self, floor=None, room_type=None):
        """Search for an available room, can be specified by floor and/or room type
            Returns:
                index of first available room
        """
        rooms_list = self.rooms
        # filter list if parameters were past
        if floor:
            rooms_list = list(filter(lambda current_room: current_room.floor == floor, rooms_list))
        if room_type:
            rooms_list = list(filter(lambda current_room: current_room.room_type == room_type, rooms_list))
        # return index of the room in the list
        for room in rooms_list:
            if room.available is True:
                return self.find_room(room.room_number)

    def reserve_room(self, floor=None, room_type=None):
        """reserve an available room, can be specified by floor and/or room type.
        """
        # find available room
        room_index = self.search_room(floor, room_type)
        if room_index is not None:
            self.rooms[room_index].reserve_room()

    def release_room(self, room_number):
        """
           Releases a room (given a room number).
        """
        room_index = self.find_room(room_number)
        self.rooms[room_index].release_room()

    def find_room(self, room_number):
        """Find a given room's index in the room list"""
        try:
            index_of_room = self.rooms.index(next(room for room in self.rooms if room.room_number == room_number))
            return index_of_room
        except StopIteration:
            print("Room not found in list.")

    def add_bed(self, room_number):
        """Add a bed to a room"""
        room_index = self.find_room(room_number)
        self.rooms[room_index].add_bed()

    def remove_bed(self, room_number):
        """remove a bed from a room"""
        room_index = self.find_room(room_number)
        self.rooms[room_index].remove_bed()

    def upgrade(self, room_number):
        """upgrade a guest to the next type level of room"""

        types_list = ['Single', 'Double', 'King', 'Shufra Deshufra']
        # find guests current room details
        room_index = self.find_room(room_number)
        room = self.rooms[room_index].room_type
        room_type = types_list.index(room)
        current_beds = self.rooms[room_index].current_beds

        # upgrade guest if possible
        if room_type != 3:
            new_room_index = self.search_room(None, types_list[room_type + 1])
            self.rooms[room_index].release_room()
            self.rooms[new_room_index].reserve_room()
            for _ in range(current_beds):
                self.rooms[new_room_index].add_bed()

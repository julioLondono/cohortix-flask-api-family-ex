
from random import randint

class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
            {"first_name": "John", "age": "33 Years old", "gender": "Male", "Lucky Numbers": [7, 13, 22], "member_id": 1},
            {"first_name": "Jane", "age": "35 Years old", "gender": "Female", "Lucky Numbers": [10, 14, 3], "member_id": 2},
            {"first_name": "Jimmy", "age": "5 Years old", "gender": "Male", "Lucky Numbers": [1], "member_id": 3}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "first_name" in member and "age" in member and "gender" in member and "lucky_numbers" in member:
            member["member_id"] = randint(0, 99999999)
            self._members.append(member)
        else:
            return 400
        return self._members

    def delete_member(self, id):
        newList = []
        for x in self._members:
            if x["member_id"] != id:
                newList.append(x)
        self._members = newList
        return self._members

    def update_member(self, id, member):
        localMember = self.get_member(id)
        if localMember != False:
            if "first_name" in member and "age" in member and "lucky_numbers" in member:
                localMember["first_name"] = member["first_name"]
                localMember["age"] = member["age"]
                localMember["lucky_numbers"] = member["lucky_numbers"]
                return localMember
            return 400
        return 404
        ## you have to implement this method
        ## loop the list and replace the memeber with the given id


    def get_member(self, person_id):
        for x in self._members:
            if x["member_id"] == person_id:
                return (x)
            return False

    def get_all_members(self):
        return self._members

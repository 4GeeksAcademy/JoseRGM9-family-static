from random import randint
from flask import Flask, jsonify
app = Flask(__name__)


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # example list of members
        self._members = [{
                                "id": self._generate_id(),
                                "first_name": "John",
                                "last_name": last_name,
                                "age": 33,
                                "lucky_numbers": [7, 13, 22]
                            },
                            {
                                "id": self._generate_id(),
                                "first_name": "Jane",
                                "last_name": last_name,
                                "age": 35,
                                "lucky_numbers": [10, 14, 3]
                            },
                            {
                                "id": self._generate_id(),
                                "first_name": "Jimmy",
                                "last_name": last_name,
                                "age": 5,
                                "lucky_numbers": [1]
                            },
                        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id


    def add_member(self, member):
        member ['id'] = self._generate_id()
        member ['last_name'] = self.last_name
        return self._members.append(member)
    pass


    def delete_member(self, id):
        for member in self._members:
            if member['id'] == id:
                    self._members.remove(member)


    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
            break

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

    










#!/usr/bin/python3
"""city"""


from model.base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.country_id = country_id
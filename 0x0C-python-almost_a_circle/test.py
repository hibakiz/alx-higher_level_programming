from models.base import Base
from models.square import Square
import json
import inspect
sq = Square(1, 0, 0, 609)
json_dict = sq.to_dictionary()
json_string = Base.to_json_string([json_dict])
print(json.loads(json_string))

import sys
import json
from pprint import pprint

constants_json_path = "constants.json"

def set_constants(env):
    with open(constants_json_path) as jsonFile:
        data = json.load(jsonFile)

    data["env"] = env

    with open(constants_json_path, "w") as jsonFile:
        json.dump(data, jsonFile)

    print(data)

if __name__ == '__main__':
    env = sys.argv[2]
    set_constants(env)
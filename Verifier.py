import json

with open("../goblin/package.json", "r") as file:
    package = json.load(file)

with open("../info/config.json", "r") as file:
    config = json.load(file)["config"]

accepted = True
reason = "Package accepted"

if package["Size"] > config["RequestDataLimit"]:
    accepted = False
    reason = "RequestDataLimit exceeded"

if package["DataType"] != config["RequestDataType"]:
    accepted = False
    reason = "RequestDataType mismatch"

response = {
    "accepted": accepted,
    "reason": reason
}

with open("../goblin/response.json", "w") as file:
    json.dump(response, file, indent=2)

print(reason)

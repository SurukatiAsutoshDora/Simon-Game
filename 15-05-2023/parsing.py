import json

with open("sample_data.json") as file:
    json_content = file.read()
    data = json.loads(json_content)
    transformed_items = []
    parameters_list = data["parametersList"]
    for parameter in parameters_list:
        transformed_item = {
            "parameter_name": parameter["parameterName"],
            "minimun_value": parameter["min"],
            "maximum_value": parameter["max"],
            "average_value": parameter["avg"]
        }
        transformed_items.append(transformed_item)

transformed_json = json.dumps(transformed_items, indent=2)
print(transformed_json)

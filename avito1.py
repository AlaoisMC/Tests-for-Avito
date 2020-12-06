import json


class avito1:
    def __init__(self):
        pass

    def values(self):
        with open("./qa-into-CoE-trainee-task/Values.json", "r") as read_file:
            data = json.load(read_file)

        with open("./qa-into-CoE-trainee-task/TestcaseStructure.json", "r") as read_file:
            data1 = json.load(read_file)

        # print("values:")
        for value in data["values"]:
            # print(value)
            for param in data1["params"]:
                # print(params)
                param["value"] = value["value"]

        # print("params:")
        for param in data1["params"]:
            if (str(param["value"]) == ""):
                param["value"] = "Валидация параметров на подаче объявления"
            # print(param)

        with open('newdata.json', 'w', encoding='utf-8') as outfile:
            json.dump(data1, outfile, ensure_ascii=False)


if name == "__main__":
    avito1 = avito1()
    avito1.values()
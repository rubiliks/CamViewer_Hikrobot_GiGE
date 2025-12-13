#data [[{'selectValve': 56, 'valveTime': -0.00272266502417174, 'valveOpen': True}, {'selectValve': 46, 'valveTime': 0.04362241528522805}, {'selectValve': 44, 'valveTime': 0.007034189659472008}, {'selectValve': 66, 'valveTime': 0.050068910561150926}]]
bool_list = [False] * 80

data_list = [[{'selectValve': 56, 'valveTime': -0.00272266502417174, 'valveOpen': True}, {'selectValve': 46, 'valveTime': 0.04362241528522805}, {'selectValve': 44, 'valveTime': 0.007034189659472008}, {'selectValve': 66, 'valveTime': 0.050068910561150926}]]
for objsInframe in data_list:
    for obj in objsInframe:
        print(obj)
        if "valveOpen" in obj:
            if obj["valveOpen"] == True:
                print("Open valve", obj)
                bool_list[obj["selectValve"]] = True
            else:
                print("Close valve", obj)
                bool_list[obj["selectValve"]] = False
counter = 0
for valve in bool_list:
    print('valve',counter, valve)
    counter = counter + 1

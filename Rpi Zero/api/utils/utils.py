import datetime


def process_labels_single_dataset_charts(data, filter, chartId):
    try:
        print("processing labels...")
        parsed_data = []
        obj = {}
        obj["labels"] = []
        obj["datasets"] = []
        if filter == -1 or filter == 365:
            arr = []
            for x in data:
                arr.append(
                    {
                        "date": datetime.date(int(x.txn_year), int(x.txn_month), 1),
                        "value": round(x.avg, 2),
                    }
                )
            arr.sort(
                key=lambda x: (x["date"].year, x["date"].month),
            )
            for y in arr:
                obj["labels"].append(y["date"])
                parsed_data.append(y["value"])
            obj["datasets"].append(
                {
                    "label": "Data",
                    "backgroundColor": "#00D8FF",
                    "data": parsed_data,
                }
            )

        elif filter == 0 or filter == 7 or filter == 30:
            labels = []
            for x in data:
                labels.append(x.created_at)
                parsed_data.append(round(x.avg, 2))
            obj["labels"] = labels[::-1]
            obj["datasets"].append(
                {
                    "label": "Data",
                    "backgroundColor": "#00D8FF",
                    "data": parsed_data[::-1],
                }
            )
        return obj
    except Exception as e:
        print("Error processing labels: ", e)
        return None


# doughnut chart label processing: BEWARE : the view format is different !
# This processing in not compatible with other chart formats
def process_labels_multiple_dataset_charts(data, filter, chartId):
    try:
        print("processing labels...")
        parsed_data = None
        obj = {}
        obj["datasets"] = []
        obj["labels"] = []
        if filter == -1 or filter == 365:
            temp = {}
            # convert into an object by month and date and add the relevant information
            for x in data:
                temp[str(int(x.txn_year)) + "-" + str(int(x.txn_month))] = {}
            for x in data:
                if chartId == "rain_chart":
                    temp[str(int(x.txn_year)) + "-" + str(int(x.txn_month))][
                        str(x.is_raining)
                    ] = x.count
                else:
                    temp[str(int(x.txn_year)) + "-" + str(int(x.txn_month))][
                        str(x.is_soil_moist)
                    ] = x.count
            # add the totals and parse each False and True and generate labels
            true_data = []
            false_data = []
            labels = []
            for x in temp:
                labels.append(x)
                false = temp[x]["False"] if "False" in temp[x] else 0
                true = temp[x]["True"] if "True" in temp[x] else 0
                total = false + true
                true_data.append(int(round(true / total, 2) * 100))
                false_data.append(int(round(false / total, 2) * 100))
            # finally arrange the dataset
            obj["datasets"].append(
                {
                    "label": "True",
                    "backgroundColor": "#41B883",
                    "data": true_data[::-1],
                }
            )
            obj["datasets"].append(
                {
                    "label": "False",
                    "backgroundColor": "#E46651",
                    "data": false_data[::-1],
                }
            )
            obj["labels"] = labels[::-1]

        elif filter == 0 or filter == 7 or filter == 30:
            total = 0
            false_count = 0
            true_count = 0
            temp = {}
            # parse the data from the database -> construct as object with date as key
            for y in data:
                temp[str(y.created_at)] = {}
                temp[str(y.created_at)]["count"] = 0
            for x in data:
                if chartId == "rain_chart":
                    if x.is_raining == False:
                        temp[str(x.created_at)]["false"] = x.count
                    else:
                        temp[str(x.created_at)]["true"] = x.count
                if chartId == "moisture_chart":
                    if x.is_soil_moist == False:
                        temp[str(x.created_at)]["false"] = x.count
                    else:
                        temp[str(x.created_at)]["true"] = x.count
                temp[str(x.created_at)]["count"] += x.count
            true_data = []
            false_data = []
            labels = []
            # the key might not exist, we check for that by replacing by 0
            for key in temp:
                labels.append(str(key))
                true_data.append(
                    int(
                        round(
                            (
                                (temp[key]["true"] if "true" in temp[key] else 0)
                                / temp[key]["count"]
                            ),
                            2,
                        )
                        * 100
                    ),
                )
                false_data.append(
                    int(
                        round(
                            (
                                (temp[key]["false"] if "false" in temp[key] else 0)
                                / temp[key]["count"]
                            ),
                            2,
                        )
                        * 100
                    ),
                )
            # finally arrange the dataset
            obj["datasets"].append(
                {
                    "label": "True",
                    "backgroundColor": "#41B883",
                    "data": true_data[::-1],
                }
            )
            obj["datasets"].append(
                {
                    "label": "False",
                    "backgroundColor": "#E46651",
                    "data": false_data[::-1],
                }
            )
            obj["labels"] = labels[::-1]
        return obj
    except Exception as e:
        print("Error processing labels: ", e)
        return None

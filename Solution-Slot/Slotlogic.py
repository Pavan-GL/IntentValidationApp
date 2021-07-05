def util_convert_to_dict2(tempResult):
    d = collections.OrderedDict()
    d['intents_info'] = tempResult[0]
    d['parameters'] = tempResult[1]
    d['slots_filled'] = tempResult[2]
    d['trigger'] = tempResult[3]
    return d


def in_slot_validator(data):
    intents_info = {"name": data["intents_info"]["name"], "slots": []}
    parameters = []
    slots_filled = []
    trigger = ""
    slots_input = data["intents_info"]["slots"]
    validator_mapper = {"finite_values_entity": validate_finite_wrapper,
                        "numeric_values_entity": validate_numeric_wrapper}

    # Aggregation
    for slot in slots_input:
        validate = slot["validation_parser"]
        func_validate = validator_mapper[validate]

        result = func_validate(slot)

        tempslot = {"name": slot["name"], "filled": result["filled"], "partially_filled": result["partially_filled"]}

        intents_info["slots"].append(tempslot)
        parameters.append(result["parameters"])
        slots_filled.append(slot["name"])

    # Filtering for slots_filled
    newslots_filled = []
    for i in range(len(intents_info["slots"])):
        res = intents_info["slots"][i]

        if not res["filled"]:
            trigger = trigger + "_" + slots_filled[i]
            continue
        newslots_filled.append(slots_filled[i])

    slots_filled = newslots_filled

    # Filtering for parameters
    new_parameters = {}
    for i in range(len(parameters)):
        if len(parameters[i]) > 0:
            li=tuple(parameters[i].items())
            print(li)
            new_parameters[li[0][0]]=li[0][1]

    parameters = new_parameters

    parameters = new_parameters
    trigger = "_" + intents_info["name"] + "_collect_" + trigger + "_"
    tempResult = tuple([intents_info, parameters, slots_filled, trigger])
    result = util_convert_to_dict2(tempResult)
    return result
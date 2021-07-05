import collections
from typing import List, Dict

from simpleeval import simple_eval


def util_convert_to_dict(tempResult):
    d = collections.OrderedDict()
    d['filled'] = tempResult[0]
    d['partially_filled'] = tempResult[1]
    d['trigger'] = tempResult[2]
    d['parameters'] = tempResult[3]
    return d


def validate_finite_wrapper(jsoni):
    jsonNative = jsoni
    values = jsonNative["values"]
    supported_values = jsonNative["supported_values"]
    invalid_trig = jsonNative["invalid_trigger"]
    key = jsonNative["key"]

    pick_first = False
    supported_multiple = False
    if "pick_first" in jsonNative:
        pick_first = jsonNative["pick_first"]
    if "supported_multiple" in jsonNative:
        supported_multiple = jsonNative["supported_multiple"]

    tempResult = validate_finite_values_entity(values, supported_values, invalid_trig, key, supported_multiple,
                                               pick_first)
    result = util_convert_to_dict(tempResult)
    return result


def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None,
                                  invalid_trigger: str = None, key: str = None,
                                  support_multiple: bool = True, pick_first: bool = False):
    """
    Validate an entity on the basis of its value extracted. The method will check if the values extracted("values"
    arg) lies within the finite list of supported values(arg "supported_values").
    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param supported_values: List of supported values for the slot
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :return: a tuple of (filled, partially_filled, trigger, params)
    """

    filled = False
    partially_filled = False
    trigger = ""
    parameters = {}
    # Edge case
    if len(values) == 0:
        trigger = invalid_trigger
        SlotValidationResult = tuple([filled, partially_filled, trigger, parameters])
        return SlotValidationResult

    if len(values) > 0:
        partially_filled = True

    # Convert supported_values to set for faster search
    supported_values = set(supported_values)

    parameters[key] = []
    for diction in values:
        if diction["value"] in supported_values:
            parameters[key].append(diction["value"].upper())
        else:
            trigger = invalid_trigger

    if trigger != invalid_trigger:
        filled = True
        partially_filled = False
    else:
        parameters = {}
    if pick_first:
        parameters[key] = str(values[0]["value"].upper())

    SlotValidationResult = tuple([filled, partially_filled, trigger, parameters])
    return SlotValidationResult


def validate_numeric_wrapper(jsoni):
    jsonNative = jsoni
    values = jsonNative["values"]
    invalid_trig = jsonNative["invalid_trigger"]
    key = jsonNative["key"]
    constraint = jsonNative["constraint"]
    var_name = jsonNative["var_name"]

    pick_first = False
    supported_multiple = False
    if "pick_first" in jsonNative:
        pick_first = jsonNative["pick_first"]
    if "supported_multiple" in jsonNative:
        supported_multiple = jsonNative["supported_multiple"]

    tempResult = validate_numeric_entity(values, invalid_trig, key, supported_multiple, pick_first, constraint,
                                         var_name)

    result = util_convert_to_dict(tempResult)
    return result


def evaluate_expr(constraint, var_name, val):
    # Check notes for its logic
    t = simple_eval(constraint, names={var_name: val})
    if isinstance(t, bool):
        return t
    else:
        raise Exception("Not a valid boolean expression")


def validate_numeric_entity(values: List[Dict], invalid_trigger: str = None, key: str = None,
                            support_multiple: bool = True, pick_first: bool = False, constraint=None, var_name=None):
    """
    Validate an entity on the basis of its value extracted.
    The method will check if that value satisfies the numeric constraints put on it.
    If there are no numeric constraints, it will simply assume the value is valid.
    If there are numeric constraints, then it will only consider a value valid if it satisfies the numeric constraints.
    In case of multiple values being extracted and the support_multiple flag being set to true, the extracted values
    will be filtered so that only those values are used to fill the slot which satisfy the numeric constraint.
    If multiple values are supported and even 1 value does not satisfy the numeric constraint, the slot is assumed to be
    partially filled.
    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :param constraint: Conditional expression for constraints on the numeric values extracted
    :param var_name: Name of the var used to express the numeric constraint
    :return: a tuple of (filled, partially_filled, trigger, params)
    """

    filled = False
    partially_filled = False
    trigger = ""
    parameters = {}

    # Edge case
    if len(values) == 0:
        trigger = invalid_trigger
        SlotValidationResult = tuple([filled, partially_filled, trigger, parameters])
        return SlotValidationResult

    # No Constraints Edge case
    if constraint == "":
        filled = True
        if pick_first:
            parameters[key] = values[0]["value"]
            SlotValidationResult = tuple([filled, partially_filled, trigger, parameters])
            return SlotValidationResult

        parameters[key] = []
        for diction in values:
            parameters[key].append(diction["value"])
        SlotValidationResult = tuple([filled, partially_filled, trigger, parameters])
        return SlotValidationResult

    if len(values) > 0:
        partially_filled = True

    parameters[key] = []
    for diction in values:

        is_valid = evaluate_expr(constraint, var_name, diction["value"])
        if is_valid:
            parameters[key].append(diction["value"])
        else:
            trigger = invalid_trigger

    if trigger != invalid_trigger:
        filled = True
        partially_filled = False
    else:
        parameters = {}
    if pick_first:
        parameters[key] = values[0]["value"]

    SlotValidationResult = tuple([filled, partially_filled, trigger, parameters])
    return SlotValidationResult

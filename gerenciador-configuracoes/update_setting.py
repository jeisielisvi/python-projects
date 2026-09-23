def update_setting(setting_dict, setting_tuple):

    key, value = setting_tuple
    key = key.lower()
    value = value.lower()
    
    if key in setting_dict:
        setting_dict.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
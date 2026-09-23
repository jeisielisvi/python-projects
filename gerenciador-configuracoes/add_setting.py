def add_setting(setting_dict, setting_tuple):

    key, value = setting_tuple
    key = key.lower()
    value = value.lower()
    
    if key in setting_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    setting_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
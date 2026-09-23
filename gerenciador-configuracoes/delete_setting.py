def delete_setting(setting_dict, setting_key):

    key = setting_key.lower()

    if key in setting_dict:
        setting_dict.pop(key)
        return f"Setting '{key}' deleted successfully!"

    return 'Setting not found!'
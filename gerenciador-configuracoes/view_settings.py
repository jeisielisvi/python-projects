def view_settings(setting_dict):

    if not setting_dict:
        return "No settings available."

    return "Current User Settings:\n"+"\n".join(f"{key.capitalize()}: {value}" for key, value in setting_dict.items())+"\n"
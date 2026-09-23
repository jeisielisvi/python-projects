from add_setting import add_setting
from update_setting import update_setting
from delete_setting import delete_setting
from view_settings import view_settings
from data import test_settings

if __name__ == "__main__":
    print(add_setting(test_settings, ("THEME", "dark")))
    print(add_setting(test_settings, ("VOLUME", "high")))
    print(update_setting({'theme': 'light'}, ('theme', 'dark')))
    print(update_setting({'theme': 'light'}, ('volume', 'high')))
    print(delete_setting({'theme': 'light'}, 'theme'))
    print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
from add_setting import add_setting
from data import test_settings

if __name__ == "__main__":
    print(add_setting(test_settings, ("THEME", "dark")))
    print(add_setting(test_settings, ("VOLUME", "high")))
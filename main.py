test_settings = {
    'theme':'dark',
    'language':'enabled',
    'notifications':'high'
}
test_pair = ('Theme','white')

def add_setting(settings: dict, pair: tuple):
    key = pair[0].lower()
    value = pair[1].lower()
    if key in settings:
        return f'Setting {key} updated to {value} successfully!'
        #print(f'Setting {key} already exists! Cannot add a new setting with this name.')
    else:
        settings.update({key:value})
        return f'Setting {key} added with value {value}'
    pass

print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
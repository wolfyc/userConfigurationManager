test_settings = {
    'Theme':'dark',
    'Notifications':'enabled',
    'Volume':'high'
}

def delete_setting(settings: dict, key: str):
    key = key.lower()  
    
    if key in settings:  
        settings.pop(key)  
        return f"Setting '{key}' deleted successfully!" 
    return "Setting not found!"

def update_setting(settings:dict, pair:tuple):
    key, value = pair
    key=key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def add_setting(settings: dict, pair: tuple):
    key, value = pair

    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
        
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def view_settings(settings:dict):
    if settings == {}:
        return "No settings available."
    
    result = "Current User Settings:\n"
    
    
    for key, value in settings.items():
       
        cap_key = key.capitalize()
        result += f"{cap_key}: {value}\n"
    
    return result

print(view_settings(test_settings)) 
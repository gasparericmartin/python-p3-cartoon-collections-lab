def roll_call_dwarves(names):
    [print(f'{names.index(name) + 1}. {name}') for name in names]


def summon_captain_planet(names):
    return [name.capitalize() + '!' for name in names]

def long_planeteer_calls(calls):
    if [True for long in calls if len(long) > 4]:
        return True
    else:
        return False    

def find_the_cheese(items):
    if 'cheddar' in items:
        return 'cheddar'
    elif 'gouda' in items:
        return 'gouda'
    elif 'camembert' in items:
        return 'camembert'

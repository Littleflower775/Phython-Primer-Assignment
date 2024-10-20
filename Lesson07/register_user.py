user_list = []

def register_user(name, is_new=True):
    if is_new == True:
        user_list.append(name)
        print(f"Hi, {name}! Welcome to Code like a girl!")
    else:
        print(f"Hi, {name}! Welcome back!")
    return user_list

register_user('Julia')
register_user('Xiaoyu', False)
register_user('Cloe', True)
register_user('Jodie')

print(user_list)

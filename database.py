users = {}

def add_user(user_id):
    if user_id not in users:
        users[user_id] = {"plan": None}

def set_plan(user_id, plan):
    users[user_id]["plan"] = plan

def get_user(user_id):
    return users.get(user_id)

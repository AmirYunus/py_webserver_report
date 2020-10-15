def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}

    for each_event in events:
        if each_event.machine not in machines:
            machines[each_event.machine] = set()
        
        if each_event.type == "login":
            machines[each_event.machine].add(each_event.user)

        elif each_event.type == "logout" and each_event.user in machines:
            machines[each_event.machine].remove(each_event.user)
    
    return machines

def generate_report(machines):
    for each_machine, each_user in machines.items():

        if len(each_user) > 0:
            user_list = ", ".join(each_user)
            print(f"{each_machine}: {user_list}")

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
# print(users)

generate_report(users)
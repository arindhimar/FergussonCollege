import datetime

def get_current_date():
    return datetime.date.today().isoformat()

print(get_current_date())  
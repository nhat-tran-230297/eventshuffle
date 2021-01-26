from datetime import datetime

def validate_datetime(date_format):
    try:
        date = datetime.strptime(date_format, '%Y-%m-%d')
        if date.strftime('%Y-%m-%d') != date_format:
            return False
        
        return True
        
    except ValueError:
        return False


def validate_duplicate(dates):
    return len(dates) == len(set(dates))

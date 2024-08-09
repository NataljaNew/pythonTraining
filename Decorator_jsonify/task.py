import functools
import json
def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        json_data = json.dumps(value)
        return json_data
    return wrapper
def normalize(map):
    def decorator_normalize(func):
        def wrapper_normalize(*args, **kwargs):
            result = func(*args, **kwargs)
            return transform(map, result)
        return wrapper_normalize
    return decorator_normalize


def normalize_list(map):
    def decorator_normalize(func):
        def wrapper_normalize(*args, **kwargs):
            result = func(*args, **kwargs)
            normal_list = [transform(map, element) for element in result]
            return normal_list
        return wrapper_normalize
    return decorator_normalize


def transform(map, element):
    return {map[key]: value for key, value in element.items()}

def is_containe(validation_keys: list, checked_keys: list) -> bool:
    return set(validation_keys).issubset(set(checked_keys))

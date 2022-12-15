def is_containe(validation_keys: list, checked_keys: list) -> bool:
    return validation_keys == list(set(validation_keys) & set(checked_keys))

def get_column_in_case(columns, name):
    '''
    '''
    name_lower = name.lower()
    candidates = [column for column in columns if column.lower() == name_lower]
    if len(candidates) != 1:
        return None
    return candidates[0]

from typing import Dict, Any, Tuple

def build_insert_statement(mapped_dict: Dict[str, Any]) -> Tuple[str, str]:
    values_statement = ', '.join(f':{key}' for key in mapped_dict)
    fields_statement = values_statement.replace(':', '')
    return fields_statement, values_statement

def build_update_statement(mapped_dict: Dict[str, Any]) -> str:
    return ', '.join(f'{key} = :{key}' for key in mapped_dict)
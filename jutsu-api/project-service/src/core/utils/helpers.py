from datetime import datetime


def generate_project_name_key(name: str) -> str:
    """
    Generate a key from a given name.

    This function generates a key from a name by taking the first three characters
    of the name if the name is a single word. If the name consists of multiple words,
    it takes the first letter from each word.

    The generated key is returned in uppercase.

    Args:
        name (str): The name from which to generate a key.

    Returns:
        str: The generated key in uppercase.

    Examples:
        >>> generate_name_key("OpenAI")
        'OPE'

        >>> generate_name_key("Artificial Intelligence")
        'AI'
    """
    words = name.split()
    if len(words) == 1:
        name_key = words[0][:3].upper()
    else:
        name_key = ''.join([word[0] for word in words]).upper()
    return name_key


def generate_workflow_name(project_name_key: str, number: int = 1, name: str = "") -> str:
    """
    Generate a workflow name based on given parameters.

    This function generates a workflow name based on a provided project name key and number. 
    If a name is provided, it sanitizes it by replacing spaces with hyphens. 
    If no name is provided, it generates a name in the format of 'project_name_key-number-year'. 
    The number is formatted as a two-digit number, and the year is the last two digits of the current year.

    Args:
        project_name_key (str): The key of the project name.
        number (int, optional): A number to include in the workflow name. Defaults to 1.
        name (str, optional): A specific name for the workflow. Defaults to an empty string.

    Returns:
        str: The generated or sanitized workflow name.

    Examples:
        >>> generate_workflow_name("OPN", 2)
        'OPN-02-23'  # Assuming the current year is 2023

        >>> generate_workflow_name("OPN", name="Workflow Name")
        'Workflow-Name'
    """
    current_year = datetime.now().year % 100
    formatted_number = f"{number:02d}"

    if name:
        sanitized_name = '-'.join(name.split())
    else:
        sanitized_name = f'{project_name_key}-{formatted_number}-{current_year}'

    return sanitized_name


def format_datetime(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%d %H:%M:%S')

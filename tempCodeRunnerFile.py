def calculate_xfactor(age) -> int:
    """_summary_

    Args:
        age (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        int: _description_
    """
    if age <= 0:
        raise ValueError("Age cannot ve 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
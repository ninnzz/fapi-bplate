"""
Util functions.

Put all utility functions here.
Functions should be as granular as possible.
AVOID putting complex function and functions that deals with
application/business logic.

Some examples of function are
- convert_to_date
- generate_uuid
- delete_local_file
- etc
"""


def np_float_safe_convert(data) -> float:
    """
    Safe convert from numpy data types.

    :param data:
    :return:
    """
    try:
        return data.item()
    except BaseException:
        return data

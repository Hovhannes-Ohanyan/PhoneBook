import operator


def read_records_from_file(file_path):
    """
    Read records from a file.

    Parameters:
        file_path (str): The path to the file containing records.

    Returns:
        list: A list of records read from the file. Each record is represented as a list of strings.
    """
    records = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                record_data = line.strip().split(" ")
                records.append(record_data)
    except FileNotFoundError:
        print("File not found. Please make sure the path is correct")
    return records


def validate_record(record):
    """
    Validate a single record.

    Parameters:
        record (list): A list representing a record, containing name, surname, separator, and phone number.

    Returns:
        list: A list of validation errors for the record.
    """
    errors = []

    # Validate phone number
    if len(record[-1]) != 9 or not record[-1].isdigit():
        errors.append("Phone number should be 9 digits ")

    # Validate separator
    if record[-2] not in [":", "-"]:
        errors.append("Separator should be ':' or '-' .")

    return errors


def sort_records(records, sort_criteria, sort_order):
    """
     Sort records based on specified criteria and order.

     Parameters:
         records (list): A list of records to be sorted.
         sort_criteria (str): The criteria for sorting (Name, Surname, PhoneNumberCode).
         sort_order (str): The order for sorting (Ascending or Descending).

     Returns:
         list: A list of sorted records.
     """
    if sort_criteria == "Name":
        key_func = operator.itemgetter(0)
    elif sort_criteria == "Surname":
        key_func = operator.itemgetter(1)
    elif sort_criteria == "PhoneNumberCode":
        key_func = lambda record: int(record[3][:3]) if record[3][:3].isdigit() else float('inf')
    else:
        raise ValueError("Invalid sorting criteria")

    sorted_records = sorted(records, key=key_func, reverse=(sort_order == 'Descending'))
    return sorted_records

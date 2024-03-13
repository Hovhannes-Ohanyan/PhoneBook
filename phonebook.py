from utils import read_records_from_file, validate_record, sort_records


def main():
    """
    Main function for the PhoneBook console application.

    This function prompts the user to enter a file path containing records of a PhoneBook.
    It then reads the records from the file, validates each record, and sorts the records based on user-specified criteria.
    Finally, it displays the sorted records in the console.

    Returns:
        None
    """
    file_path = input("Enter the file path: ")

    try:
        records = read_records_from_file(file_path)
    except FileNotFoundError:
        print("File not found. Please make sure the path is correct.")
        return

    if records:
        print("Validating records:")
        validation_failed = False
        for i, record in enumerate(records, start=1):
            validation_errors = validate_record(record)
            if validation_errors:
                validation_failed = True
                print(f"Validation errors for line {i}: {', '.join(validation_errors)}")
        if not validation_failed:
            print("All records passed validation successfully.")

            sort_criteria = input("Please choose criteria (Name, Surname, PhoneNumberCode): ")
            sort_order = input("Please choose ordering (Ascending or Descending): ")

            sorted_records = sort_records(records, sort_criteria, sort_order)

            print("Sorted Records:")
            for record in sorted_records:
                print(' '.join(record))


if __name__ == "__main__":
    main()

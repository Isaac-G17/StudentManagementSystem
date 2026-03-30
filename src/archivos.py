import csv
import os

def save_csv(list_students, route, include_header=True):
    """
    Saves the student list to a CSV file.

    Parameters:
        list_students (list): List of students.
        path (str): File path.
        include_header (bool): Whether to include a header.

    Returns:
        None
    """
    if not list_students:
        print("Empty list, cannot be saved.\n")
        return

    try:
        final_route = os.path.join("data", route)

        with open(final_route, "w", newline="", encoding="utf-8") as archive:
            writer = csv.writer(archive)

            if include_header:
                writer.writerow(["Id", "name", "age","course","status"])

            for s in list_students:
                writer.writerow([s["id"], s["name"], s["age"], s["course"], s["status"]])

        print(f"List of students saved in: {final_route}\n")

    except PermissionError:
        print("Error: You do not have permission to write to that path.\n")
    except Exception as e:
        print(f"Error: saving file: {e}\n")



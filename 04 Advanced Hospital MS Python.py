class Data:
    def _init_(self):
        self.age = 0
        self.room = 0
        self.name = ""
        self.address = ""
        self.disease = ""
        self.gender = ""
        self.description = ""
class Node:
    def _init_(self):
        self.data = Data()
        self.next = None

def create_dataframe(head):
    data = []
    while head is not None:
        patient_data = {
            "Name": head.data.name,
            "Address": head.data.address,
            "Gender": head.data.gender,
            "Disease": head.data.disease,
            "Description": head.data.description,
            "Age": head.data.age,
            "Room No.": head.data.room
        }
        data.append(patient_data)
        head = head.next

    df = pd.DataFrame(data)
    return df

def save_dataframe_as_csv(df, filename):
    df.to_csv(filename, index=False)
    print("DataFrame saved as", filename)

def load_dataframe_from_csv(filename):
    try:
        df = pd.read_csv(filename)
        print("DataFrame loaded from", filename)
        return df
    except FileNotFoundError:
        print("File", filename, "not found. Creating a new DataFrame.")
        return pd.DataFrame()

def menu():
    print("1 - Add OPD Patient")
    print("2 - Delete Patient")
    print("3 - Search by Name")
    print("4 - Search by Room No.")
    print("5 - Search by Age")
    print("6 - List Length")
    print("7 - Print Whole List")
    print("8 - Change Patient Name")
    print("9 - Add Emergency Patient")
    print("10 - Remove Duplicates")
    print("11 - Save Data as CSV\n\n")

def main():
    head = None
    print("\n\nHospital Management System")
    menu()
    filename = "patient_data.csv"
    df = load_dataframe_from_csv(filename)


def insert_front(head, data):
    temp = Node()
    temp.data = data
    temp.next = head
    head = temp
    return head


def append(head, data):
    temp = Node()
    temp.data = data
    temp.next = None
    if head is None:
        head = temp
        return head

    last = head
    while last.next is not None:
        last = last.next
    last.next = temp
    print("Append Completed!")
    return head


def change_node(head, data, new_data):
    while head is not None:
        if head.data.name == data.name:
            head.data = new_data
            break
        head = head.next


def change_node_by_name(head, data, new_data):
    while head is not None:
        if head.data.name == data:
            head.data.name = new_data
            break
        head = head.next


def print_linked_list(head):
    if head is None:
        print("Head is None")
        return
    print("Name\tAddress\tGender\tDisease\tDescription\tAge\tSpecialist No.")
    while head.next is not None:
        print(
            head.data.name,
            "\t",
            head.data.address,
            "\t",
            head.data.gender,
            "\t",
            head.data.disease,
            "\t",
            head.data.description,
            "\t",
            head.data.age,
            "\t",
            head.data.room,
        )
        head = head.next
    print(
        head.data.name,
        "\t",
        head.data.address,
        "\t",
        head.data.gender,
        "\t",
        head.data.disease,
        "\t",
        head.data.description,
        "\t",
        head.data.age,
        "\t",
        head.data.room,
    )


def list_length(head):
    temp = 0
    if head is None:
        print("Node is empty")
        return 0
    while head.next is not None:
        temp += 1
        head = head.next
    return temp + 1


def delete_element(head, loc):
    temp = head
    if head is None:
        print("Node is null")
        return
    for i in range(1, loc):
        temp = temp.next
        if i < loc:
            head = head.next
    head.next = temp.next


def search_list(head, v):
    if head is None:
        print("Node is empty, returning None")
        return None
    l = 1
    while head.next is not None and head.data.name != v.name:
        head = head.next
        l += 1
    print("Element found at location:", l)
    return head


def search_list_by_name(head, v):
    if head is None:
        print("Node is empty, returning None")
        return None
    l = 1
    while head.next is not None and head.data.name != v:
        head = head.next
        l += 1
    print("Element found at location:", l)
    return head


def input_patients():
    p = Data()
    p.name = input("Enter Patient Name: ")
    p.address = input("Enter Patient Address: ")
    p.disease = input("Enter Patient Disease: ")
    p.gender = input("Enter Patient Gender: ")
    p.description = input("Enter Disease Description: ")
    p.room = int(input("Enter Patient Special Room No.: "))
    p.age = int(input("Enter Patient Age: "))
    print("Input Function Completed!")
    return p


def get_patient_details():
    p = Data()
    p.name = input("Enter Patient Name: ")
    p.address = input("Enter Patient Address: ")
    p.disease = input("Enter Patient Disease: ")
    p.gender = input("Enter Patient Gender: ")
    p.description = input("Enter Disease Description: ")
    p.room = int(input("Enter Patient Special Room No.: "))
    p.age = int(input("Enter Patient Age: "))
    print("Input Function Completed!")
    return p


def search_by_room(head, room_no):
    found = False
    while head is not None:
        if head.data.room == room_no:
            print("Patient found:")
            print("Name:", head.data.name)
            print("Address:", head.data.address)
            print("Gender:", head.data.gender)
            print("Disease:", head.data.disease)
            print("Description:", head.data.description)
            print("Age:", head.data.age)
            found = True
            break
        head = head.next

    if not found:
        print("Patient with Room No.", room_no, "not found.")


def search_by_age(head, age):
    found = False
    while head is not None:
        if head.data.age == age:
            print("Patient found:")
            print("Name:", head.data.name)
            print("Address:", head.data.address)
            print("Gender:", head.data.gender)
            print("Disease:", head.data.disease)
            print("Description:", head.data.description)
            print("Room No.:", head.data.room)
            found = True
        head = head.next

    if not found:
        print("Patient with Age", age, "not found.")


def remove_duplicates(head):
    if head is None or head.next is None:
        return head

    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data.name == current.data.name:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    print("Duplicates removed.")
    return head

def save_dataframe_as_csv(df, filename):
    df.to_csv(filename, index=False)
    print("DataFrame saved as", filename)


def menu():
    print("1 - Add OPD Patient")
    print("2 - Delete Patient")
    print("3 - Search by Name")
    print("4 - Search by Room No.")
    print("5 - Search by Age")
    print("6 - List Length")
    print("7 - Print Whole List")
    print("8 - Change Patient Name")
    print("9 - Add Emergency Patient")
    print("10 - Remove Duplicates")
    print("11 - Save Data as CSV\n\n")

def main():
    head = None
    print("\n\nHospital Management System")
    menu()
    filename = "patient_data.csv"
    df = None
    while True:
        try:
            op = int(input("Select an option: "))
        except ValueError:
            break
        if op == 1:
            print("Enter Patient Details Below")
            patient = get_patient_details()
            head = append(head, patient)
        elif op == 2:
            if list_length(head) < 2:
                print("Length is less than two.\nTerminating program")
                break
            else:
                loc = int(input("Enter the location of the patient to delete: "))
                head = delete_element(head, loc)

        elif op == 3:
            name_to_search = input("Enter name to search patient: ")
            search_list_by_name(head, name_to_search)

        elif op == 4:
            room_no = int(input("Enter Room No. to search patient: "))
            search_by_room(head, room_no)

        elif op == 5:
            age = int(input("Enter Age to search patient: "))
            search_by_age(head, age)

        elif op == 6:
            print("You have", list_length(head), "Patients in your Hospital.")

        elif op == 7:
            print_linked_list(head)

        elif op == 8:
            old_name = input("Enter old name: ")
            new_name = input("Enter new name: ")
            head = change_node_by_name(head, old_name, new_name)

        elif op == 9:
            patient = get_patient_details()
            head = insert_front(head, patient)

        elif op == 10:
            head = remove_duplicates(head)
        elif op == 11:
            df = create_dataframe(head)
            save_dataframe_as_csv(df, filename)

        else:
            print("Wrong option selected")

        menu()


if _name_ == "_main_":
    main()
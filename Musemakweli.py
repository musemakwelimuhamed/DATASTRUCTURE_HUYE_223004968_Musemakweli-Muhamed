print("ONLINE EXAM REGISTRATION SYSTEM")




from collections import deque

class OnlineExamRegistration:
    def __init__(self):
        self.available_exams = []       # List of available exams
        self.pending_queue = deque()    # Queue for pending registrations
        self.undo_stack = []            # Stack for undoing registrations
    
   
    def add_exam(self, exam_name):
        self.available_exams.append(exam_name)
        print(f"Exam '{exam_name}' added to available exams.")
    
    
    def register_for_exam(self, exam_name):
        if exam_name in self.available_exams:
            self.pending_queue.append(exam_name)
            self.available_exams.remove(exam_name)
            self.undo_stack.append(('register', exam_name))
            print(f"Successfully registered for '{exam_name}'.")
        else:
            print(f"Exam '{exam_name}' is not available or already registered.")
    
   
    def undo_last_action(self):
        if not self.undo_stack:
            print("No actions to undo.")
            return
        last_action, exam_name = self.undo_stack.pop()
        if last_action == 'register':
            self.pending_queue.remove(exam_name)
            self.available_exams.append(exam_name)
            print(f"Registration for '{exam_name}' undone.")
    
   
    def view_available_exams(self):
        if not self.available_exams:
            print("No available exams.")
        else:
            print("Available Exams:")
            for exam in self.available_exams:
                print(f"- {exam}")
    
   
    def view_pending_registrations(self):
        if not self.pending_queue:
            print("No pending registrations.")
        else:
            print("Pending Registrations:")
            for exam in self.pending_queue:
                print(f"- {exam}")
    
   
    def view_undo_stack(self):
        if not self.undo_stack:
            print("Undo stack is empty.")
        else:
            print("Undo Stack:")
            for action, exam in self.undo_stack:
                print(f"- {action} '{exam}'")



def menu():
    registration_system = OnlineExamRegistration()
    
    while True:
       
        print("1. Add a new exam")
        print("2. Register for an exam")
        print("3. Undo last registration")
        print("4. View available exams")
        print("5. View pending registrations")
        print("6. View undo stack")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            exam_name = input("Economics: ")
            registration_system.add_exam(exam_name)

        elif choice == '2':
            exam_name = input("Enter the exam name to register for: ")
            registration_system.register_for_exam(exam_name)

        elif choice == '3':
            registration_system.undo_last_action()

        elif choice == '4':
            registration_system.view_available_exams()

        elif choice == '5':
            registration_system.view_pending_registrations()

        elif choice == '6':
            registration_system.view_undo_stack()

        elif choice == '7':
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")



menu()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"User Name: {self.name}")
        print(f"User Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
        self.content = []

    def upload_contents(self, content):
        self.content.append(content)
        print(f"Uploaded Content Successfully: {self.content}")

    def display_info(self):
        super().display_info()
        print("Role: Instructor")
        print(f"Subject expertise: {self.subject}")

class CourseCreator(Instructor):
    def _init__(self, name, email, subject):
        super().__init__(name, email, subject)
        # self.courses = {}

    def create_course(self, course_name, module):
        self.courses = {}
        self.courses[course_name] = module
        print(f"Course {course_name} created with modules: {module}")
    
    def display_info(self):
        super().display_info()
        print("Role: Course Creator")
        #print(f"Courses Created: {list(self.courses.keys())}")

C1 = CourseCreator("Nisarg Patel", "kbnisargpatel001454@gmail.com", "Artificial Intelligence")
C1.display_info()
C1.upload_contents("Introduction to Deep Learning")
C1.create_course("Deep Learning", {"Module-1":"Basics", "Module-2":"Algorithms"})
C1.display_info()

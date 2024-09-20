from mongoengine import Document, connect, StringField, ListField, ReferenceField, DoesNotExist, ValidationError
from flask import Flask, request, jsonify, render_template

# Create a Flask app
app = Flask(__name__)

# Connect to MongoDB
connect(db='quran_academy', host='127.0.0.1', port=27017)

# Define the Teacher model
class Teacher(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)  # Email must be unique

# Define the Student model
class Student(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)  # Email must be unique

# Define the Class model
class Class(Document):
    title = StringField(required=True)
    teacher = ReferenceField(Teacher, required=True)
    students = ListField(ReferenceField(Student))

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a new teacher
@app.route('/add_teacher', methods=['POST', 'GET'])
def add_teacher():
    if request.method == 'GET':
        # Render the HTML form for GET requests
        return render_template('add_teacher.html')
    
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()

            # Check if a teacher with the same email already exists
            existing_teacher = Teacher.objects(email=data['email']).first()
            if existing_teacher:
                return jsonify(message="Teacher with this email already exists"), 400
            
            # Create a new teacher if no duplicate is found
            teacher = Teacher(name=data['name'], email=data['email'])
            try:
                teacher.save()
            except ValidationError as e:
                return jsonify(error=str(e)), 400

            return jsonify(message="Teacher added successfully!")
        else:
            return jsonify(error="Unsupported Media Type. Please send JSON data."), 415

# Route to add a new student
@app.route('/add_student', methods=['POST', 'GET'])
def add_student():
    if request.method == 'GET':
        return render_template('add_student.html')
    
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()

            # Check if a student with the same email already exists
            existing_student = Student.objects(email=data['email']).first()
            if existing_student:
                return jsonify(message="Student with this email already exists"), 400
            
            student = Student(name=data['name'], email=data['email'])
            try:
                student.save()
            except ValidationError as e:
                return jsonify(error=str(e)), 400

            return jsonify(message="Student added successfully!")
        else:
            return jsonify(error="Unsupported Media Type. Please send JSON data."), 415

# Route to create a new class and assign to a teacher
@app.route('/create_class', methods=['POST', 'GET'])
def create_class():
    if request.method == 'GET':
        return render_template('create_class.html')
    
    if request.method == 'POST':
        data = request.get_json()

        # Find the teacher in the database by email
        teacher = Teacher.objects(email=data['teacher_email']).first()
        if not teacher:
            return jsonify(message="Teacher not found"), 404
        
        # Create a new class
        new_class = Class(title=data['title'], teacher=teacher)
        try:
            new_class.save()
        except ValidationError as e:
            return jsonify(error=str(e)), 400

        return jsonify(message="Class created successfully!")

# Route to enroll a student in a class
@app.route('/enroll_student', methods=['POST', 'GET'])
def enroll_student():
    if request.method == 'GET':
        return render_template('enroll_student.html')
    
    if request.method == 'POST':
        data = request.get_json()

        # Find the student and class from the database
        student = Student.objects(email=data['student_email']).first()
        class_ = Class.objects(title=data['class_title']).first()

        if not student:
            return jsonify(message="Student not found"), 404
        if not class_:
            return jsonify(message="Class not found"), 404

        # Enroll the student in the class
        if student not in class_.students:
            class_.students.append(student)
            class_.save()

        return jsonify(message="Student enrolled successfully!")

# Route to get all students in a specific class
@app.route('/class_students/<class_title>', methods=['GET'])
def class_students(class_title):
    class_ = Class.objects(title=class_title).first()

    if not class_:
        return jsonify(message="Class not found"), 404

    # Get the list of students in the class
    students = [student.name for student in class_.students]

    # Render the class_students.html template and pass the students
    return render_template('class_students.html', students=students)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

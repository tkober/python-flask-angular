from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema

# Create a Flask application
app = Flask(__name__)

# Build DB Schema, if needed
Base.metadata.create_all(engine)

@app.route('/exams')
def get_exams():
    # Fetch exams from DB
    session = Session()
    exam_objects = session.query(Exam).all()

    # Transform to JSON-serialaizable objects
    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)
    print(exams)

    # Close DB session
    session.close()

    # Serialize to JSON and return it
    return jsonify(exams)


@app.route('/exams', methods=['POST'])
def add_exam():
    # Mount exam object
    posted_exam = ExamSchema(only=('title', 'description')).load(request.get_json())

    exam = Exam(**posted_exam, created_by='HTTP post request')

    # Persist exam
    session = Session()
    session.add(exam)
    session.commit()

    # Return created exam
    new_exam = ExamSchema().dump(exam)
    session.close()
    return jsonify(new_exam), 201
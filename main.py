from backend.src.entities.entity import Session, engine, Base
from backend.src.entities.exam import Exam

if __name__ == '__main__':

    # Build DB Schema
    Base.metadata.create_all(engine)

    # Start a session
    session = Session()

    # Check for existing data
    exams = session.query(Exam).all()

    if len(exams) == 0:
        # Create and persist mock exam
        python_exam = Exam(
            title='SQLAlchemy Exam',
            description="Test your knowledge about SQLAlchemy.",
            created_by='script'
        )
        session.add(python_exam)
        session.commit()
        session.close()

        # Reload exams
        exams = session.query(Exam).all()

    # Show existing exams
    print('### Exams:')
    for exam in exams:
        print(f'({exam.id}) {exam.title} - {exam.description}')

% Database of students, teachers, subjects, and subject codes

% Format: student_teacher_subject(Student, Teacher, Subject, SubjectCode).
student_teacher_subject('Alice', 'Mr. Smith', 'Math', 'MTH101').
student_teacher_subject('Bob', 'Mrs. Johnson', 'Science', 'SCI202').
student_teacher_subject('Charlie', 'Mr. White', 'History', 'HIS303').
student_teacher_subject('David', 'Ms. Brown', 'English', 'ENG404').
student_teacher_subject('Eva', 'Mrs. Green', 'Math', 'MTH101').
student_teacher_subject('Frank', 'Mr. Smith', 'Math', 'MTH101').

% Query to get the teacher, subject, and subject code based on the student name
get_teacher_and_subject(Student, Teacher, Subject, SubjectCode) :-
    student_teacher_subject(Student, Teacher, Subject, SubjectCode).

% Query to find all students taught by a specific teacher
get_students_by_teacher(Teacher, Student) :-
    student_teacher_subject(Student, Teacher, _, _).

% Query to find the subject and teacher based on the subject code
get_subject_by_code(SubjectCode, Subject, Teacher) :-
    student_teacher_subject(_, Teacher, Subject, SubjectCode).

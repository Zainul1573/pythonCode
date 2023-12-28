

dict_1 = {
    'Student1': {
        'Name': 'Nizar',
        'Age': 20,
        'Subject':{
          'Maths': 'B',
          'English': 'C'}
        },

    'Student2': {
        'Name': 'Zainul',
        'Age': 19,
        'Subject': {
          'Maths': 'C',
          'English': 'A'}
    }
}
print()
for student, info in dict_1.items():
    print(student)
    for key, value in info.items():
        if key == 'Subject':
            print(f'  {key}:')
            for subject, grade in value.items():
                print(f'    {subject}: {grade}')
        else:
            print(f'  {key}: {value}')

"""
student_name = dict_1['Student1']['Name']
student_age = dict_1['Student1']['Age']
student_maths = dict_1['Student1']['Subject']['Maths']
student_english = dict_1['Student1']['Subject']['English']

maths = dict_1['Student1']['Subject']['Maths']
print(maths)

print(f'Name :  {student_name}')
print(f'Age :- {student_age}')
print('----Exam Results:----')
print(f'   Maths :- {student_maths}')
print(f'   Maths :- {student_english}')

"""
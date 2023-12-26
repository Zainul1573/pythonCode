# test


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
print(dict_1)
student_name = dict_1['Student1']['Name']
student_age = dict_1['Student1']['Age']
student_maths = dict_1['Student1']['Subject']['Maths']

maths = dict_1['Student1']['Subject']['Maths']
print(maths)

print(f'Name :  {student_name}')
print(f'Age :- {student_age}')
print('----Exam Results:----')
print(f'   Maths :- {student_maths}')
print(f'   Maths :- {student_maths}')
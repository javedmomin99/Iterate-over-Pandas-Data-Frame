student_dict = {
  "student" : ["Javed","Sajid","Shafi"],
  "score" : [50,80,90]
}
#for (key,value) in student_dict.items():
#  print(key,value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

#Loop through a Data Frame
#for (key,value) in student_data_frame.items():
#      print(value)

#Loop through Rows of a Data Frame 
#for (index,row) in student_data_frame.iterrows():
#      print(row)

#for (index, row) in student_data_frame.iterrows():
#    print(row.student)

#for (index, row) in student_data_frame.iterrows():
#    print(row.score)

#Loop through a Data Frame with a Condition
for (index, row) in student_data_frame.iterrows():
    if row.student == "Javed":
      print(row.score)



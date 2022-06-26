About :-
This is a python project to read a JSON file and convert it into excel format.
Either the entire json or a part of it can be converted.
The node path can be entered in one of the following ways :-
object.field1.field2....
array.1.field1.field2... (1 may be replaced by other numerical values)

System Requirements :-
The only system requirement is a working python setup on the machine along with the required modules for the project.

Program :-
The python source file 'json_logger.py' is the only file required to run this program.
Generated excel files will be stored in the 'logs' folder of the directory by the name of the node path that is provided.

Input :-
Replace the "file.json" with the appropriate JSON source file in the directory.
Alternatively, you may provide the absolute path of the file to the program by replacing the file location in line 4.
=> file_path = "file.json" #Provide the path here.
(Note : It is necessary for the source file to be a '.JSON' file.)

Output :-
As per the node path provided, the obtained json will be converted into an excel file with the help of pandas library.
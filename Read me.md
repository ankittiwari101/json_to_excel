About :-
This is a python project to parse a JSON log file and convert it into appropriate '.column' files.

System Requirements :-
The only system requirement is a working python setup on the machine.

Program :-
The python source file 'json_logger.py' is the only file required to run this program.
Generated column files will be stored in the 'logs' folder of the directory. Make sure to not delete or rename it.

Input :-
Replace the "file.json" with the appropriate JSON source file in the directory.
Alternatively, you may provide the absolute path of the file to the program by replacing the file location in line 3.
=> file_path = "file.json" #Provide the path here.
(Note : It is not necessary for the source file to be a '.JSON' file.Just that it should have a valid JSON object on each line of the file.)

Output :-
As per the structure of the given JSON objects, for every unique field a new '.column' file will be generated in the 'logs' folder with 
appropriate data entry corresponding to values of those particular fields.
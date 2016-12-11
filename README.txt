Name : UPASNA MENON    UIN:659574838

README for question 1)Entity Resolution
Steps to follow while executing:
clean.py:
1) Install python3
2) Install pyenchant library using https://www.howtoinstall.co/en/ubuntu/precise/universe/python3-enchant/.
3) Run the command : python3 clean.py > cleaned.txt 
   Here, output of clean.py is saved into another file cleaned.txt.
4) Now, open cleaned.txt to get the cleaned data by : vi cleaned.txt
5) The output may take upto 40 seconds.It comes as a list of "Professor last name" - "Courses"
   The list of professors and his corresponding courses are listed.The duplicate values and spell checks
   are corrected.Also, professor's courses are merged ; each professor appears once.

query.py
1)The query.py python file has to be executed as follows:
  python3 query.py cleaned.txt
  Here, the "cleaned.txt" file is given as input to query.py to query data from the cleaned data.
2)The answers to each of the 3 queries are obtained.

Description of transformation rules:( What is actually happening)
* Each line from the "class.txt" file is read .
* We need to split each line by "-" to obtain  list of professors and a list of courses.
* Since we only need the last names of professors we need to further split and filter.
* Some of the professor names are of the form 
1)Kshemkalyani, Ajay , 2)Craig D. Foster ,3)Lu, V Hui ,4)Tanya.Bergerwolf ,5)A. Prasad Sistla and a few more..
* Since each one is in a differenet format we apply transformation rules to get only the last names:
1) Ex :Split the "," in case the prof name is of form "Lu, V Hui" and take only the 1st split part to obtain "Lu"
2) Ex :Split the "." in case the prof name is of form  "Craig D. Foster" and take only the last split part to obtain "Foster"


Creating dictionary of unique professors with courses:
* I created a dictionary "prof_course_dict" to merge professors who are repeating and append their courses.

SpellChecking:
* I installed the pyenchant library to perform spell checking.
* Each course name's word was extracted and passed to a function which did explicit spell checks to check all conditions
  using pyenchant.
* The list of sugeestions given by pyenchant were analyzed using the edit distance function to find the most probable word.

Edit Distance:
* The function for edit distnace was borrowed from stackoverflow -http://stackoverflow.com/questions/2460177/edit-distance-in-python   

Jaccard Distance:
* The Jaccard Distance was used for query3 to obtain professor names with identical courses.
* The function for Jaccard Distance was borrowed from - http://www.bogotobogo.com/python/python_sets_union_intersection.php



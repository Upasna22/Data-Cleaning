import sys
import fileinput
import string

def query():

    part =[]
    professors =[]
    courses =[]
    course =[]
    for stuff in fileinput.input():
        stuff = stuff.strip()
        part.append(stuff)

    for c in part:
        parts = c.split(" - ")
        professors.append(parts[0])
        courses.append(parts[1])

    cou=[]


    cr =[]
    for j in range(0,len(courses)):
        cp =courses[j].split("|")
       # print(cp)
        while '' in cp:
            cp.remove('')


        for k in range(0,len(cp)):
            cou.append(cp[k])
        #for j in range(0,len(cp)):
         #   cr = cp[j].split(",")
       # print(cr)
#print (cou)

    print("How many distinct courses does this dataset contain?:")

    query1 =q1(cou)
    print(query1)
    print("\n")
    print("List all the courses (in alphabetical order) taught by Professor Mitchell Theys: ")
    q2(professors,courses)
    print("\n")
    print("The two professors have the most aligned teaching interests based on course titles are: ")
    q3(professors,courses)





def q1(course_src):


    course_distinct= set(list(course_src))
    l = len(course_distinct)
    return l


def q2(professors,courses):

    c1 =[]
    for i in range(0,len(courses)):

       if professors[i]=="Theys ":

           c1 =courses[i].split("|")
           while '' in c1:
               c1.remove('')

           print(c1)


def q3(professors,courses):

    cr =[]
    for j in range(0,len(courses)):
        cr.append([])
        crs=courses[j].split("|")
        while '' in crs:
            crs.remove('')
        l=len(crs)
        #print (crs)
        for k in range(0,l):
            cr[j].append(crs[k])

    prof=[]
    jacc=[]
    profs =[]
    for i in range(0,len(professors)):
        if(len(cr[i]) >4):
           prof.append(professors[i])
    for i in range(0,len(prof)):
        profs.append([])
        for j in range(1,len(prof)):
            profs.append([prof[i],prof[j]])
            jacc.append(jaccard(cr[i],cr[j]))

    j1=max(jacc)
   # print(j1)
    p=jacc.index(j1)
  #  print(p)
    print (profs[p])



def jaccard(s1, s2):
    " takes two lists as input and returns Jaccard coefficient"
    st1=set(s1)
    st2=set(s2)
    u = set(st1).union(st2)
    i = set(st1).intersection(st2)
    return len(i)/len(u)



if __name__ == '__main__':
    query()
                                      
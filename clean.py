import sys
import fileinput
import enchant
import string
import re, string ,timeit

def parta():
    def  __init__(self, prof_lastname):
        self.prof_lastname =prof_lastname


    prof=[]
    course=[]
    result =[]
    for line in open("class.txt"):
        line = line.strip()
        parts = line.split(" - ")
        course.append(parts[1])
        prof.append(parts[0])


        result =[]
        prof_lastname =[]
        for c in range(0,len(prof)):
            if ',' in prof[c]:
                prof_parts = prof[c].split(",")
                prof_lastname.append( prof_parts[0])
            elif '.' in prof[c]:
                prof_parts =prof[c].split(".")
                if ' ' in prof_parts[-1]:
                    prof_p2 = prof_parts[-1].split(" ")
                    prof_lastname.append( prof_p2[-2])
                else:
                    prof_lastname.append( prof_p2[-1])
            else:
                prof_parts = prof[c].split(" ")
                prof_lastname.append( prof_parts[-2])
        arr = prof_lastname
        for c in range(0,len(arr)):
            arr[c] =arr[c].title()
        course_p =[]
        course_t =[]
    prof_course_dict = {}
    courses =[]
    key_d= prof_course_dict.keys()
    for i in range(len(course)):
        if arr[i] in key_d:
            if "|" in course[c]:
                course_parts =course[c].split("|")
                for j in range(0,len(course_parts)):
                    t= prof_course_dict[arr[i]] + '|' +course_parts[i]
                    prof_course_dict[arr[i]] = t
            else:
                t= prof_course_dict[arr[i]] + '|' +course[i]
                prof_course_dict[arr[i]] = t
        else:
            if "|" in course[c]:
                course_parts =course[c].split("|")
                for j in range(0,len(course_parts)):
                    prof_course_dict[arr[i]] = course_parts[j]
            else:
                prof_course_dict[arr[i]] = course[i]
    li=list(prof_course_dict.values())
    cof=[]
    for i in range(0,len(course)):
        cof.append([])
        if "|" in course[i]:
            cou_par =course[i].split("|")
            for j in range(len(cou_par)):
                sa=spell_check(cou_par[j])
                if (j==(len(cou_par))-1):
                    cof[i].append(sa)

                else:
                    cof[i].append(sa)

        else:
            sa=spell_check(course[i])
            cof[i].append(sa)


 ##################################################################33/

    prof_dict ={}


    pro= list(prof_course_dict.keys())
    pro.sort()
    #print (pro)
    for i in range(0,len(pro)):
        print( pro[i]+ "|   - ",end='')
        for j in range(0,len(arr)):
            if pro[i]==arr[j]:
                for k in range(0,len(cof[j])):
                    print ("|"+cof[j][k],end='')
        print ("")

def spell_check(s1):

    s12=[word.strip(string.punctuation) for word in s1.split(" ")]
    while '' in s12:
       s12.remove('')
    #print (s1)
    for i in range(0,len(s12)):
        s=spellcheck(s12[i])
        s1=s1.replace(s12[i],s)
    if '&' in s1:
        s1=s1.replace('&','And')
    if '.' in s1:
        s1=s1.replace('.','')
    s13=[word.strip(string.punctuation) for word in s1.split(" ")]
    while '' in s13:
       s13.remove('')
    for i in range(0,len(s13)):
        if s13[i]=='Intro':
            s1=s1.replace(s13[i],'Introduction')
        if 'z' in s13[i][-1]:
            s =s13[i].replace('z','s')
            s1 = s1.replace(s13[i],s)
    return s1
def spellcheck(s1):


#    print(s1)

    spel = enchant.Dict("en_US")

    if(spel.check(s1))==False:
        sim = spel.suggest(s1)

        flag=0
        if(len(s1)>3 and len(sim[0])==len(s1) and flag==0 and editDistance(s1,sim[0])<3):
            s1=sim[0]
            flag=1
        if(len(s1)>3 and len(sim[2])==len(s1) and flag==0 and editDistance(s1,sim[2])<3):
            s1=sim[2]
            flag=1
        if(len(s1)>3 and len(sim[1])==len(s1) and flag==0 and editDistance(s1,sim[1])<3):
            s1=sim[1]
            flag=1
        return s1.title()
    else:
        return s1.title()


def editDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                 distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

#print(editDistance("Hellowoorld","Halloworld"))


def DistJaccard(str1, str2):
    str1 = set(str1.split())
    str2 = set(str2.split())
    return float(len(str1 & str2)) / len(str1 | str2)
#print(DistJaccard("hola amigo","chao amigo"))


if __name__ == '__main__':
    parta()


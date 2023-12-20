

#function - add location of new camps 
def addloc(cmp):
    dd=cmp[0:2]
    ln=len(planned)
    if ln==0:
        planned.append(cmp)
    else:
        last=planned[ln-1]
        if int(dd)>=int(last[0:2]):
            planned.append(cmp)
        else:
            for i in range(ln):
                cp=planned[i]
                if int(dd)<=int(cp[0:2]):
                    planned.insert(i,cmp)
                    break

#function - conducted camps                
def conductCamp(cmp):
    conducted.append(cmp)
    planned.remove(cmp)
def search(cmp,lst):
    ln=len(lst)
    for i in range(ln):
        if cmp in list[i]:
            return lst[i]
    else:
        return False
    
#function - search conducted camps
def search(cmp,lst):
    ln=len(lst)
    for i in range(ln):
        if cmp in lst[i]:
            return lst[i]
#function - report of conducted camps
def report():
    lenp = len(planned)
    lenc=len(conducted)
    print("\t REPORT")
    print("-----\t-----")
    print("Camps conducted so far:",lenc)
    print("People served so far",ppl)
    print("Camps to be conducted so far",lenp)
    print("-----\t-----")

#function - Display report of conducted camps
def Display():
    print("\Camps Planned :",end='')
    for i in planned:
        print(i,end=',')
    print("...!")
    print("\nCamps Conducted so far :",end='')
    for i in conducted:
        print(i,end=',')
    print("...!!")
#Main part of the program
planned=[]
conducted=[]

ppl=0
ch=0

while(ch!=6):
    print("\t---")
    print("MENU")
    print('\t--')
    print("1.Add Camp Location")
    print("2.Camp conducted")
    print("3.Look for a Camp")
    print("4.report")
    print("5.Display list")
    print("6.EXIT")

    ch= int(input("Enter your choice"))
    if ch==1:
        cm=input("Enter camp location:")
        dd=input("Enter the date of the month(only in dd format)")
        cmp=dd+cm
        addloc(cmp)
    
    if ch==2:
        cm=input("Camp conducted at location?")
        p=int(input("How many people are seved at this camp?"))
        ppl=ppl+p
        result=search(cm,planned)
        if result==False :
            print("Sorry no such camp in the list")
        else:
            conductCamp(result)
    
    elif ch==3:
        cm =input("Enter the camp location:")
        r1=search(cm,planned)
        if r1==False:
            r2=search(cm,conducted)
            if r2==False:
                print("Sorry ,no such camp exists in the list")
            else:
                dd=r2[0:2]
                print(cm,"was conducted on the date",dd,"of this month")
        else:
            dd=r1[0:2]
            print(cm,"Camp is to be conducted on date",dd,"of this month")
    elif ch==4:
            report()
    elif ch==5:
            Display()
    elif ch!=6:
        print("Wrong Choice!")
else:
    print("THNAK YOU!!")


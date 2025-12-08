##__________________________________________________________________
##|  price     |  members   | duration   |   time     | location   |
##|____________|____________|____________|____________|____________|
##|  $10       |  2         | 1hr        |  12:00     |  home      |
##|____________|____________|____________|____________|____________|
##|  $20       |  4         | 2hr        |  5:00      |  in town   |
##|____________|____________|____________|____________|____________|
##|  $50+      |  6+        | 3hr+       |  9:00+     |  far away  |
##|____________|____________|____________|____________|____________|

print(""" 
      This program is intended to assist you in choosing an activity based on the inputs you give it.
      It holds a list of options and rules out all options that dont fit the constraints.
      
      """)

options = ["movie theater","cards","movie at home","lunch out","concert","shopping","dinner out","videogame","escape room"]

def gather():
   price, members, duration, time, location=None,None,None,None,None
   if price==None:
      def pr():
         p=input("Enter your available budjet or press enter to skip: ")
         if p=='':
              return(p)
         elif int(p)>=0:
            return(int(p))
         elif p=="50+":
            return(50)
         else:
            print("Invalid input: try entering without the '$'")
            return(pr())
      price=pr()
   if members==None:
      def me():
         m=input("Enter your group size or press enter to skip: (2) (4) (6+) ")
         if m=='':
              return(m)
         if int(m)==2 or int(m)==4 or int(m)==6:
            return(int(m))
         elif m=="6+":
            return(6)
         else:
            print("Invalid input")
            return(me())
      members=me()
   if duration==None:
      def du():
         d=input("Enter your time constraint or press enter to skip: (1hr) (2hr) (3hr+) ")
         if d=='':
              return(d)
         if int(d)==1 or int(d)==2 or int(d)==3:
            return(int(d))
         elif d=="3+":
            return(3)
         else:
            print("Invalid input: try entering without the 'hr'")
            return(du())
      duration=du()
   if time==None:
      def ti():
         t=input("Enter your time constraint or press enter to skip: (12:00) (5:00) (9:00+) ")
         if t=='':
              return('')
         if int(t)==12 or int(t)==5 or int(t)==9:
            return(int(t))
         elif t=="9+":
            return(9)
         else:
            print("Invalid input: try entering without the ':00'")
            return(ti())
      time=ti()
   if location==None:
      def lo():
         l=input("Enter your distance constraint or press enter to skip: (home) (in town) (far away) ")
         if l=='':
              return('')
         if l=="home":
            return(1)
         elif l=="in town":
            return(2)
         elif l=="far away":
            return(3)
         else:
            print("Invalid input")
            return(lo())
      location=lo()
   return([[1,price],[2,members],[3,duration],[4,time],[5,location]])
inputs=gather()

for i in inputs:
      if i[0]==1 and i[1]!='':
            if i[1]>=20 and i[1]<50:
                  for y in {"videogame","concert","escape room"}:
                        if y in options:
                              options.remove(y)
            elif i[1]>=10 and i[1]<20:
                  for y in {"movie at home","lunch out","concert","shopping","dinner out","videogame","escape room"}:
                        if y in options:
                              options.remove(y)
      elif i[0]==2 and i[1]!='':
            if i[1]>=6:
                  for y in {"lunch out","concert","dinner out"}:
                        if y in options:
                              options.remove(y)
            elif i[1]>=4 and i[1]<6:
                  for y in {"concert"}:
                        if y in options:
                              options.remove(y)
            elif i[1]>=2 and i[1]<4:
                   for y in {"cards","videogame","escape room"}:
                         if y in options:
                               options.remove(y)
      elif i[0]==3 and i[1]!='':
            if i[1]>=3:
                  for y in {"lunch out","shopping","dinner out"}:
                        if y in options:
                              options.remove(y)
            elif i[1]>=2 and i[1]<3:
                  for y in {"movie theater","cards","movie at home","shopping","videogame","escape room"}:
                        if y in options:
                              options.remove(y)
            elif i[1]>=1 and i[1]<2:
                  for y in {"movie theater","cards","movie at home","concert","videogame","escape room"}:
                        if y in options:
                              options.remove(y)
      elif i[0]==4 and i[1]!='':
            if i[1]==12:
                  for y in {"movie theater","concert","dinner out","escape room"}:
                        if y in options:
                              options.remove(y)
            elif i[1]==5:
                  for y in {"movie theater","cards","movie at home","lunch out","concert","shopping","dinner out","videogame","escape room"}:
                        if y in options:
                              options.remove(y)
            elif i[1]==9:
                  for y in {"lunch out","shopping","dinner out","escape room"}:
                        if y in options:
                              options.remove(y)
      elif i[0]==5 and i[1]!='':
            if i[1]==1:
                  for y in {"movie theater","lunch out","concert","shopping","dinner out","escape room"}:
                        if y in options:
                              options.remove(y)
            elif i[1]==2:
                  for y in {"cards","movie at home","concert","videogame","escape room"}:
                        if y in options:
                              options.remove(y)
            elif i[1]==3:
                  for y in {"cards","movie at home","videogame"}:
                        if y in options:
                              options.remove(y)

q=''
if len(options)>=1:
      q="Your options are: "
      for a in options:
            if int((len(options)-1))!=int(options.index(a)):
                q+=a+", "
            else:
                 q+="and "+a
else:
      q="No options available based on your constraints"
      
print("""


      """+q)
      

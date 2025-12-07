##__________________________________________________________________
##|  price     |  members   | duration   |   time     | location   |
##|____________|____________|____________|____________|____________|
##|  $10       |  2         | 1hr        |  12:00     |  home      |
##|____________|____________|____________|____________|____________|
##|  $20       |  4         | 2hr        |  5:00      |  in town   |
##|____________|____________|____________|____________|____________|
##|  $50+      |  6+        | 3hr+       |  7:00+     |  far away  |
##|____________|____________|____________|____________|____________|

print(""" 
      This program is intended to assist you in choosing an activity based on the inputs you give it.
      It holds a list of options and rules out all options that dont fit the constraints.
      
      """)

options = {"movie theater","cards","movie at home","lunch out","concert","shopping","dinner out","videogame","escape room"}

inputs = def gather():
   price, members, duration, time, location
   if price~=None:
      def pr():
         p=input("Enter your available budjet or press enter to skip: ")
         if int(p)>=0 or p=="":
            price=int(p)
         elif p=="50+":
            price=50
         else:
            print("Invalid input: try entering without the '$'")
            pr()
   if members~=None
      def me():
         m=input("Enter your group size or press enter to skip: (2) (4) (6+)")
         if int(m)==2 or int(m)==4 or int(m)==6 or m=="":
            members=int(m)
         elif m=="6+":
            members=6
         else:
            print("Invalid input")
            me()
   if duration~=None
      def du():
         d=input("Enter your time constraint or press enter to skip: (1hr) (2hr) (3hr+)")
         if int(d)==1 or int(d)==2 or int(d)==3 or d=="":
            duration=int(d)
         elif d=="3+":
            duration=3
         else:
            print("Invalid input: try entering without the 'hr'")
            du()
   if time~=None
      def ti():
         t=input("Enter your time constraint or press enter to skip: (12:00) (5:00) (7:00+)")
         if int(t)==12 or int(t)==5 or int(t)==7 or t=="":
            time=int(t)
         elif t=="7+":
            time=7
         else:
            print("Invalid input: try entering without the ':00'")
            ti()
   if location~=None
      def lo():
         l=input("Enter your distance constraint or press enter to skip: (home) (in town) (far away)")
         if l=="home" or l=="":
            location=1
         elif l=="in town":
            location=2
         elif l=="far away"
            location=3
         else:
            print("Invalid input")
            lo()
   return {price, members, duration, time, location}

x=0
for i in inputs:
      x+=1
      if x==1:
            if i>=20 and i<50:
                  for y in {"videogame","concert","escape room"}:
                        if y in options:
                              options.remove(y)
            elif i>=10 and i<20:
                  for y in {"lunch out","dinner out","move at home","shopping"}
                        if y in options:
                              optioms.remove(y)
      elif x==2:
            if i>=4 and i<6:
                  for y in {"escape room"}:
                        if y in options:
                              options.remove(y)
            elif i>=2 and i<4:
                   for y in {""}
      elif x==3:

      elif x==4:

      elif x==5:

print(F"my name is {'priti'}")
d={'a':1, 'b':2, 'c':3}
print(F"Hello word")
library = [('author','topic','pages'),('priti','python','200'),('priti','java','300')]
for book in library:
    print(F"{book[0]}", book[1], book[2])


for author,topic,pages in library:
    print(f"{author:<{10}}{topic:<{30}} {pages:<{10}}")
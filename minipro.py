fo=open("movies.txt","r")
raw_data_movie=fo.read()
fr=open("rating.txt")
raw_data_ratings=fr.read()
list_attr_ratings=['movie_id','rating']
list_attr_movie=['movie_id','movie_name','genre','year']
list_data_v2=[]
list_data_movie_v3=[]
list_data_ratings_v3=[]
genre=set()
year=set()
#movie_data
list_data_v1=raw_data_movie.split("\n")
for i in range(len(list_data_v1)):
    list_data_v2.append(list_data_v1[i].split(","))
for j in range(len(list_data_v2)):
    list_data_movie_v3.append(dict(zip(list_attr_movie,list_data_v2[j])))
for i in range(len(list_data_v2)):
    list_data_movie_v3[i]["genre"]=list_data_v2[i][2].split("|")
#rating_data
list_data_v2.clear()
list_data_v1=raw_data_ratings.split("\n")
for i in range(len(list_data_v1)):
    list_data_v2.append(list_data_v1[i].split(","))
for j in range(len(list_data_v2)):
    list_data_ratings_v3.append({list_attr_ratings[i]:float(list_data_v2[j][i]) for i in range(len(list_attr_ratings))})
fo.close()
fr.close()
c=0
#create set for genre
for i in range(len(list_data_movie_v3)):
        genre.update(x for x in list_data_movie_v3[i]["genre"])
#create set for year
for i in range(len(list_data_movie_v3)):
        year.update(x for x in [list_data_movie_v3[i]["year"]])
def movie_count_for_spec_genre(a):
    global c
    if a=='All':
        a=genre
        print(a)
    else:
        a=a.split()
    for each in a:
        for i in range(len(list_data_movie_v3)):
            if each.capitalize() in list_data_movie_v3[i]["genre"]:
                print("'",list_data_movie_v3[i]["movie_name"],"'",end='\t')
                c+=1
        print("\n",each.capitalize()," :",c)
        c=0

def movie_count_by_genre_n_ratings(a,b):
    global c
    if a=='All':
        a=genre
    else:
        a=a.split()
    for each in a:
            for i in range(len(list_data_movie_v3)):
                if each.capitalize() in list_data_movie_v3[i]["genre"]:
                    if list_data_ratings_v3[i]["rating"]>b:
                        c+=1
            if c!=0:
                print(each.capitalize()," :",c)
                c=0

def movie_count_by_year_rating_cmbgenre(y,r,g):
    global c
    g=g.split()
    for i in range(len(list_data_movie_v3)):
        if int(list_data_movie_v3[i]["year"])>y:
            temp_set=set(i for i in list_data_movie_v3[i]["genre"] if i in g)
            if temp_set==set(g) and list_data_ratings_v3[i]["rating"]>r:
                print(list_data_movie_v3[i]['movie_name'])
                c=c+1
    print(c," movies were released after",y,"having rating greater than",r,"and genre:",g)
    c=0
def top_movie_by_genre(a):
    global c
    lar=0
    if a=='All':
        a=genre
    else:
        a=a.split()
    for each in a:
            for i in range(len(list_data_movie_v3)):
                if each.capitalize() in list_data_movie_v3[i]["genre"]:
                    if list_data_ratings_v3[i]["rating"]>lar:
                        lar=list_data_ratings_v3[i]["rating"]
                        c=list_data_movie_v3[i]["movie_name"]
            if lar!=0:
                print("Top movie in",each,"was","'",c,"'")
                lar=0
                c=0
def top_movie_by_year(a):
    global c
    lar=0
    if a=='All':
        a=year
    else:
        a=str(a)
        a=a.split()
    for each in a:
            for i in range(len(list_data_movie_v3)):
                if each in str(list_data_movie_v3[i]["year"]):
                    if list_data_ratings_v3[i]["rating"]>lar:
                        lar=list_data_ratings_v3[i]["rating"]
                        c=list_data_movie_v3[i]["movie_name"]
            if lar!=0:
                print("Top movie in",each,"was","'",c,"'")
                lar=0
                c=0
#exection starts from here
while True:
    print("1-> movies_count by genre ans\n2-> movie count by genre and ratings\n3=>movie_count_by_combination_of_(year,rating,genre)")
    print("4->top_movie_in_genre\n5->top_movie_in year")
    n=int(input("select any one operation"))
    if n==1:
       n1=input("enter any genre or 'all' for each genre")
       movie_count_for_spec_genre(n1.capitalize())
    
    elif n==2:
        a=input("enter any genre or enter 'all' for each genre")
        b=float(input("enter rating"))
        movie_count_by_genre_n_ratings(a.capitalize(),b)
    elif n==3:
        y=int(input("enter year"))
        r=float(input("enter rating"))
        g=input("enter genre(s)")
        movie_count_by_year_rating_cmbgenre(y,r,g.capitalize())
    elif n==4:
       n1=input("enter any genre or 'all' for each genre")
       top_movie_by_genre(n1.capitalize())
    elif n==5:
       n1=input("enter year or 'all' for each year")
       top_movie_by_year(n1.capitalize())
#continue yes or no   
    ync=input("Do you want to continue (type 'y' or 'n')")
    while ync not in ('y','n','Y','N'):
        ync=input("Do you want to continue (type 'y' or 'n')")
    if ync in('n','N'):
            break

from urllib import request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from urllib.request import urlopen
import json

# from recommend.views import account_list

#from .models_post import Ratings

#url = "http://ec2-3-36-57-87.ap-northeast-2.compute.amazonaws.com:8000/posts/"
#responseBody = urlopen(url).read().decode('utf-8')
#jsonArray = json.loads(responseBody)

cred = credentials.Certificate("healingfeeling-9c1bf-firebase-adminsdk-kktgb-7226f7ac89.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://healingfeeling-9c1bf-default-rtdb.firebaseio.com/'
})

# 행복 ratings 
happydirsong = db.reference('score').child('노래')
happydirbook = db.reference('score').child('도서')
happydirwhere = db.reference('score').child('장소')

# 분노 ratings 
angrydirsong = db.reference('angryscore').child('노래')
angrydirbook = db.reference('angryscore').child('도서')
angrydirwhere = db.reference('angryscore').child('장소')

# 슬픔 ratings 
saddirsong = db.reference('sadscore').child('노래')
saddirbook = db.reference('sadscore').child('도서')
saddirwhere = db.reference('sadscore').child('장소')

print(happydirsong.get())
print(angrydirsong.get())
print(saddirsong.get())
#print('views.RatingsSerializer'.objects.order_by('happysongtitle').first())

#print(account_list('GET'))

#!/usr/bin/env python
#coding: utf-8

# In[35]:

#rating; 평가
import math
import pandas as pd


# 행복 ratings
happy_dataset_df=pd.DataFrame(happydirsong.get())
happy_dataset_df.fillna("Not Seen Yet",inplace=True)
happy_dataset_df

happy_dataset_df2=pd.DataFrame(happydirbook.get())
happy_dataset_df2.fillna("Not Seen Yet",inplace=True)
happy_dataset_df2

happy_dataset_df3=pd.DataFrame(happydirwhere.get())
happy_dataset_df3.fillna("Not Seen Yet",inplace=True)
happy_dataset_df3

# 분노 ratings
angry_dataset_df=pd.DataFrame(angrydirsong.get())
angry_dataset_df.fillna("Not Seen Yet",inplace=True)
angry_dataset_df

angry_dataset_df2=pd.DataFrame(angrydirbook.get())
angry_dataset_df2.fillna("Not Seen Yet",inplace=True)
angry_dataset_df2

angry_dataset_df3=pd.DataFrame(angrydirwhere.get())
angry_dataset_df3.fillna("Not Seen Yet",inplace=True)
angry_dataset_df3

# 슬픔 ratings
sad_dataset_df=pd.DataFrame(saddirsong.get())
sad_dataset_df.fillna("Not Seen Yet",inplace=True)
sad_dataset_df

sad_dataset_df2=pd.DataFrame(saddirbook.get())
sad_dataset_df2.fillna("Not Seen Yet",inplace=True)
sad_dataset_df2

sad_dataset_df3=pd.DataFrame(saddirwhere.get())
sad_dataset_df3.fillna("Not Seen Yet",inplace=True)
sad_dataset_df3


# In[36]:

# 행복 ratings
happydatasetsong=happydirsong.get()
happydatasetbook=happydirbook.get()
happydatasetwhere=happydirwhere.get()

# 분노 ratings
angrydatasetsong=angrydirsong.get()
angrydatasetbook=angrydirbook.get()
angrydatasetwhere=angrydirwhere.get()

# 슬픔 ratings
saddatasetsong=saddirsong.get()
saddatasetbook=saddirbook.get()
saddatasetwhere=saddirwhere.get()


print(happydirbook.get())
print("kkkkkkkkkkkk")
print(angrydatasetsong)


def unique_items_song(dataset):
    unique_items_list = []
    for person in dataset.keys():
        for items in dataset[person]:
            unique_items_list.append(items)
    s=set(unique_items_list)
    unique_items_list=list(s)
    return unique_items_list

def unique_items_book(dataset):
    unique_items_list = []
    for person in dataset.keys():
        for items in dataset[person]:
            unique_items_list.append(items)
    s=set(unique_items_list)
    unique_items_list=list(s)
    return unique_items_list

def unique_items_where(dataset):
    unique_items_list = []
    for person in dataset.keys():
        for items in dataset[person]:
            unique_items_list.append(items)
    s=set(unique_items_list)
    unique_items_list=list(s)
    return unique_items_list
# In[37]:


print(unique_items_song(happydatasetsong))
print(unique_items_book(happydatasetbook))
print(unique_items_where(happydatasetwhere))

print("살려줘")
print(unique_items_song(angrydatasetsong))


# In[61]:



# custom function to create pearson correlation method from scratch
import math

def person_corelation(dataset,person1,person2):
    both_rated = {}
    for item in dataset[person1]:
        if item in dataset[person2]:
            both_rated[item] = 1

    number_of_ratings = len(both_rated)
    if number_of_ratings == 0:
        return 0

    person1_preferences_sum = sum([dataset[person1][item] for item in both_rated])
    person2_preferences_sum = sum([dataset[person2][item] for item in both_rated])

    # Sum up the squares of preferences of each user
    person1_square_preferences_sum = sum([pow(dataset[person1][item], 2) for item in both_rated])
    person2_square_preferences_sum = sum([pow(dataset[person2][item], 2) for item in both_rated])

    # Sum up the product value of both preferences for each item
    product_sum_of_both_users = sum([dataset[person1][item] * dataset[person2][item] for item in both_rated])

    # Calculate the pearson score
    numerator_value = product_sum_of_both_users - (
    person1_preferences_sum * person2_preferences_sum / number_of_ratings)
    denominator_value = math.sqrt((person1_square_preferences_sum - pow(person1_preferences_sum, 2) / number_of_ratings) * (
    person2_square_preferences_sum - pow(person2_preferences_sum, 2) / number_of_ratings))
    if denominator_value == 0:
        return 0
    else:
        r = numerator_value / denominator_value
        return r
    
def most_similar_users(dataset,target_person,no_of_users):
    
    # Used list comprehension for finding pearson similarity between users
    scores = [(person_corelation(dataset,target_person,other_person),other_person) for other_person in dataset if other_person !=target_person]
    
    #sort the scores in descending order
    scores.sort(reverse=True)
    
    #return the scores between the target person & other persons
    return scores[0:no_of_users]


tp = 'CvOap2Q2t7MTe47zBxAvBpgFBTW2'
most_similar_users(happydatasetsong,tp,len(happydatasetsong))
most_similar_users(happydatasetbook,tp,len(happydatasetbook))
most_similar_users(happydatasetwhere,tp,len(happydatasetwhere))


# In[62]:


def recommendation_phase(dataset,person):
    # Gets recommendations for a person by using a weighted average of every other user's rankings
    totals = {}  #empty dictionary
    simSums = {} # empty dictionary
    for other in dataset:
        # don't compare me to myself
        if other == person:
            continue
        sim = person_corelation(dataset,person, other)
        # ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in dataset[other]:
            # only score movies i haven't seen yet
            if item not in dataset[person]:
                # Similrity * score
                totals.setdefault(item, 0)
                totals[item] += dataset[other][item] * sim
                # sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
                # Create the normalized list

    rankings = [(total / simSums[item], item) for item, total in totals.items()]
    rankings.sort(reverse=True)
    # returns the recommended items
    recommendataions_list = [(recommend_item,score) for score, recommend_item in rankings]
    return recommendataions_list


# In[63]:


print("Enter the target person")
b=False
b2=False
b3=False

c=False
c2=False
c3=False

d=False
d2=False
d3=False


# 행복 ratings
if tp in happydatasetsong.keys():
    a=recommendation_phase(happydatasetsong,tp)
    print(a)
    if a != -1:
        print(a)
        print("Recommendation Using User based Collaborative Filtering:  ")
        
        for webseries,weights in a:
            print(webseries,'——>',weights)
            if(b==False):
                happytitlesong=webseries
                happydatasong=weights
            b=True
        
else:
    happytitlesong="no"
    happydatasong="no"

if tp in happydatasetbook.keys():
        a=recommendation_phase(happydatasetbook,tp)
        if a != -1:
            print("Recommendation Using User based Collaborative Filtering:  ")
            
            for webseries,weights in a:
                print(webseries,'——>',weights)
                if(b2==False):
                    happytitlebook=webseries
                    happydatabook=weights
                b2=True
            
else:
    happytitlebook="no"
    happydatabook="no"

if tp in happydatasetwhere.keys():
        a=recommendation_phase(happydatasetwhere,tp)
        if a != -1:
            print("Recommendation Using User based Collaborative Filtering:  ")
            for webseries,weights in a:
                print(webseries,'——>',weights)
                if(b3==False):
                    happytitlewhere=webseries
                    happydatawhere=weights
                b3=True
            
else:
    happytitlewhere="no"
    happydatawhere="no"


# 분노 ratings

if tp in angrydatasetsong.keys():
    a=recommendation_phase(angrydatasetsong,tp)
    print(a)
    if a != -1:
        print(a)
        print("분노!!  ")
        
        for webseries,weights in a:
            print(webseries,'——>',weights)
            if(c==False):
                angrytitlesong=webseries
                angrydatasong=weights
            c=True
        
else:
    angrytitlesong="no"
    angrydatasong="no"

if tp in angrydatasetbook.keys():
        a=recommendation_phase(angrydatasetbook,tp)
        if a != -1:
            print("Recommendation Using User based Collaborative Filtering:  ")
            
            for webseries,weights in a:
                print(webseries,'——>',weights)
                if(c2==False):
                    angrytitlebook=webseries
                    angrydatabook=weights
                c2=True
            
else:
    angrytitlebook="no"
    angrydatabook="no"

if tp in angrydatasetwhere.keys():
        a=recommendation_phase(angrydatasetwhere,tp)
        if a != -1:
            print("Recommendation Using User based Collaborative Filtering:  ")
            for webseries,weights in a:
                print(webseries,'——>',weights)
                if(c3==False):
                    angrytitlewhere=webseries
                    angrydatawhere=weights
                c3=True
            
else:
    angrytitlewhere="no"
    angrydatawhere="no"


# 슬픔

if tp in saddatasetsong.keys():
    a=recommendation_phase(saddatasetsong,tp)
    print(a)
    if a != -1:
        print(a)
        print("Recommendation Using User based Collaborative Filtering:  ")
        
        for webseries,weights in a:
            print(webseries,'——>',weights)
            if(d==False):
                sadtitlesong=webseries
                saddatasong=weights
            d=True
        
else:
    sadtitlesong="no"
    saddatasong="no"

if tp in saddatasetbook.keys():
        a=recommendation_phase(saddatasetbook,tp)
        if a != -1:
            print("Recommendation Using User based Collaborative Filtering:  ")
            
            for webseries,weights in a:
                print(webseries,'——>',weights)
                if(d2==False):
                    sadtitlebook=webseries
                    saddatabook=weights
                d2=True
            
else:
    sadtitlebook="no"
    saddatabook="no"

if tp in saddatasetwhere.keys():
        a=recommendation_phase(saddatasetwhere,tp)
        if a != -1:
            print("Recommendation Using User based Collaborative Filtering:  ")
            for webseries,weights in a:
                print(webseries,'——>',weights)
                if(d3==False):
                    sadtitlewhere=webseries
                    saddatawhere=weights
                d3=True
            
else:
    sadtitlewhere="no"
    saddatawhere="no"



# In[ ]:
print(happytitlesong)
print(happydatasong)
print(happytitlebook)
print(happydatabook)
print(happytitlewhere)
print(happydatawhere)
print("\n")
print(sadtitlesong)
print(saddatasong)
print(sadtitlebook)
print(saddatabook)
print(sadtitlewhere)
print(saddatawhere)
print("\n")
print(angrytitlesong)
print(angrydatasong)
print(angrytitlebook)
print(angrydatabook)
print(angrytitlewhere)
print(angrydatawhere)
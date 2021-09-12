from django.db import models
from .userRecommend import happydatabook, happydatasong, happydatawhere, happytitlebook, happytitlesong, happytitlewhere
from .userRecommend import saddatabook, saddatasong, saddatawhere, sadtitlebook, sadtitlesong, sadtitlewhere
from .userRecommend import angrydatabook, angrydatasong, angrydatawhere, angrytitlebook, angrytitlesong, angrytitlewhere
#from .userRecommend import data , title, titlebook, titlewhere,databook,datawhere

# class Post(models.Model):
#     ratings = data
#     title = title
#     bookratings=databook
#     booktitle=titlebook
#     whereratings=datawhere
#     wheretitle=titlewhere


class Rating(models.Model):
    happysongratings = happydatasong
    happysongtitle = happytitlesong
    happybookratings = happydatabook
    happybooktitle = happytitlebook
    happywhereratings = happydatawhere
    happywheretitle = happytitlewhere
    sadsongratings = saddatasong
    sadsongtitle = sadtitlesong
    sadbookratings = saddatabook
    sadbooktitle = sadtitlebook
    sadwhereratings = saddatawhere
    sadwheretitle = sadtitlewhere
    angrysongratings = angrydatasong
    angrysongtitle = angrytitlesong
    angrybookratings = angrydatabook
    angrybooktitle = angrytitlebook
    angrywhereratings = angrydatawhere
    angrywheretitle = angrytitlewhere

# class Recommend(models.Model):
#     userId =models.CharField(max_length=200) 
#     emotion = models.CharField(max_length=200)
#     category = models.CharField(max_length=200)
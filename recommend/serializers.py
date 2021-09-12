from rest_framework import  serializers
# from .models import Post, Recommend
from .models import Rating

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('ratings','title','bookratings','booktitle','whereratings','wheretitle')


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('happysongratings','happysongtitle','happybookratings','happybooktitle','happywhereratings','happywheretitle',
        'sadsongratings','sadsongtitle','sadbookratings','sadbooktitle','sadwhereratings','sadwheretitle',
        'angrysongratings','angrysongtitle','angrybookratings','angrybooktitle','angrywhereratings','angrywheretitle'
        
        )


# class RecommendSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recommend
#         fields = ('userId','emotion','category')
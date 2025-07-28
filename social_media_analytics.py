from collections import Counter, defaultdict
posts = [
    {'id':1,'user':'alice','content':"Love Python programming!",'likes':15,'tags':["python", "coding"] },
    {'id':2,'user':'bob','content':"Great weather today",'likes':8,'tags':["weather","life"] },
    {'id':3,'user':'alice','content':"Data structures are fun",'likes':22,'tags':["python","learning"] }
]
users = {
    "alice": {"followers": 150, "following": 75},
    "bob": {"followers": 89, "following": 120},
}



MOST_POPULAR_TAGS = Counter(posts[0]['tags'])
TOTAL_LIKES = defaultdict(int)


for i  in range(0,len(posts)):
    post = posts[i]
    post_counter = Counter(post['tags'])
    user_name = post['user']
    if i != 0:
        MOST_POPULAR_TAGS = MOST_POPULAR_TAGS + post_counter
    TOTAL_LIKES[user_name] += post['likes']

    if not users[user_name].get('likes'):
        users[user_name]['likes'] = post['likes']
    else:
        users[user_name]['likes'] += post['likes']

    if not users[user_name].get('post_count'):
        users[user_name]['post_count'] = 1
    else:
        users[user_name]['post_count'] += 1






# 1. Most Popular Tags – Use collections.Counter to find the most frequent tags across posts.
# print(MOST_POPULAR_TAGS)

# 2. User Engagement Analysis – Use defaultdict to compute total likes per user.
# print(TOTAL_LIKES)

# 3. Top Posts by Likes – Use sorted() to list posts in descending order of likes.
# print(sorted(posts, key= lambda post: -post['likes']))


# 4. User Activity Summary – Combine post and user data to generate a summary per user (posts count, likes, followers, etc.).
# print(users)

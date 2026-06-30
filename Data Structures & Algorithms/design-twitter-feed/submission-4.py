import heapq
class User:
    def __init__(self):
        self.newsFeed = [] # max heap sorted by globalTweetId
        self.following = set()
        self.followers = set()
        self.posts = set()
    
    def addTweetToNewsFeed(self, tweetId, globalTweetId):
        heapq.heappush(self.newsFeed, (globalTweetId, tweetId))
    
    def removeTweetsFromPosts(self, postsToRemove):
        postsToStayInNewsFeed = []
        while self.newsFeed:
            post = self.newsFeed[0][1], self.newsFeed[0][0]
            if post not in postsToRemove:
                postsToStayInNewsFeed.append(post)
            heapq.heappop(self.newsFeed)
        
        for tweetId, globalTweetId in postsToStayInNewsFeed:
            self.addTweetToNewsFeed(tweetId, globalTweetId)
    
    def notifyFollowersOfPost(self, tweetId, globalTweetId):
        for user in self.followers:
            user.addTweetToNewsFeed(tweetId, globalTweetId)


class Twitter:
    def __init__(self):
        self.globalTweetId = 0
        self.users = {} #map userId to User
    
    def getUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User()
        return self.users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        # create a user if don't exist
        user = self.getUser(userId)

        user.posts.add((tweetId, self.globalTweetId))

        # add tweet to user news feed
        user.addTweetToNewsFeed(tweetId, self.globalTweetId)

        # add tweet to all followers news feed
        user.notifyFollowersOfPost(tweetId, self.globalTweetId)

        self.globalTweetId += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.getUser(userId)
        return [x[1] for x in heapq.nlargest(10, user.newsFeed)]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        follower = self.getUser(followerId)
        followee = self.getUser(followeeId)

        for post in followee.posts:
            if followee not in follower.following:
                follower.addTweetToNewsFeed(post[0], post[1])
        
        follower.following.add(followee)
        followee.followers.add(follower)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        follower = self.getUser(followerId)
        followee = self.getUser(followeeId)

        if followee in follower.following and follower in followee.followers:
            follower.following.remove(followee)
            followee.followers.remove(follower)
            follower.removeTweetsFromPosts(followee.posts)
        

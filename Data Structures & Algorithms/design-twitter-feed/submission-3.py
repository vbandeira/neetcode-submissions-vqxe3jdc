class Twitter:
    # Minha solução: O(F * T) 
    #   onde F é o número de seguidores e 
    #   T é o máximo número de tweets por usuário

    def __init__(self):
        # Control followers - Hashmap with userId and followeeId
        self.followMap = defaultdict(set)
        # Control tweets for each use - Hashmap with userId 
        #   and list of tweets
        self.tweetMap = defaultdict(list)
        # Time tracker
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add tweet and increments time (signal inverted for max heap)
        self.tweetMap[userId].append((self.counter, tweetId))
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Returns the 10 most recents tweets of a user and
        # who it is following ordered by time desc
        
        # Get followees and adds itself to temp set
        followees = self.followMap[userId]
        followees.add(userId)
        tweets = []

        # Iterates over followees to get all tweets
        for f in followees:
            if not self.tweetMap[f]:
                continue
            for t in self.tweetMap[f]:
                tweets.append(t)

        # Creates a heap on tweets and initialize response array
        heapq.heapify(tweets)
        top = []
        
        # Gets top 10 tweets checking if they exists
        for i in range(min(len(tweets), 10)):
            top.append(heapq.heappop(tweets)[1])
        return top

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add follower
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove follower

        # Use discard method to ignore if the value doesn't exists
        self.followMap[followerId].discard(followeeId)
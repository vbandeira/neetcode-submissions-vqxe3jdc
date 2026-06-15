class Twitter:
    # Explicação: O(...)

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
        minHeap = []

        # Iterates over followees to get the latest tweets
        for f in followees:
            if f in self.tweetMap:
                index = len(self.tweetMap[f]) - 1
                c, t = self.tweetMap[f][index]
                minHeap.append([c, t, f, index - 1])

        # Creates a heap on tweets and initialize response array
        heapq.heapify(minHeap)
        top = []
        
        # Gets top 10 tweets checking if they exists
        while minHeap and len(top) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            top.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return top

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add follower
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove follower

        # Use discard method to ignore if the value doesn't exists
        self.followMap[followerId].discard(followeeId)
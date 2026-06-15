class Twitter:

    def __init__(self):
        # Control followers - Hashmap with userId and followeeId?
        self.followMap = defaultdict(set)
        # Controle tweets for each use - Hashmap with userId and heap?
        self.tweetMap = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.counter, tweetId))
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Returns the 10 most recents tweets of a user and
        # who it is following ordered by time desc
        followees = self.followMap[userId]
        followees.add(userId)
        tweets = []
        for f in followees:
            if not self.tweetMap[f]:
                continue
            for t in self.tweetMap[f]:
                tweets.append(t)

        heapq.heapify(tweets)
        top = []
        print(tweets)
        for i in range(min(len(tweets), 10)):
            top.append(heapq.heappop(tweets)[1])
        return top

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add follower
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove follower

        self.followMap[followerId].discard(followeeId)
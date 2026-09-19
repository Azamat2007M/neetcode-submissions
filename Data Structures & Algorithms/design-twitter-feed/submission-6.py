from collections import defaultdict

class Twitter:
    #MaxHeap method Time: O(KlogK) for get others O(1)
    def __init__(self):
        self.count = 0
        self.table_feeds = defaultdict(list)
        self.table_followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.table_feeds[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        self.table_followers[userId].add(userId)

        for followeeId in self.table_followers[userId]:
            if followeeId in self.table_feeds:
                index = len(self.table_feeds[followeeId]) - 1
                ctn, tweetId = self.table_feeds[followeeId][index]

                heapq.heappush(max_heap, (-ctn, tweetId, followeeId, index - 1))

        while max_heap and len(res) < 10:
            ctn, tweetId, followeeId, next_index = heapq.heappop(max_heap)
            res.append(tweetId)

            if next_index >= 0:
                next_ctn, next_tweetId = self.table_feeds[followeeId][next_index]
                heapq.heappush(max_heap, (-next_ctn, next_tweetId, followeeId, next_index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.table_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.table_followers[followerId] and followeeId != followerId:
            self.table_followers[followerId].remove(followeeId)

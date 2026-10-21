from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # negative time for max heap
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        possible_tweets = []
        feed = []

        users = set(self.following[userId])
        users.add(userId)

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
                possible_tweets.append((-time, tweetId, user, index))
        
        heapq.heapify(possible_tweets)

        while possible_tweets and len(feed) < 10:
            _, tweetId, user, index = heapq.heappop(possible_tweets)
            feed.append(tweetId)

            if index > 0:
                next_index = index - 1
                time, tweetId = self.tweets[user][next_index]
                heapq.heappush(possible_tweets, (-time, tweetId, user, next_index))
        
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

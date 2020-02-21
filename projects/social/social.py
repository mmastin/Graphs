import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'Users {i + 1}')

        # Create friendships
        # create a list with all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)
        print('--------')
        print(possible_friendships)
        print('--------')

        # shuffle the list
        # grab the first N friendship pairs from the list
        # and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # avg_friendships = total_friendships / num_users
        # total friendships = avg_friendships * num_users
        # N = avg_friendships * num_users // 2

    def populate_graph_linear(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(num_users):
            self.add_user(f'User {i + 1}')

        friendships_to_create = avg_friendships * num_users
        friendships = 0
        collisions = 0
        while friendships < friendships_to_create:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                friendships += 2
            else:
                collisions += 1
        print(f'COLLISIONS: {collisions}')

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # create an empty queue
        q = Queue()
        # add a path to queue
        q.enqueue( [user_id] )
        # create an empty set to store visited nodes
        visited = {}
        # while queu is not empty
        while q.size() > 0:
            # dequeue the first vertex
            path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            v = path[-1]
            # check if it's been visited
            # if has not been visited
            if v not in visited:
                # mark it as visited
                # add it to the visited dictionary, with the path as the key
                visited[v] = path
                # then add all FRIENDS to back of queue
                # for friend_id in self.get_friends(v):
                for friend in self.friendships[v]:
                    # COPY THE PATH
                    path_copy = path.copy()
                    # ADD FRIEND TO THE PATH
                    path_copy.append(friend)
                    q.enqueue(path_copy)

        return visited

import time

if __name__ == '__main__':
    sg = SocialGraph()

    start_time = time.time()
    sg.populate_graph(100, 90)
    end_time = time.time()
    print(f'quadratic runtime: {end_time - start_time} seconds')

    start_time = time.time()
    sg.populate_graph_linear(100, 90)
    end_time = time.time()
    print(f'linear runtime: {end_time - start_time} seconds')

    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)

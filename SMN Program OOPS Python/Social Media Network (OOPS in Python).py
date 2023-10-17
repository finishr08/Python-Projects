#Group Leader
#Mustafa Ahmed
#Team Members
#Sanaullah
#Usman
#Amir

class User:
    def __init__(self, username, profile_picture=None, first_name=None, last_name=None, email=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.profile_picture = profile_picture
        self.friends = []
        self.friends_requested = []
        self.friends_pending = []
        self.posts = []

    def create_post(self, content):
        post = Post(self, content)
        self.posts.append(post)

    def add_friend(self, friend):
        self.friends.append(friend)
        self.friends_requested.remove(friend)

    def add_pending_friend(self, friend):
        self.friends_pending.append(friend)

    def add_comment(self, post, comment_text):
        comment = Comment(self, comment_text)
        post.comments.append(comment)


class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.comments = []


class Comment:
    def __init__(self, user, text):
        self.user = user
        self.text = text


def create_profile():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = input("Enter your username: ")
    email = input("Enter your email address: ")
    profile_picture = input("Enter a link to your profile picture (optional): ")

    # Create a user instance with first name, last name, and email
    user = User(username, profile_picture, first_name, last_name, email)
    all_users.append(user)
    print(f"Welcome, {user.first_name} {user.last_name}!")


def create_post(user):
    content = input("What's on your mind? ")
    user.create_post(content)
    print(f"{user.username}, your post has been created!")


def comment_on_post(user):
    post_owner_username = input("Enter the username of the post owner: ")
    post_content = input("Enter the content of the post you want to comment on: ")
    target_user = None
    for friend in all_users:
        if friend.username == post_owner_username:
            target_user = friend
            break
    if target_user:
        for post in target_user.posts:
            if post.content == post_content:
                comment_text = input("Enter your comment: ")
                post.add_comment(user, comment_text)
                print("Your comment has been added!")
                return
    print("Post not found or user not in your friend list.")


def send_friend_request(user):
    friend_username = input("Enter the username of the user you want to send a friend request to: ")
    for friend in user.friends:
        if friend.username == friend_username:
            print("You are already friends with this user.")
            return
    for friend in user.friends_requested:
        if friend.username == friend_username:
            print("Friend request already sent to this user.")
            return
    for friend in user.friends_pending:
        if friend.username == friend_username:
            print("Friend request from this user is pending. You can accept it.")
            return
    for friend in all_users:
        if friend.username == friend_username:
            user.add_pending_friend(friend)
            print("Friend request sent!")
            return
    print("User not found.")


def accept_friend_request(user):
    friend_username = input("Enter the username of the user you want to accept a friend request from: ")
    for friend in user.friends:
        if friend.username == friend_username:
            print("You are already friends with this user.")
            return
    for friend in user.friends_requested:
        if friend.username == friend_username:
            user.add_friend(friend)
            print("Friend request accepted!")
            return
    print("No friend request found from this user.")


def view_news_feed(user):
    print(f"News Feed for {user.username}:")
    for friend in user.friends:
        for post in friend.posts:
            print(f"{friend.username}'s post: {post.content}")
            for comment in post.comments:
                print(f"    {comment.user.username} commented: {comment.text}")


if __name__ == "__main__":
    all_users = []
    while True:
        print("\nSocial Media Network Menu:")
        print("1. Create and customize your profile")
        print("2. Post on your profile")
        print("3. Comment on a post")
        print("4. Send a friend request")
        print("5. Accept a friend request")
        print("6. View news feed")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_profile()
        elif choice == "2":
            create_post(all_users[0])  # Assuming the first user in the list is the logged-in user.
        elif choice == "3":
            comment_on_post(all_users[0])  # Assuming the first user in the list is the logged-in user.
        elif choice == "4":
            send_friend_request(all_users[0])  # Assuming the first user in the list is the logged-in user.
        elif choice == "5":
            accept_friend_request(all_users[0])  # Assuming the first user in the list is the logged-in user.
        elif choice == "6":
            view_news_feed(all_users[0])  # Assuming the first user in the list is the logged-in user.
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

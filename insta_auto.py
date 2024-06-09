from instabot import Bot

b = Bot()
# here in the login function we need to give username and password 
# of the instagram account which we would be using
b.login(username="*****",password="*****")
# here in the follow function we need to give the username of the
# instagram account which we want to follow
b.follow("*****")
#here in the upload photo function we need frst give the url of the pic 
# which we want to ulpoad and the caption if required, caption parameter is
# an optional parameter
b.upload_photo("*****",caption="*****")
# here in the unfollow function we need to give the username of the
# instagram account which we want to unfollow
b.unfollow("*****")
# here in the send message function first we need to write the message 
# we want to send and in the second parameter we need to give the usernames
# we can send to multiple users if we want beacaue second parameter is a list
b.send_message("*****",["*****"])
# here in the get user followers function we need to give the username
# of the logged in account to get the details of the followers  
followers = b.get_user_followers("*****")
for f in followers:
    print(b.get_user_info(f))
# here in the get user followings function we need to give the username
# of the logged in account to get the details of the followings  
following = b.get_user_following("*****")
for f in following:
    print(b.get_user_info(f))
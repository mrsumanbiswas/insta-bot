from instabot import Bot as insta


class Bot():
    def __init__(
        self,
        username:str,
        password:str
    ) -> None:
        self.bot = insta()
        self.bot.login(username=username,password=password)

    def upload_image(
        self,
        photo:str,
        caption:str,
    ):
       """
        Upload photo to Instagram

        @param photo Path to photo file (String)

        @param caption Media description (String)
       """
       return self.bot.upload_photo(photo,caption,None,False)

    def upload_video(self,video:str,caption:str,thumbnail:str):
        """
        Upload video to Instagram

        @param video Path to video file (String)

        @param caption Media description (String)

        @param thumbnail Path to thumbnail for video (String). 
        """
        return self.bot.upload_video(video,caption,thumbnail)

    def upload_story(self,photo:str):
        """
        Upload story photo to Instagram
        """
        return self.bot.upload_story_photo(photo)

    def send_message(self,text:str,user_ids:list):
        """
        send message to user(s).
        """
        return self.bot.send_message(text,user_ids)

    def follow(self,user_ids:list):
        """
        follw a user
        """
        return self.bot.follow_users(user_ids)
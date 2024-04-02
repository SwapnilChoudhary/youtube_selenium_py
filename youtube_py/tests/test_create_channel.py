import unittest
import os
from youtube_class import Youtube
import time
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

# Convert to absolute path
profile_picture_path = os.path.abspath("./tests/assets/channel_logo.jpg")
banner_picture_path = os.path.abspath("./tests/assets/channel_banner.png")
watermark_picture_path = os.path.abspath("./tests/assets/channel_logo.jpg")

class TestCreateChannel(unittest.TestCase):

    def test_create_channel_success(self):
        if not test_email or not test_password:

            self.skipTest("Test email and password not provided")

        youtube = Youtube(email=test_email, password=test_password)
        # Test the create_channel function with valid inputs
        result = youtube.create_channel(
            channel_name="Adonis Jamal",
            channel_handle="jamal283492857",
            channel_description="hello there",
            profile_picture_path=profile_picture_path,
            banner_picture_path=banner_picture_path,
            watermark_picture_path=watermark_picture_path,
            contact_email_path="contact@williamferns.com",
            links=[{"title": "Link 1", "url": "https://www.link1.com"}, {"title": "Link 2", "url": "https://www.link2.com"}]
        )

        if result:
            print(result)
            # Assert that the channel was created successfully
            self.assertEqual(result["message"], "Channel created successfully")
            self.assertIsNotNone(result["channel_id"])
            self.assertIsNotNone(result["cookies"])

        else:
            raise Exception("Channel creation failed, result is None")
        
        time.sleep(5)
        youtube.close()

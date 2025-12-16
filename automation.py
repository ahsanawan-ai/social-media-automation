# Social Media Automation Tool
# By [Your Name]

import schedule
import time
from datetime import datetime

def post_to_social_media(platform, message):
    """Function to post to social media"""
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] Posted to {platform}: {message}")
    return True

# Example posts
posts = [
    {"platform": "Facebook", "message": "Good morning! 🌞"},
    {"platform": "Instagram", "message": "Check out our new product! 🚀"},
    {"platform": "Twitter", "message": "Tech news update... #AI"}
]

# Schedule posts
for i, post in enumerate(posts):
    schedule.every().day.at(f"09:0{i}").do(
        post_to_social_media, 
        post["platform"], 
        post["message"]
    )

print("Social Media Automation Started...")
print("Posts scheduled for 9:00 AM, 9:01 AM, 9:02 AM")

# Keep running
while True:
    schedule.run_pending()
    time.sleep(1)

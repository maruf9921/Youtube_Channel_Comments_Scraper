import googleapiclient.discovery
import pandas as pd

# API configuration
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = ""  # Replace with your actual API key
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

# Function to get all video IDs from a channel
def get_channel_videos(channel_id, max_results=50):
    videos = []
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=max_results,
        type="video"
    )
    while request:
        response = request.execute()
        for item in response['items']:
            videos.append(item['id']['videoId'])
        request = youtube.search().list_next(request, response)
    return videos

# Function to get comments for a single video
def get_video_comments(video_id, max_results=100):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results
    )
    while request:
        try:
            response = request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                comments.append([
                    comment['authorDisplayName'],
                    comment['publishedAt'],
                    comment['updatedAt'],
                    comment['likeCount'],
                    comment['textDisplay']
                ])
            request = youtube.commentThreads().list_next(request, response)
        except googleapiclient.errors.HttpError as e:
            if e.resp.status == 403 and 'commentsDisabled' in str(e.content):
                print(f"Comments are disabled for video ID: {video_id}. Skipping...")
                break
            else:
                raise e
    return comments

# Main function to scrape comments from all videos in a channel
def scrape_channel_comments(channel_id):
    try:
        video_ids = get_channel_videos(channel_id)
        all_comments = []
        for video_id in video_ids:
            print(f"Fetching comments for video ID: {video_id}")
            comments = get_video_comments(video_id)
            all_comments.extend(comments)
        df = pd.DataFrame(all_comments, columns=['author', 'published_at', 'updated_at', 'like_count', 'text'])
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to save DataFrame to Excel
def save_to_excel(df, filename='comments.xlsx'):
    try:
        df.to_excel(filename, index=False)
        print(f"Comments saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving to Excel: {e}")

# Example usage
channel_id = ""  # Replace with the actual channel ID
df_comments = scrape_channel_comments(channel_id)
if df_comments is not None:
    df_comments.head()
    save_to_excel(df_comments)
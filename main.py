from pytube import YouTube
import os

def download_youtube_video(video_url, save_path):
    try:
        yt = YouTube(video_url)

        video_stream = yt.streams.filter(progressive=True, file_extension="mp4").first()

        # This displays the video details
        print(f"Downloading: {yt.title}")
        print(f"From: {video_url}")
        print(f"Resolution: {video_stream.resolution}")
        print(f"File size: {video_stream.filesize // (1024 * 1024)} MB")
    
        # Download video
        video_stream.download(save_path)
        print(f"Congrats! the video downloaded successfully! It's Saved at: {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Enter the youtube video URL
    video_url = input("Enter the YouTube video URL: ")

    # Specify the folder to save the video
    save_path = input("Enter the folder to save the video (e.g., C:\\Users\\YourName\\Downloads): ")
    
    # Making sure the save path exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    download_youtube_video(video_url, save_path)

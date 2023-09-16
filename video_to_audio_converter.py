import streamlit as st
import moviepy.editor as mp

def video_to_audio(video_path):
    try:
        # Load the video clip
        video = mp.VideoFileClip(video_path)

        # Extract the audio from the video
        audio = video.audio

        # Define the output audio file path
        audio_path = 'output_audio.mp3'

        # Write the audio to the output file
        audio.write_audiofile(audio_path)

        return audio_path, video.duration
    except Exception as e:
        return str(e), None

if __name__ == "__main__":
    st.title("Video to Audio Converter")

    video_file_buffer = st.file_uploader("Upload a video", type=['mp4', 'mov', 'avi', 'gif', 'webm'])

    if video_file_buffer:
        st.text('Input Video')
        st.video(video_file_buffer)

        if st.button("Convert Video to Audio"):
            try:
                video_path = "temp_video.mp4"
                with open(video_path, "wb") as f:
                    f.write(video_file_buffer.read())

                audio_path, video_duration = video_to_audio(video_path)

                if video_duration:
                    st.write(f"Video Duration: {video_duration:.2f} seconds")  # Display the duration

                st.audio(audio_path, format="audio/mp3")

            except Exception as e:
                st.error(f"An error occurred during video to audio conversion: {str(e)}")

    else:
        st.warning("Please upload a video file.")

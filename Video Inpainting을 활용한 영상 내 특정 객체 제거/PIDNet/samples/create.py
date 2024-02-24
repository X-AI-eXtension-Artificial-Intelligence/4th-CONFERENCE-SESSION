import cv2

def save_video_frames_as_images(video_path, output_folder):
    """
    비디오를 불러와서 각 프레임을 이미지 파일로 저장합니다.
    
    :param video_path: 비디오 파일 경로
    :param output_folder: 이미지 파일을 저장할 폴더 경로
    """
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame_count += 1
        frame_filename = f"{output_folder}/frame_{frame_count:05}.png"
        cv2.imwrite(frame_filename, frame)

    cap.release()
    print(f"총 {frame_count}개의 프레임이 저장되었습니다.")

# 비디오 경로 및 출력 폴더 설정 (이 부분은 실제 경로로 수정해야 합니다)
video_path = "samples/video/running_video.mp4"
output_folder = "samples/frames"

# 함수 호출
save_video_frames_as_images(video_path, output_folder)
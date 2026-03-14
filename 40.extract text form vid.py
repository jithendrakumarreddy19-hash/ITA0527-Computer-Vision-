import cv2
import pytesseract

def extract_text_from_video(video_path):

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    cap = cv2.VideoCapture(video_path)

    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Show the video
        cv2.imshow("Video", frame)

        # Process every 20th frame for OCR
        if frame_count % 20 == 0:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

            _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

            text = pytesseract.image_to_string(thresh)

            if text.strip() != "":
                print("Detected Text:")
                print(text)
                print("----------------------")

        # Press q to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


video_path = r"C:\Users\jithe\OneDrive\Documents\opencv\istockphoto-1384856881-640_adpp_is.mp4"

extract_text_from_video(video_path)
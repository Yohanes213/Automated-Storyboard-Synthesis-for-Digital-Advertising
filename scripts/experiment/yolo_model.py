import ultralytics

def detect_objects(image_path):
    """Detects objects in an image using YOLOv8.

    Args:
        image_path: Path to the image file.

    Returns:
        A list of detected objects with bounding boxes and confidence scores.
    """

    # Load the YOLOv8 model
    model = ultralytics.YOLO('yolov8n.pt')

    # Detect objects in the image
    results = model.predict(image_path, conf=0.5)#, save_dir = 'data')  # Adjust confidence threshold as needed

    # Extract detected objects
    #detections = results[0].xyxy[0].numpy()
    results.save(save_dir='save')

    return results


if __name__ == "__main__":
    print(detect_objects('data/0a59be2e7dd53d6de11a10ce3649c081/thumbnail-new.jpg'))
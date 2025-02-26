import face_recognition
import os


def load_known_faces(known_faces_dir):
    """
    Loads and encodes known faces from the specified directory.

    Args:
        known_faces_dir (str): Path to the directory containing known face images.

    Returns:
        known_face_encodings (list): A list of encoded face data.
        known_face_names (list): A list of names corresponding to the known face encodings.
    """
    known_face_encodings = []  # Will store the encoded face data
    known_face_names = []      # Will store the names of the people

    # Loop through each image file in the known_faces directory
    for filename in os.listdir(known_faces_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(image_path)

            # Extract facial encodings (list of face encodings found in the image)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_face_encodings.append(encodings[0])  # Assuming one face per image
                # Use the file name (without extension) as the person's name
                name = os.path.splitext(filename)[0]
                known_face_names.append(name)
                print(f"✅ Loaded encoding for {name}")
            else:
                print(f"⚠️ No faces found in {filename} - please use clear face images.")

    return known_face_encodings, known_face_names


def recognize_faces_in_image(image_path, known_face_encodings, known_face_names, tolerance=0.6):
    """
    Identifies known faces in an image by comparing them to the known encodings.

    Args:
        image_path (str): Path to the image for face recognition.
        known_face_encodings (list): Encoded face data of known individuals.
        known_face_names (list): Names corresponding to the known encodings.
        tolerance (float): How strict the matching should be (lower = stricter).

    Returns:
        recognized_names (list): Names of the recognized individuals or 'Unknown' if not matched.
    """
    # Load and process the target image
    image = face_recognition.load_image_file(image_path)

    # Detect face locations and encodings in the target image
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    recognized_names = []

    # Loop through each face found in the target image
    for face_encoding in face_encodings:
        # Compare this face encoding with all known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance)

        # Default to 'Unknown' if no match is found
        name = "Unknown"

        # If we found a match, get the first match's index and assign the corresponding name
        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]

        recognized_names.append(name)

    return recognized_names


if __name__ == "__main__":
    # Example usage
    known_faces_dir = "./known_faces"
    image_to_process = "./images_to_process/sample.jpg"

    print("🔄 Loading known faces...")
    known_face_encodings, known_face_names = load_known_faces(known_faces_dir)

    print(f"🔍 Recognizing faces in {image_to_process}...")
    results = recognize_faces_in_image(image_to_process, known_face_encodings, known_face_names)

    print(f"✨ Faces recognized in {image_to_process}: {results}")

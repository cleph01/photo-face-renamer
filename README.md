# Photo Face Renamer

Welcome to **Photo Face Renamer**, an open-source tool designed to help you organize and secure your photo collection with facial recognition technology. This software renames photos based on recognized faces or adds descriptive filenames when faces can't be recognized, ensuring your photos are organized and easy to find, all while keeping your data private and under your control.

This project is part of the **John Connor Project**, a mission dedicated to empowering individuals with digital sovereignty and protecting privacy in an age of surveillance and centralized cloud services.

---

## **Project Overview**

In today's world, personal data is often stored and processed by large, centralized cloud services, leaving users vulnerable to surveillance, data breaches, and loss of control over their own information. The **Photo Face Renamer** was created to help individuals take back control by providing an easy-to-use tool that works **locally** on your own devices, without relying on any cloud service.

With **Photo Face Renamer**, you can:

- **Rename photos** based on the people detected in them using facial recognition.
- **Store your photos locally** on your own NAS or storage device, protecting your family's privacy from third-party surveillance.
- **Automate the organization** of your photo library, making it easier to sort and search through your personal media.
- **Ensure your digital sovereignty**, disconnecting from centralized services like iCloud, Google Photos, or Dropbox.

This tool is designed to be simple yet powerful, allowing anyone to easily set up a local photo storage and management system. It’s perfect for individuals who want to protect their privacy and stop relying on third-party services for something as personal as their family photos.

---

## **Why This Project?**

In line with the **John Connor Project**'s mission, this software aims to help users break free from the control of large tech companies, enabling them to take control of their own data and privacy. By running this software locally, users can avoid the dangers of centralized cloud providers, ensuring that their personal information, like photos, stay private and secure.

We believe in **Digital Sovereignty**—the idea that individuals should have full control over their own data and digital lives. This tool is a small step toward that goal, offering a free, open-source alternative to centralized services that compromise privacy.

---

## **Features**

- **Face Detection & Recognition**: Automatically detects and recognizes faces in photos.
- **Descriptive Filenames**: If no faces are detected, the tool generates descriptive filenames based on the content of the image.
- **Local Storage**: All photos and data remain on your device, giving you full control over your privacy.
- **Open-Source**: Built with transparency and community collaboration in mind. You can contribute to the project, report bugs, or help improve the software.
- **Handle multiple images per person** to improve recognition accuracy over time.

- Built-in logic to handle age differences by comparing multiple encodings per person.

- **CLI functionality for easy face training** and batch photo processing (Goal is to eventually deploy as webapp).

---

## **Project Structure**

```
photo-face-renamer/
│
├── known_faces/               # User adds known faces here (one folder per person)
│   ├── john_doe/
│   │   ├── john_25.jpg
│   │   ├── john_35.jpg
│   │   └── john_45.jpg
│   └── jane_smith/
│       ├── jane_teen.jpg
│       └── jane_30s.jpg
│
├── data/                      # Stores serialized data (encodings, etc.)
│   └── known_faces.pkl
│
├── photos_to_process/         # Folder for photos to be processed
│
├── processed_photos/          # Output folder with renamed photos
│
├── main.py                    # Main CLI entry point
│
├── requirements.txt           # Dependencies
│
├── LICENSE                    # MIT License
│
└── README.md                  # Project documentation (this file)
```

---

## **Handling Age Differences**

The facial recognition component considers facial changes over time by:

- Allowing multiple images per person in the known_faces/ folder. The application will compare target photos against all encodings for each person.

- Adjusting the recognition threshold as needed for better accuracy.

To improve accuracy:

- Add images showing different ages and appearances (e.g., different haircuts, with/without facial hair).

- Higher threshold values may reduce false negatives but could increase false positives. The default is 0.6.

---

## **Installation**

To get started with the **Photo Face Renamer**, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/photo-face-renamer.git
   cd photo-face-renamer
   ```

2. **Set up a virtual environment:**

   - On **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     # cd into your project directory and run the following
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the program:**
   ```bash
   python src/main.py
   ```

---

## **Usage**

To use the **Photo Face Renamer**, simply place your images in a folder and run the program. The tool will process your photos, detect faces, and rename them accordingly. If it can't recognize any faces, it will assign a descriptive name to the image based on its contents.

You can customize how photos are named and add new known faces to improve recognition over time.

---

## **Contributing**

We welcome contributions to this project! If you have an idea for improving the software or would like to fix a bug, please feel free to fork the repository and submit a pull request. Make sure to follow these guidelines:

- Open an issue first to discuss the change you want to make.
- Write tests for any new features or bug fixes.
- Ensure your code adheres to the project's style.

---

## **License**

This project is licensed under the **MIT License** - see the [LICENSE](./LICENSE) file for details.

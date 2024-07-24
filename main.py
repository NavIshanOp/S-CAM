import cv2
# import os
import serial
import time

# Function to initialize and start the camera
def start_camera():
    print("Attempting to start camera...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture")
        return None
    print("Camera started successfully.")
    return cap

# Function to initialize video writer
def start_video_writer(filename):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    return cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

# Function to release and stop the camera and video writer
def stop_camera_and_writer(cap, out):
    if cap:
        print("Stopping camera...")
        cap.release()
    if out:
        print("Stopping video writer...")
        out.release()
    cv2.destroyAllWindows()
    print("Camera and video writer stopped.")

# Function to listen for motion triggers from the ESP32 via the serial port
def listen_for_motion_trigger(serial_port):
    try:
        ser = serial.Serial(serial_port, 115200, timeout=1)
        print("Listening for motion trigger on serial port...")

        cap = None
        out = None

        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(f"Received data: {line}")

                if "Motion detected" in line:
                    if cap is None:
                        cap = start_camera()
                        if cap:
                            timestamp = time.strftime("%Y%m%d-%H%M%S")
                            filename = f"recordings/recording_{timestamp}.avi"
                            out = start_video_writer(filename)
                elif "No Motion Detected" in line:
                    if cap is not None:
                        stop_camera_and_writer(cap, out)
                        cap = None
                        out = None

            # Capture video if camera is active
            if cap and out:
                ret, frame = cap.read()
                if ret:
                    out.write(frame)
                else:
                    print("Error: Failed to capture frame")
                    stop_camera_and_writer(cap, out)
                    cap = None
                    out = None

    except serial.serialutil.SerialException as e:
        print(f"Error opening serial port {serial_port}: {e}")

if __name__ == "__main__":
    serial_port = 'COM7'  # Change to your serial port (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux)
    listen_for_motion_trigger(serial_port)
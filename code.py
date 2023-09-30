import speech_recognition as sr
import RPi.GPIO as GPIO

def voice_control():
    # Set up GPIO pins
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    
    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the microphone as the source
    with sr.Microphone() as source:
        print("Say something!")
        try:
            audio = r.listen(source)
        except Exception as e:
            print(f"Error listening to audio: {str(e)}")
            return

    try:
        # Use Google's speech recognition service
        command = r.recognize_google(audio)

        # Check the command and output the device ID and state
        if "device one" in command:
            print("Device ID: 1")
            if "on" in command:
                GPIO.output(11, GPIO.HIGH)
                print("Device state: ON")
            elif "off" in command:
                GPIO.output(11, GPIO.LOW)
                print("Device state: OFF")
        elif "device two" in command:
            print("Device ID: 2")
            if "on" in command:
                GPIO.output(13, GPIO.HIGH)
                print("Device state: ON")
            elif "off" in command:
                GPIO.output(13, GPIO.LOW)
                print("Device state: OFF")
        else:
            print("Invalid command")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {str(e)}")

    # Clean up GPIO pins
    GPIO.cleanup()

# Call the function to run
voice_control()

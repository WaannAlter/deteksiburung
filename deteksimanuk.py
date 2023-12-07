import subprocess
from pathlib import Path
from playsound import playsound

# Path to your custom sound notification script
sound_script_path = 'suara.py'

# Path to your detect.py script
detect_script_path = 'detect.py'

# Set the desired confidence threshold
confidence_threshold = 0.7

# Run the detect.py script with the specified confidence threshold
detection_result = subprocess.run(
    ['python', detect_script_path, '--weights', 'best.pt', '--source', '0', '--conf-thres', str(confidence_threshold)],
    capture_output=True
)

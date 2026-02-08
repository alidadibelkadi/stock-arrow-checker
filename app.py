import cv2
import numpy as np

def analyze_stock_arrow(image_path):
    # Load the screenshot
    img = cv2.imread(image_path)
    if img is None:
        return "Error: Image not found."

    # Convert to HSV color space for better color detection
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define color ranges
    # Green (Up)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    
    # Red (Down) - Red wraps around in HSV
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Create masks
    mask_g = cv2.inRange(hsv, lower_green, upper_green)
    mask_r1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_r2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_r = cv2.add(mask_r1, mask_r2)

    # Count pixels to see which color dominates
    green_pixels = cv2.countNonZero(mask_g)
    red_pixels = cv2.countNonZero(mask_r)

    if green_pixels > red_pixels and green_pixels > 50:
        return "🚀 Stock is going UP (Green detected)"
    elif red_pixels > green_pixels and red_pixels > 50:
        return "🔻 Stock is going DOWN (Red detected)"
    else:
        return "Could not determine direction. Try a clearer screenshot."

# Test the function
# Replace 'arrow.png' with your file name
print(analyze_stock_arrow('arrow.png'))

import time
import numpy as np

def get_AB_AC_angle(xA, yA, xB, yB, xC, yC):
    # Define your points (A, B, C)
    A = np.array([xA, yA])  # Replace xA, yA with the coordinates of point A
    B = np.array([xB, yB])  # Replace xB, yB with the coordinates of point B
    C = np.array([xC, yC])  # Replace xC, yC with the coordinates of point C
    
    # Create vectors AB and AC
    AB = B - A
    AC = C - A
    
    # Calculate the angle using arctan2
    angle = np.arctan2(AC[1], AC[0]) - np.arctan2(AB[1], AB[0])
    
    # Normalize the angle to be between 0 and 2π (0 and 360 degrees)
    angle = np.mod(angle, 2 * np.pi)
    
    # Convert angle to degrees
    angle_degrees = np.degrees(angle)
    
    return(angle_degrees)

def print_remaining_time(start_time, elapsed_time, current_frame, frame_total):
    total_estimated_time = elapsed_time * frame_total
    remaining_time = total_estimated_time * (frame_total - current_frame) / frame_total
    print(f"{current_frame} of {frame_total} frames processed: {(remaining_time/60):.2f} mins left", end='\r', flush=True)


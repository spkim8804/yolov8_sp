import time

def print_remaining_time(start_time, elapsed_time, current_frame, frame_total):
    total_estimated_time = elapsed_time * frame_total
    remaining_time = total_estimated_time * (frame_total - current_frame) / frame_total
    print(f"{current_frame} of {frame_total} frames processed: {(remaining_time/60):.2f} mins left", end='\r', flush=True)

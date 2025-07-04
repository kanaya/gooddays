from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size):
    # Create a new image with white background
    image = Image.new('RGBA', (size, size), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Calculate dimensions
    margin = size * 0.1
    box_size = size * 0.8
    
    # Draw a green square
    draw.rectangle([
        (margin, margin),
        (margin + box_size, margin + box_size)
    ], fill=(76, 175, 80))
    
    # Draw a calendar icon
    line_width = size * 0.05
    draw.line([
        (margin + line_width, margin + box_size - line_width),
        (margin + box_size - line_width, margin + box_size - line_width)
    ], fill=(255, 255, 255), width=int(line_width))
    
    draw.line([
        (margin + line_width, margin + box_size - line_width - line_width),
        (margin + box_size - line_width, margin + box_size - line_width - line_width)
    ], fill=(255, 255, 255), width=int(line_width))
    
    draw.line([
        (margin + line_width, margin + line_width),
        (margin + line_width, margin + box_size - line_width)
    ], fill=(255, 255, 255), width=int(line_width))
    
    draw.line([
        (margin + line_width + line_width, margin + line_width),
        (margin + line_width + line_width, margin + box_size - line_width)
    ], fill=(255, 255, 255), width=int(line_width))
    
    # Save the image
    image.save(f'images/icon{size}.png')

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Generate icons in different sizes
create_icon(48)
create_icon(128)

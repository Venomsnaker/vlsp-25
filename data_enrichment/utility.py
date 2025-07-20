import os

def load_img_paths(folder):
    files = os.listdir(folder)
    img_extensions = {'.jpg', '.png'}
    
    img_paths = [os.path.join(folder, f) for f in files if os.path.splitext(f)[1].lower() in img_extensions]
    return img_paths
    
    
import requests
import os
import imageio
import time
from datetime import datetime

def download_image(url, folder):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = os.path.join(folder, f"image_{timestamp}.jpg")
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename
    else:
        print(f"[{datetime.now()}] Failed to download image:", response.status_code)
        return None

def create_gif(image_files, folder):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    gif_filename = os.path.join(folder, f"images_{timestamp}.gif")
    with imageio.get_writer(gif_filename, mode='I') as writer:
        for image_file in image_files:
            image = imageio.imread(image_file)
            writer.append_data(image)
    return gif_filename

def main():
    image_count = 0
    image_files = []
    image_folder = "images"
    gif_folder = "gifs"
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    if not os.path.exists(gif_folder):
        os.makedirs(gif_folder)

    while True:
        # download image
        image_url = "https://webcama1.watching-grass-grow.com/current.jpg"
        filename = download_image(image_url, image_folder)
        if filename:
            print(f"[{datetime.now()}] Downloaded image: {filename}")
            image_files.append(filename)
            image_count += 1

        # time to make a gif?
        # set line 49 to 60 for 1 GIF per hour, 240 for 1 GIF per 4 hours (codespace max keepalive)
        if image_count == 60:
            gif_filename = create_gif(image_files, gif_folder)
            print(f"[{datetime.now()}] Created GIF: {gif_filename}")

            # delete images
            for image_file in image_files:
                os.remove(image_file)
                print(f"[{datetime.now()}] Deleted image: {image_file}")
            image_files = []
            image_count = 0

        # wait 1m and take another pic
        time.sleep(60)

if __name__ == "__main__":
    main()

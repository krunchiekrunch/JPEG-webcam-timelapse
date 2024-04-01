# JPEG webcam timelapse maker

## Instructions

1. Download the main.py
2. Run `pip install requests imageio` to install the required modules
3. Run `python main.py` in the terminal

The script will create 2 folder, images and gifs

The script will grab a image from [here](https://assets4.webcam.io/w/MmqrKM/latest.jpg) every minute (Customisable on line 40)

It will make a gif from the images every 60 minute (Customisable on line 49)

Each frame of the GIF last for 1ms (10fps)

After that, it will delete the images used for the gif

### Need help?

Feel free to dm me on discord for help (krunchiekrunch._.)

<@1166013268008120340>

# Info

webcam.io (The provider of the AirLive LHR webcam have their own timelapse [here](https://webcam.io/webcams/MmqrKM), more info [here](https://webcam.io/pages/time-lapse)

So if you wanted a timelapse of Heathrow airport (or any webcam hosted by webcam.io) you can just go to the website, `webcam.io/webcams/CAMERAID`, change the `CAMERAID` for the id of the webcam, you can download it from the source!

This code works for other stuff as well, it can take images from other JPEG webcam and make it into timelapses, not just limited to webcam.io

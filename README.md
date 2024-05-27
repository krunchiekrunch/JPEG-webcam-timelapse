# JPEG webcam timelapse recorder

## Instructions

1. Download the main.py
2. Run `pip install requests imageio` to install the required modules
3. Run `python main.py` in the terminal

The script will create 2 folder, images and gifs

The script will grab a image from [here](https://webcama1.watching-grass-grow.com/current.jpg) every minute (Customisable on line 40)

It will make a gif from the images every 60 minute (Customisable on line 49)

Each frame of the GIF last for 1ms (I'm pretty sure it's 1ms, or whatever the default value of imageio is)

After that, it will delete the images used for the gif

### Need help?

Feel free to dm me on discord for help (krunchiekrunch._.)

<@1166013268008120340>

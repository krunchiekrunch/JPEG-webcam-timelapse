# JPEG webcam timelapse recorder

## Instructions

```
git clone https://github.com/RadioactivePotato/JPEG-webcam-timelapse.git
cd JPEG-webcam-timelapse
pip install requests imageio
python main.py
```

The script will create 2 folder, images and gifs

The script will grab a image from [here](https://webcama1.watching-grass-grow.com/current.jpg) every minute (Customisable on line 40)

It will make a gif from the images every 60 minute (Customisable on line 49)

Each frame of the GIF last for 1ms (I'm pretty sure it's 1ms, or whatever the default value of imageio is)

After that, it will delete the images used for the gif

[Here is a demo](https://github.com/RadioactivePotato/JPEG-webcam-timelapse/blob/main/example.gif)

### Need help?

Create an issue [here](https://github.com/RadioactivePotato/JPEG-webcam-timelapse/issues)

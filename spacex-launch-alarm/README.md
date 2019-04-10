Introduction
------------
Nobody wants to wake up in the middle of the night because of a SpaceX launch just to learn, that the launch was delayed. This script periodically checks for @SpaceX tweets and plays the wanted song in case it looks like there is a launch! (or anything particularly interesting, it's quite dumb, check it!)

How to run
----------
You need `virtualenv` and `Python3`. To check and setup the environment you can try running:
```
$ ./boostrap.sh
```

If that succeeds, follow the instructions it gives to source virtual environment and install 3rd party Python modules. Otherwise you need to set up the virtual environment manually.

Get your favorite song in mp3 - you are expected to play David Bowie's Starman!

Run it with
```
$ python spacex_launch_alarm.py --mp3-file <mp3-song> &
```

Enjoy the launch, even in the middle of the night

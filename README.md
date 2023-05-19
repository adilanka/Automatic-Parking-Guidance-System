# Automatic-Parking-Guidance-System
<b>Motivation</b><br>
The main motivation which motivated us to do so is the necessity of finding a parking for our cars.
I was thinking that even after so much growth in technology we still had to take tension of parking
but I knew that technology is the solution of this problem too and this made us motivated to build a
parking guidance system and after that we were thinking about what were some of the other
activities and problems which we could solve using bots and technology and all these motivations
has landed us to build this project.

<b>Objective</b><br>
Our main objective is to understand the ground level problems which people face and if possible,
make a bot which can solve the problem. We also aim to make these bots easy to use, accessible in
a place on the internet where everyone can get the bots which can help them in their daily activities
like parking, security etc (Similar to a play store but we will use a website.). The bot which we will
be making is the Automatic Parking Guidance system. Our objective with this bot is to make an
affordable way to make parking lots easier to navigate and use. Thus, making the overall parking
experience more convenient for the user.
Working Principle

The bot uses OpenCV and CVZone in combination to detect parking spots and also for checking 

the presence of Car in the spot. The OpenCV module of python is used to read and preprocess the 

image. The CVZone module is used to detect the vehicle in the mapped parking spot.

The parking spots are mapped and stored in Pickle file which can be retrieved multiple times once

it has been created and saved.

Python Modules used: -

• OpenCV

• CV Zone

• Pickle

Parking Spot Detection

The first step would be deciding the bounds of the box used to map the parking spot in the image. 

After that, we need to left click on each parking spot to select the area and save the coordinates in 

the pickle file. We can delete the wrongly selected places by right clicking in the box.

Vehicle Detection using video and image

First the marked spots are separated and then we apply Gaussian Blur and adaptive thresholding to 

the image to reduce the noise which might be there in the image or the video and separate the pixels 

into the background or foreground. Then using pixel count for the foreground pixels, we determine 

whether the spot has a vehicle or not.

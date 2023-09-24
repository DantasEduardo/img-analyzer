# img-analyzer
This is a college project of satellite image recognition for rain forecasting.

# Algorithm
In this algorithm were used steps to transforming the image to shades of gray, thresholding that serves to separate objects from the image backgorund determined by a value fixed between 0 and 255, then is used morphologyEx function to remove possible noises with a morphological opening operation which involves erosion techniques followed by dilation in the foreground, with erosion being a technique to leave the foreground completely white and the background completely dark, dilation that dilates the foreground then is cauculated the percentage of white pixels in image, being the white pixels the clouds

## Step 1
I use a script to crop the image to zoom in on the image and better center the map of Brazil.

## Step 2
After the cropped image, I use some preparation steps to use some steps of image segmentation to find the percentage of clouds in the map.
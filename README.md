# 😷 VGG16 feature extraction for face identification (mask and no mask)

Using the VGG16 neural network it's possible to extract singular features for 
different kind of people, and then use this to identify them, even in 
positions or angles. 

In the pandemy, with the usual algorithms, was hard to realize the accomplish 
the facil recognition with masks in face, because the training set of the 
networks was people withou mask until then.

# Motivation

Neural networks (NNs) needs to be trained all over again when inserting a new 
person as a different type of classification, but extracting the features 
we can build a database with singular information of people faces and remove 
the need of retraining the entire NN.

So, if you need the system to identify a new person, you just need to pass 
photos of he's face and the NN will extract the features and insert them 
into the database.

Even if the person wears mask, the feature extraction captures features 
in parts of the face that can be used to recognize the person with or without 
mask.
 
# How the recognition works

The features are arrays of type float32. So, if a image is passed to 
recognition, it's calculated the euclidean distance between the input and 
all the images in the database. The minimum distance will show the most 
familiar face in the database with the input, and the system will return 
the person name.

For this problem the distance was calculated using the minkowski distance 
function, but with the parameter p equals 2, defining the euclidean 
distance.

# TODOs

* Explores different types of distance to better fit the similarity.
* Try different types of feature extractors.
* Frame of the architecture outputed from tensorboard.

# New Version

* Graphic interface (maybe tkinter).
* Real-time face recognition and insertion of new faces at the database.
* Usage of SGBD's instead of python lists (maybe PostgreSQL or even SQLite).
* Registration of access with datetime data and name in a csv file.

# Author

[Pedro Malandrin Klesse](www.github.com/Klesse)


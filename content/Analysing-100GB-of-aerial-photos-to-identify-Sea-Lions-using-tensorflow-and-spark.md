Title: Analysing 100GB of aerial photos to identify Sea Lions using tensorflow and spark on AWS
Date: 2017-6-12 10:20
Category: Machine Learning
Tags: convnets, convolutional neural networks, machine learning, spark, parallel processing, python


With this post I will attempt to describe the approach I followed in order to analyze 100GB of image data for the purpose of counting sea lions as part of the [this](https://www.kaggle.com/c/noaa-fisheries-steller-sea-lion-population-count) kaggle competition. The reason why I found this competition an interesting challenge was threefold: it was for a good cause, it was a good opportunity to apply recently acquired knowledge about convnets/tensorflow and finally, it was a nice example of using spark as a parallel processing engine to speed up single-threaded applications. 

#### The competition

If you are not familiar with kaggle competitions, most of the time they follow the same pattern which involves a dataset, provided to the contestants, and a submission format, usually in csv, which must be used to submit results back to kaggle. Kaggle has the corresponding ground truth data for the submissions of the contestants and based on a predefined metric function a results is calculated. In this case the above were as follows:

* **Dataset**  
The dataset consists of 18636 images that are used as test data and 949 images that are used as training data. In the case of training data, a second, annotated version of those 949 images is provided in which each sea lion is annotated using a colored dot. The size of the provided dataset in bytes is close to 100Gb, with 86GB comprising the test data and around 10GB the train data.
* **Submission format**  
blahblah
* **Evaluation metric**  
sdsdas

#### Matching the Dots

Or to be more accurate: counting the dots.

#### Training a Convolutional Neural Network

#### Brute forcing object detection

#### Spark, sparks creative (and a bit unorthodox) thinking

#### Putting it all together

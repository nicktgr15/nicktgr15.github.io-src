Title: Analysing 100GB of aerial photos to identify Sea Lions using tensorflow and spark on AWS
Date: 2017-6-12 10:20
Category: Machine Learning
Tags: convnets, convolutional neural networks, machine learning, spark, parallel processing, python


With this post I will attempt to describe the approach I followed in order to analyze 100GB of image data for the purpose of identifying sea lions in aerial photos as part of [this](https://www.kaggle.com/c/noaa-fisheries-steller-sea-lion-population-count) kaggle competition. The reason why I found this competition an interesting challenge was threefold: was for a good cause, was a good opportunity to apply recently acquired knowledge about convnets/tensorflow and finally, was a nice example of using spark as a parallel processing engine to speed up single-threaded applications. 

#### The competition

If you are not familiar with kaggle competitions, most of the time they follow the same pattern which involves a dataset, provided to the contestants, and a submission format, usually in csv, which must be used as a template to submit results back to kaggle. Kaggle has the corresponding ground truth data for the submissions of the contestants and based on a predefined metric function a results is calculated. In this case the above were as follows:

* **Dataset**  
The dataset consists of 18636 images that are used as test data and 949 images that are used as training data. In the case of training data, a second, annotated version of those 949 images is provided in which each sea lion is annotated using a colored dot. The size of the provided dataset in bytes is close to 100GB, with 86GB comprising the test data and around 10GB the train data.
* **Submission format**  
The classification results is expected to be submitted using the following csv format. The `test_id` represents the test image from which the corresponding counts for each type of sea lion have been calculated. It's obvious that during the evaluation the only processing that takes place in kaggle is the comparison of the submitted results with the ground truth i.e. validation is quick.
       
        ::csv
        test_id,adult_males,subadult_males,adult_females,juveniles,pups
        0,1,1,1,1,1
        1,1,1,1,1,1
        2,1,1,1,1,1
        etc
        

* **Evaluation metric**  
The submitted results are evaluated using the Root Mean Square Error (RMSE) metric, averaged over the available columns (i.e. for the different types of sea lions)

    $RMSE_{avg} = \frac{1}{5}(\sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_{adult-males} - \hat{y}_{adult-males})^2} + ... + \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_{pups} - \hat{y}_{pups})^2})$

#### Matching the Dots


Or to be more accurate: counting the dots.

#### Training a Convolutional Neural Network

#### Brute forcing object detection

#### Spark, sparks creative (and a bit unorthodox) thinking

#### Putting it all together

Title: Analysing 100GB of aerial photos to identify Sea Lions using tensorflow and spark on AWS
Date: 2017-6-12 10:20
Category: Machine Learning
Tags: convnets, convolutional neural networks, machine learning, spark, parallel processing, python


With this post I will attempt to describe the approach I followed in order to analyze 100GB of image data for the purpose of identifying sea lions in aerial photos as part of [this](https://www.kaggle.com/c/noaa-fisheries-steller-sea-lion-population-count) kaggle competition. The reason why I found this competition an interesting challenge was threefold: was for a good cause, was a good opportunity to apply recently acquired knowledge about convnets/tensorflow and finally, was a nice example of using spark as a parallel processing engine to speed up single-threaded applications. 

#### The competition

If you are not familiar with kaggle competitions, most of the time they follow the same pattern which involves a dataset, provided to the contestants, and a submission format, usually in csv, which must be used as a template to submit results back to kaggle. Kaggle has the corresponding ground truth data for the submissions of the contestants and based on a predefined metric function a results is calculated. In this case, the above were as follows:

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

Or to be more accurate: finding and counting the dots. In the following figure an example image from the training dataset is presented. The training dataset images come in two versions, a plain image and a dotted image. On the dotted image each dot represents the location of a sea lion, while its colour indicates the corresponding sea lion type/class. As already mentioned, there are 5 types/classes of sea lions in the training data `adult_males, subadult_males, adult_females, juveniles, pups`.

<img style="width:100%;margin:auto;display:block;" src="/images/blob_detection.png"/>

In the above figure three different versions of an example training image are presented. On the left side, the dotted version, in the middle, the absolute difference between the dotted and non-dotted images and finally, on the right side, the 64x64 pixels bounding boxes indicating the actual regions of the image that will be used as training samples for each class. The Laplacian of Gaussian blob detection algorithm is used to get the locations of the dots appearing on the middle image and when those locations are retrieved the type/colour of the corresponding sea lion is extracted from the original dotted training image. 

This whole, devious procedure is required because of the way the training data were provided by the competition organisers i.e. as part of the image so the coordinates and class information need to be extracted through some kind of post-processing. For each training image a dictionary like the following is generated.

```
{
    "sea-lions": {
        "adult_males": [
                [dot_x, dot_y],
                ...
        ],
        "subadult_males": [ ... ],
        "adult_females": [ ... ],
        "juveniles": [ ... ],
        "pups": [ ... ],
    },
    "filename": image_filename
}
```

#####  Spark, sparks creative (and a bit unorthodox) thinking

To speedup the above procedure, which was underutilising the multiple cores available on my macbook, an attempt to parallelise it using spark was made. Spark is quite straightforward to run locally in standalone mode, and will by default utilise all available cpu resources. As long as Java is installed, the binaries can be downloaded from [https://spark.apache.org/downloads.html](https://spark.apache.org/downloads.html) and after extracting the contents of the archive a spark job can be executed as follows:

```
./spark-2.1.1-bin-hadoop2.7/bin/spark-submit my_pyspark_job.py
```

With this spark job we wanted to achieve the following:  

* From each training image extract metadata with the coordinates of the sea lions 
* From each training image generate 64x64 thumbnails centered on the coordinates extracted in the previous step  

Let's go through the actual code.

```
#!python
import json
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import SparkConf, SparkContext
import util

conf = SparkConf().setAppName("Kaggle-Sea-Lions")
sc = SparkContext(conf=conf)
sc.setLogLevel('ERROR')

filepaths = util.get_training_data_file_paths(dataset_path='../dataset')

# extract training metadata 
metadata = sc.parallelize(filepaths).map(util.extract_training_data).collect()

with open("training_metadata.json", "wb") as f:
    json.dump(metadata, f)

# create thumbnails for every sea lion in the training data
sc.parallelize(results).map(util.extract_training_images).collect()
```

* **lines 7-9**: Spark job initialisation and metadata
* **line 11**: `filepaths` contains the absolute locations of the training images after some filtering to remove a subset of images flagged as inappropriate for training by the organisers
* **line 14**: This is an example of a Resilient Distributed Dataset (RDD) in spark. The `parallelize` function receives as input a list containing the available training images and using the `map` function applies the metadata extraction function `util.extract_training_data(training_image)` to each one of them. In spark terminology, the `parallelize` and `map` are considered "transformations" and as such no processing is triggered by them. The processing is triggered using an "action", which in this case is the `.collect()` call which fetches the entire RDD to the driver. The RDD returned is a list with the metadata dictionaries described earlier.
The following screenshot from the spark ui shows that only one executor is created when running locally in standalone mode and that executor is able to execute 8 tasks in parallel which in this case is equal to the  4 cores x 2 threads of an intel i7 cpu.

<img style="width:100%;margin:auto;padding-left:50px;display:block;" src="/images/executor.png"/>

#### Training a Convolutional Neural Network

#### Brute forcing object detection


#### Putting it all together

Applications
============

Image segmentation
------------------

This application performs image segmentation in TIF images (supports either
a single image or volume).

.. figure:: figures/seg_demo.png
   :scale: 27 %
   :alt: map to buried treasure
   :align: center

   MLExchange Image segmentation webpage

Currently available ML models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Random Forest (supervised learning)
  [`adapted from Dash example code <https://github.com/plotly/dash-sample-apps/blob/d96997bd269deb4ff98b810d32694cc48a9cb93e/
  apps/dash-image-segmentation/trainable_segmentation.py#L64>`__]
- pyMSDtorch (supervised learning)
  [`documentation <http://pymsdtorch.readthedocs.io>`__]
- K-Means (unsupervised learning) [ALS Howard Yanxon & Nicholas Schwartz]

Supervised vs. unsupervised learning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A supervised learning algorithm utilizes labeled datasets to train
their models, while an unsupervised learning approach does not need
this information to perform training.

Run a segmentation model in the MLExchange platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Choose a dataset** at the top left section of the app.

**Choose an ML model:** 
when choosing a supervised learning algorithm,
you need to provide annotations (labels). These annotations represent
the ground truth information that the algorithm utilizes to train the
model. 
When choosing an unsupervised algorithm, you do not need to
provide annotations. 

The segmentation app allows 2 different training options for unsupervised algorithms: 
you can mark some few images to be used for training. 
If no marks are provided, the algorithm utilizes the
entire stack of images for training. It is important to clarify that
these marks do not correspond to annotations/labels/ground truth. 

**Training:** 
select the values of the model parameters and click TRAIN.
You can check the status of the training process in the list of jobs at the bottom left
section of the app. 
To check the logs of the process, select the
corresponding job in the list and the logs will appear at the bottom
right section of the app. 

**Testing:** 
once the model is trained (marked as
completed), you can proceed to test this model. To do this, select the
dataset you want to test, and click TEST. 
You can check the status of
the testing process in the list of jobs at the bottom left section of
the app. 
Once the image stack is completely segmented, you can check the
Show Segmentation box on the right to visualize the testing results in
the graph.


Image labeling
--------------
Add desctiption soon.


Orientation pattern detection
-----------------------------
Add desctiption soon.


Peak detection
---------------
Add desctiption soon.
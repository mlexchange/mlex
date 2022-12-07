Tutorials
============

User portal
-----------
User could browse available APPs, launch the selected APPs, go to and terminate the running APPs from here.
More desciptions will be added soon. 

Content registry
-----------------

If you have a new model or workflow to use within the MLExchange services (e.g., image segmentation),
you can add it through the model registry following the steps below.

Model preparation
~~~~~~~~~~~~~~~~~

The first step to submit a new model in MLExchange is to dockerize your
script. To simplify this process, you can use the following templates:

Insert the maintainer’s name in line 2 in ``docker/Dockerfile``.

.. literalinclude:: mlex_templates/docker/Dockerfile


List the Python packages you utilized in your source code with their corresponding
versions in ``docker/requirements.txt``. 

.. literalinclude:: mlex_templates/docker/requirements.txt


Use ``src/model_name.py`` to place your algorithm. You can rename this
file according to your function/command, e.g. train.py. 
While modifying this template, please make sure to identify 3 main sections of your
code: input directory(ies), output directory(ies), and parameters.
The template indicates how to declare this information and the order in which they should be declared. 
If you have more than one input directory, you should list these directories consecutively. 
The same applies for the output directories.

.. literalinclude:: mlex_templates/src/model.py

Note: If you have more than one function/command, create another script with the same template, 
and save it with a different name, e.g. ``test.py``. 
Use ``src/model_validation.py`` to define the parameter classes (if you have any) that are used in your
source files. For validation purposes, MLExchange uses
`Pydantic <https://pydantic-docs.helpmanual.io>`__. 

.. literalinclude:: mlex_templates/src/model_validation.py

Insert your project name in line 4 in Makefile (optional).
You can add example commands in Makefile. 
Once all changes have been completed, open a terminal console and type
“build_docker”. 
You have successfully dockerized your model!

.. literalinclude:: mlex_templates/Makefile

For further assistance, please contact tanchavez@lbl.gov or
zzhao2@lbl.gov.

Model registration
~~~~~~~~~~~~~~~~~~

You can register a new model at `MLExchange Content
Registry <https://mlsandbox.als.lbl.gov/model-registry>`__.

| **Register your model**

| Create a JSON file with the description of your model (fill out the
  online form to generate your model document), and upload your model
  document to the model registry after validating the document.
  
.. figure:: figures/upload_model.png
   :scale: 62 %
   :alt: Upload model panel in the MLExchange model registry 
   :align: center
   
   "Upload Model" panel in the MLExchange Model Registry 

| **Parameter definition**

| The parameter class you previously defined for your source files
  corresponds to the GUI’s components that MLExchange automatically
  generates within its applications. You can define these parameters in
  the JSON file, or you can use the model registry form to add each GUI
  component.

Currently, the model registry supports the following 8 types of components: 

- 3 types of input box: int, float, and string
- Dropdown
- Slider
- RadioItem
- BooleanSwitch
- Graph

They look like the follows:

.. figure:: figures/gui_components.png
   :scale: 62 %
   :alt: gui components
   :align: center 
   
   8 types of automatic-generated GUI components (currently) supported by MLExchange 


Search interface
----------------
To search for available applications / models within the platform, navigate to:
`https://search.mlsandbox.als.lbl.gov <https://search.mlsandbox.als.lbl.gov>`_

Two kinds of search have been provided within the MLExchange search interface:

Text Search
~~~~~~~~~~~
To run a text search, simply type in the keyword(s) you would like to
look up for, the relevant information from content registry will be returned in the table below

Image Search
~~~~~~~~~~~~
The image search is powered by a content-based image retrieval
pipeline (pyCBIR) developed by Daniela Ushizima group - Camera (LBNL). 

To run:
1. Prepare your query image(s), it could be either one folder with all (unlabeled) or one folder per image class (labeled).
2. If you are searching for more than one image, compress them into a single file before uploading.
3. Drag and drop your file into the loading box. If you don’t see the loading box, click “Toggle File Manager”.
4. Scroll to the bottom of the file table and click on the folder you just uploaded. Hit “Import” to view your query images. If there are unwanted images from the previous run, delete them. 
5. Select the database you want to search from. Currently 3 fully-labeled sample databases are available for testing: Cells, Fibers and GISAXS. Ingesting additional labeled datasets from other applications will be available soon.
6. Select the neural network for feature extraction. 3 pre-trained models using imagenet weight are available for testing. More options to choose from other pipelines will be available in the future.
7. Select the searching method. We have implemented Faiss library (developed by Facebook AI) for efficient similarity search, and it’s recommended especially for large datasets. If you prefer traditional tree algorithms (KDTree, BallTree), these two are also available.
8. Select the number of similar images you want to retrieve and click “Search”. You will see the submitted job within the list of jobs table to the bottom.
9. Select the job to track logs, the search result will be displayed once ready. The first column is your query image while each row corresponds to similar images regarding your input image.
 

Job manager 
-----------
The job manager supervises the allocation of computing resources in MLExchange.
MLExchange hosts status can be accessed and managed at `https://job.mlsandbox.als.lbl.gov <https://job.mlsandbox.als.lbl.gov>`_
 


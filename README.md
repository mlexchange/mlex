# MLExchange
MLExchange is web-based software infrastructure that deploys machine learning models for beamline scientists.

This is our 1st release. 
It contains 2 MLExchange services, i.e., the job manager and content registry, and 1 frontend application, i.e., image segmentation, and 3 machine learning models to be used for segmentation, i.e., k-means, random forest, and Mixed-Scale Dense Convolutional Networks (MSDnets). 

All these container images will be directly pulled from [the MLExchange DockerHub](https://hub.docker.com/u/mlexchange1). 

## How to use?
1. Install Docker or Docker Desktop 
2. cd into mlex folder, then run `docker-compose up`

**Note:** if you are using M1 chip, please comment out model3 in the docker-compose.yml file. Because an ARM64 compatible image for this model is not available at the moment.


## How to cite us?
MLExchange paper can be found on ArXiv: [https://doi.org/10.48550/arXiv.2208.09751](https://doi.org/10.48550/arXiv.2208.09751)

**BibTex:**  

    @misc{https://doi.org/10.48550/arxiv.2208.09751,
        doi = {10.48550/ARXIV.2208.09751},
        
        url = {https://arxiv.org/abs/2208.09751},
        
        author = {Zhao, Zhuowen and Chavez, Tanny and Holman, Elizabeth A. and Hao, Guanhua and Green, Adam and Krishnan, Harinarayan and McReynolds, Dylan and Pandolfi, Ronald and Roberts, Eric J. and Zwart, Petrus H. and Yanxon, Howard and Schwarz, Nicholas and Sankaranarayanan, Subramanian and Kalinin, Sergei V. and Mehta, Apurva and Campbell, Stuart and Hexemer, Alexander},
        
        keywords = {Machine Learning (cs.LG), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
        
        title = {MLExchange: A web-based platform enabling exchangeable machine learning workflows for scientific studies},


# Copyright
MLExchange Copyright (c) 2021, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.

If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at IPO@lbl.gov.

NOTICE.  This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights.  As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit others to do so.

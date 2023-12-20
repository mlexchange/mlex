# MLExchange
MLExchange is web-based software infrastructure that deploys machine learning models for beamline scientists.

This is our 1st release. 
It contains 2 MLExchange services, i.e., the job manager and content registry.

Within content registry webpage:  
1. 	One can launch 2 frontend applications under APPs tab, i.e., image segmentation app (seg-demo) and colowheel. Seg-demo contains 3 machine learning models to be used for segmentation, i.e., k-means, random forest, and Mixed-Scale Dense Convolutional Networks (MSDnets).   
2. 	One can launch two workflows under the Workflows tab.

All these container images will be directly pulled from [the MLExchange DockerHub](https://hub.docker.com/u/mlexchange1). 

Please note: the latest version only works on AMD chips.

## How to use?
1. Install [Docker Engine](https://docs.docker.com/engine/install/ubuntu/) on a Linux server or [Docker Desktop](https://www.docker.com/products/docker-desktop/) on a MacOS or Windows machine. 
2. cd into mlex folder, create a `.env` file (make sure there is no white space or special characters in the username or password).

	```
	MONGO_DB_USERNAME=your_username     
	MONGO_DB_PASSWORD=your_password               
 	``` 
3. To install the **lightest** MLExchange platform, run `docker-compose up`. **Note**: use `docker compose up -d` instead to run containers in the detached mode.

4. (Optional) run `docker compose -f docker-model-images.yml pull` to download the colorwheel app, segmentation app and models. 

	**Note:** if you are using M1 chip, please comment out model3 in the docker-	compose.yml file. Because an ARM64 compatible image for this model is not 	available at the moment.

5. To uninstall, run `docker compose down`. 


## How to cite us?
MLExchange paper: [https://ieeexplore.ieee.org/document/10024637](https://ieeexplore.ieee.org/document/10024637)

**BibTex:**  

    @INPROCEEDINGS{10024637,
      author={Zhao, Zhuowen and Chavez, Tanny and Holman, Elizabeth A. and Hao, Guanhua and Green, Adam and Krishnan, Harinarayan and McReynolds, Dylan and Pandolfi, Ronald J. and Roberts, Eric J. and Zwart, Petrus H. and Yanxon, Howard and Schwarz, Nicholas and Sankaranarayanan, Subramanian and Kalinin, Sergei V. and Mehta, Apurva and Campbell, Stuart I. and Hexemer, Alexander},
      booktitle={2022 4th Annual Workshop on Extreme-scale Experiment-in-the-Loop Computing (XLOOP)}, 
      title={MLExchange: A web-based platform enabling exchangeable machine learning workflows for scientific studies}, 
      year={2022},
      volume={},
      number={},
      pages={10-15},
      doi={10.1109/XLOOP56614.2022.00007}} 
 

# Copyright
MLExchange Copyright (c) 2021, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.

If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at IPO@lbl.gov.

NOTICE.  This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights.  As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit others to do so.

# Cloud-Based Energy Monitoring Dashboard with a Simulated Backend

This repository contains the code for the energy monitoring system as described in my proposal. 

## About

This project aims to demonstrate the implmentation of a Cloud-based Energy Monitoring System. The backend is implmented in simulation by a Discrete Event Simulink Model. The model models a workshop executing various machining processes. MQTT protocol is used send the energy consumed by the equipments to cloud. The MQTT message broker lives in AWS IoT Core, the generated time series data is stored in AWS Timestream and the dashboard was built using Grafana. 


## Setups

1. Clone the repository: `https://github.com/Akpamax/Energy_monitor`
2. Add /Energy_Monitoring to MATLAB PATH so that the pyhon scripts and functions are visible to the model. 
3. Configure MATLAB to run python scripts. In MATLAB command window, run

        pyenv(Version = executable) 

    where execcutable is the path your python executable is at. Find this out using the following snippet in python:

        import sys
        executable = sys.executable
    
2. Open `models/Energy_consumption_model_V4` in Simulink (version = R2022b).
3. Run the model.
4. Log into Grafana and navigate to the dashboard.
5. Observe the dashboard.



## Dependencies


1. Additional toolbox: The model uses the random() probability density function. Must install one of the following MATLAB toolboxes:

    - SimBiology
    - Statistics and Machine Learning (used for development)

2. python: The AWS-MATLAB interface logic was implemented in python. Various versions of MATLAB supports different python verion.(check here `https://in.mathworks.com/help/matlab/ref/pyrunfile.html` ). 'Python 3.8.10 - May 3, 2021' used for development. 

3. AWS SDK: Clone `https://github.com/aws/aws-iot-device-sdk-python`  in /python_mqtt_interface into the folder /aws-iot-device-sdk-python. Although this folder exists, all its content was deliberately deleted as it is a fairly large library. Clone the SDK into this folder.  

Navigate to this directory and install using 

        python setup.py install


## Notes

1. The model did not compile without errors in R2023a. Highly recommeded to run with R2022b as specified above. 

2. When the models runs and is stopped midway before completion, on a consecutive run, the following error is     encountered:

        Unable to create file 'out.mat' specified in  'Configuration Parameters' > 'Data Import/Export' > 'Log Dataset data to file'. Possible causes for this include: the specified directory does not exist, the directory or the file are not writable, disk quota is exhausted, the file is used by another simulation, or the specified file is a softlink pointing to a non-existing directory.

 Running the model again fixes this. 

 3. There are two versions of the model in /models folder, V3 and V4. The output in V3 is not published while V4 have publishing capabilities. V4 is also the model used in as the data soure for the dashboard. Recommended to run V3 first to understand how the model works before V4. 

## Usage

## Contribution

## License


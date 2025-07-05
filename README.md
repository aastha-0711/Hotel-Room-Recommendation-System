# Hotel-Room-Recommendation-System-Using-Image-Similarity
## Prerequisites
- Python 3.7 or above
- Python virtual environment

## Libraries to be installed
- pandas
- matplotlib
- PIL
- tensorflow
- urllib
- numpy
- opencv-python
- flask
- pickle

## Steps to run setup code
- Run [downloadImages.py](https://github.com/DayeemParkar/Hotel-Room-Recommendation-System-Using-Image-Similarity/blob/main/downloadImages.py) <br />
Modify the range of the 'for' loop. This will help in pausing and resuming download if needed
- Run [featureExtraction.py](https://github.com/DayeemParkar/Hotel-Room-Recommendation-System-Using-Image-Similarity/blob/main/featureExtraction.py) <br />
If prompted whether to extract features again, enter 'yes'
- To view a summary of the model, run [modelSummary.py](https://github.com/DayeemParkar/Hotel-Room-Recommendation-System-Using-Image-Similarity/blob/main/modelSummary.py)

## Steps to run the web application
- Run [appTester.py](https://github.com/DayeemParkar/Hotel-Room-Recommendation-System-Using-Image-Similarity/blob/main/appTester.py)
- Open any browser
- Open [localhost with port 5000](http://127.0.0.1:5000/login) to view the login page

# Capstone
## Predicting Coffee Ratings from Expert Reviews

This project scrapes review data from CoffeeReview.com using Beautiful Soup. Data is cleaned and compiled. Data includes a mix of evaluative numeric values, descriptive numeric data, evaluative text data, and descriptive text data. Different natural language processing (NLP) methods are applied to the text data to make it useable for machine learning. Different models are tested and evaluated to determine which model is the best fit for predicting the coffee rating. Finally, the final model is explored further to see which features are most important, as well as what other insights can be gained from the model.  

## Built With
* pandas
* requests
* jupyter
* lxml
* matplotlib
* seaborn
* numpy
* scipy
* python=3.8
* beautifulsoup4
* pymysql
* sqlalchemy
* scikit-learn
* statsmodels
* tensorflow==2.7.0
* gensim=3.8.3
* xgboost=1.1.1

## Getting Started
The project spans 7 Jupyter Notebooks:
* Notebook 1: Collecting the Data
* Notebook 2: Cleaning the Data Part 1
* Notebook 3: Cleaning the Data Part 2
* Notebook 4: Compiling the Data and Further Cleaning
* Notebook 5: Baseline EDA and Modeling on Non-Text Data
* Notebook 6: Natural Language Processing 
* Notebook 7: Optimizing Models on All Data

Follow the steps outlined below to get your environment set up to support the project.

### Prerequisites
The following packages will need to be installed to run the notebooks.

channels:
* defaults

dependencies:
* pandas 1.4.4
* requests 2.28.1
* jupyter 1.0.0
* lxml 4.8.0
* matplotlib 3.5.2
* seaborn 0.11.2 
* numpy 0.11.2 
* scipy 1.7.3  
* python 3.8.13
* beautifulsoup4 4.11.1
* pymysql 1.0.2
* sqlalchemy 1.4.39   
* scikit-learn 1.1.2
* statsmodels 0.13.2  
* tensorflow 2.7.0
* gensim 3.8.3
* xgboost 1.1.1
* nltk 3.7

### Installation
Packages can be installed using (referenced file on GitHub): 
  ```sh
conda env create --file coffee_conda_env.yml
  ```

## Use Case
This project can be used to explore web scraping, data cleaning, text vectorization, and machine learning modeling. 

## Contact
Kate Meredith: kmere21@gmail.com
Project Link: https://github.com/KMere21/capstone

## Acknowledgements
* [Coffee Review](https://www.coffeereview.com/)
* [Choose an Open Source License](https://choosealicense.com/)
* [Best READ.ME template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md) 
* [Recreating python environment](https://stackoverflow.com/questions/46375576/get-the-list-of-packages-installed-in-anaconda)
* Additional resources are cited in the individual notebooks in which the resource was used

## License
Distributed under the MIT License. See license.txt for more information.



# Predicting Future Sales
**This is a light version of the project intended for an interview. [Original version here](https://github.com/Druizm128/predicting_sales_1c)**

![](img/logos.png)


## Team
- **Dante Ruiz 183340**, 
- Alejandra Lelo 124433
- Jose Carlos Escobar 175895



## Objective

To predict the total monthly sales by product and store for [1C]( http://1c.ru/eng/title.html), one of the largest software companies in Russia. The purpose of this predictions is to inform business management strategy, marketing strategies and inventory management.


## Tools used

* **Shell scripting**: to download files from the Kaggle API
* **R**: to preprocess, clean and explore data
* **Google Could Translation API**: to translate text from Russian to English
* **Python**: to train and evaluate machine learning models using scikit-learn package.
* **Flask**: to deploy the final model to make monthly sales predictions by product and store.
* **Azure**: to use a Data Science Machine to conduct the entire process

## Files:

1. **Executive summary**: An executive summary of the project in spanish
2. **01_Comprendiendo_Negocio.ipynb**: describes the dataset 
3. **Traduccion.html** : describes the text translation from Russian to English 
4. **02_Comprensión de los Datos en Python.ipynb** : describes the business problem 
5. **03_04_Preparacion_Datos_y_Modelado.ipynb**: presents the exploratory data analysis, and also describes how models were evaluated, the best model selected and how predictions were performed.
6. **05_Evaluacion.ipynb**: presents the machine learning process of evaluation and Kaggle score.
7. **06_Deployment.ipynb**: presents process to deploy model in Flask and Docker 
8. **Traduccion.html**: describes how to translate catalogs from Russian to English
9. **DescargaDatos.sh**: code to download original data

## App: 

* **predictor.py**: web service application in flask to predict monthly sales by product and store for the month of November 2015. The app can be downloaded from Docker Hub under the name of [danteruiz/salespredictor](https://cloud.docker.com/u/danteruiz/repository/docker/danteruiz/salespredictor)

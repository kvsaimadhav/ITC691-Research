Documentation of ITC691 Project by Kaza Venkata Sai Madhav

PART 1: Follow the below steps to change the present working directory to src directory after unzipping the ITC691-Research file.

1. Change your present working directory to ITC691-Research directory.

2. Now, change your present working directory to src directory.

PART 2: Follow the below steps for the working of the covid-19 prediction source files.

1. First, install python and the dataset from the below links.
	Dataset: https://covidtracking.com/data/download
	Python: https://www.python.org/downloads/
 
2. You need to install Jupyter Notebook for source files to be run in your computer.
   Please, follow this link to download jupyter notebook: 
   https://test-jupyter.readthedocs.io/en/latest/install.html

3. Install fbprophet, numpy, pandas, and pickle packages for popping up of no errors in the code. Do not skip this step. 
	As it is important for the files to run properly, we need to install these packages before going into step 7. 

4. Type the command in the command prompt: jupyter notebook 

5. You will see a chrome window opening automatically and go to the ITC691-Research folder and follow steps of part-1.

6. You need to run the commands written in the .ipynb files. There are 5 files which are self descriptive. 
	Tutorial for running commands can be followed in the attached below link:  
	https://www.codecademy.com/articles/how-to-use-jupyter-notebooks

7. Files to look into till Midterm Progress are src folder, week2-statistics-michigan-data.ipynb, week3-prophet-mcihigandata.ipynb, week4-prophet-variable-percent-splitdata.ipynb, week5-saturating-min-prophet.ipynb and webapp_pre-processing.ipynb.

8. You can look at the documentation folder inside the ITC691-Research folder for more details on the results till midterm progress.

PART 3: Follow the below steps for the working of the website covid-19 prediction project files.

1. Now, change the present working directory to project folder which is inside of the src folder.

2. Install Django package for popping up no errors in the code.

3. Type the command in the command prompt:  python3 manage.py migrate

4. Type the command in the command prompt: python3 manage.py runserver

5. Now, open the below link in chrome window to access the website.
	http://127.0.0.1:8000/covid_project/

6. The website will ask you to enter the personal details like First Name and Last Name. After you enter the details, 
	the steps are self-explanatory to come to the final page. 


	
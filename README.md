# PlantPathoDetect
Image classification project for detecting diseases in tomatoes, maize, and potatoes using AI


# PlantPathoDetect
![alt text](Images/main.jpeg)
 

## Table of Contents

1. [Business Understanding](#business-understanding)
   - [Overview](#overview)
   - [Goal](#goal)
   - [Objectives](#objectives)
   - [Stakeholders](#stakeholders)

2. [Data Understanding](#data-understanding)

3. [Data Preparation](#data-preparation)

4. [Modeling](#modeling)

5. [Conclusion](#conclusion)

6. [Recommendations](#recommendations)

7. [Next Steps](#next-steps)

8. [Deployment](#deployment)
   - [Installation](#installation)

9. [Libraries and Tools Used](#libraries-and-tools-used)

10. [License](#license)

11. [Contributing Members](#contributing-members)

12. [Contacts](#contacts)

13. [Repository Structure](#repository-structure)

## Business Understanding

**Overview**
Agriculture is crucial for food security and economic stability, yet essential crops like maize, potatoes, and tomatoes face rising threats from diseases that significantly reduce yields and impact farmers' livelihoods. In regions reliant on these crops, such challenges lead to economic strain, increased pesticide use, and food shortages, affecting entire communities. This project aims to address these issues by developing a machine learning-powered image classification system for early disease detection. By enabling farmers to upload crop images to a web-based platform for real-time analysis and treatment recommendations, the solution empowers them with vital insights, helping to protect yields and sustain food production.
 

**Goal**

To develop a web-based application that facilitates early detection and prediction of crop diseases in maize, potatoes, and tomatoes using machine learning-based image classification.
**Objectives**

1. **Data Collection and Preprocessing**: To collect and preprocess a diverse dataset of images capturing common diseases affecting maize, potatoes, and tomatoes.
2. **Model Development**: To design and train a convolutional neural network (CNN) for accurate image classification of crop diseases.
3. **Application Deployment**: To implement the trained model within a user-friendly web application where farmers can upload images for disease diagnosis.
4. **System Evaluation and Feedback**: To assess the model’s performance, gather user feedback, and iteratively refine the application for practical use by local farmers.

## Stakeholders
1. Farmers: Smallholder and commercial farmers, particularly in regions where crop diseases like those affecting maize, potatoes, and tomatoes are prevalent. They are the end-users who will directly benefit from the disease detection tool.

2. Agricultural Extension Officers: Professionals who work closely with farmers, providing advice and support in crop management. They may use this tool to assist farmers in disease identification and treatment recommendations.

3. Agricultural Research Institutions: Organizations focused on agricultural technology and innovation. They may be interested in the data, findings, and outcomes to support further research on crop diseases and digital agricultural solutions.

4. Government and Policymakers: Officials responsible for food security and agricultural productivity initiatives. They might use insights from the project to shape policies and support digital innovations that aid farmers.

5. Technology and Data Science Professionals: Individuals or teams involved in the development, maintenance, and improvement of the machine learning model and web application.

6. Non-Governmental Organizations (NGOs): Organizations that work with smallholder farmers to improve food security and promote sustainable farming practices could also benefit from the tool by integrating it into their support programs.
## Data Understanding
The dataset used in this project is sourced from PlantVillage and comprises 70,000 high-quality images of both healthy and diseased plant leaves from nine distinct species. This dataset is meticulously organized into three splits—train, test, and validation—ensuring consistent categories across each split. It offers an excellent foundation for machine learning research and applications in plant disease detection and classification.

Ideal for both agricultural experts and machine learning practitioners, this diverse dataset captures a broad range of plant species, disease types, and growth stages. By leveraging this dataset, the project aims to advance research in plant pathology and support farmers in enhancing crop health and productivity, ultimately contributing to more sustainable agricultural practices.

Link to The Plant Village Website [Plant Village](https://plantvillage.psu.edu/)
 
## Data Preparation

The data processing step involved analyzing and cleaning a merged dataset of tweets related to the 2024 Paris Olympics originally composed of multiple CSV files. A DataUnderstanding class was created to examine the dataset revealing missing values and discrepancies as well as a large number of apparent duplicates most of which were false positives due to partial similarities.
## Visualizations
 
 
 
 ## Modeling
  
 

## Conclusion

 
## Recommendations

 

## Next steps
 

### Deployment
 
### Installation 
To run the application locally, follow the following steps:

**Clone the repository**

**https:**
```
git clone https://github.com/KAREN154/PlantPathoDetect.git
```
**ssh:**
```
git clone git@github.com:KAREN154/KAREN154/PlantPathoDetect.git
```
**Navigate to the project directory**

```
cd PlantPathoDetect.git
```
**Create a virtual environment**

```
 python -m venv patho-p

```
**Activate the virtual environment**

**Windows:**
```
patho-p\Scripts\activate
```
**MacOS/Linux:**
```
source patho-p/bin/activate
```
**Install dependencies**
```
pip install -r requirements.txt
```
 

## 🔗 Libraries and Tools Used
![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![tensorflow](https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=blue)
![keras](https://img.shields.io/badge/keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![nltk](https://img.shields.io/badge/NLTK-154f3c?style=for-the-badge&logo=python&logoColor=white)
![streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=pink)
![vadersentiment](https://img.shields.io/badge/vaderSentiment-7D4698?style=for-the-badge&logo=python&logoColor=white)
![scikitlearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)


## License
MIT License

 
## Contacts
- karenmercy49@gmail.com

Kindly don't hesitate to reach out if you have any questions.

## Repository Structure

```
PlantPathoDetect/
│
└── Project Files/
    ├── Csv Files
    ├── Images
    ├── Models
    ├── Notebooks
    ├── the_team
    ├──  
    ├── .gitattributes
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├──  
    ├── requirements.txt
    ├──  
    └──  
      
```




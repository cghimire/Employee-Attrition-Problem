# Employee Attrition Problem
## Table of Content
  * [Overview](#overview)
  * [Data Preparation and Exploration](#data-preparation-and-exploration)
  * [Data Modeling](#data-modeling)
  * [Important Features for Employee Turnover](#important-features-for-employee-turnover)

## Overview

I am exploring the employee dataset to solve following research questions: 
* Why employee are prone to leave?
* What type of employee are prone to leave the company?
* Predict the future employee who would tend to leave the company.

## Data Preparation and Exploration

![alt text](https://github.com/cghimire/Employee-Attrition-Problem/blob/master/df_existing-histogram.png " Current employee Histogram")

  #### *Histogram of Current Employee*
  
  ![Alt Text](https://github.com/cghimire/Employee-Attrition-Problem/blob/master/df_nonexisting_histogram_plots.png " ex-employee Histogram")
  #### *Histogram of ex-employee*
  
  A few observations can be made based on the information and histograms for numerical features. Many histograms are tail-heavy; indeed several distributions are right-skewed (e.g.time_spend_company, promotion_last_5years). Data transformation methods may be required to approach a normal distribution prior to fitting a model to the data.
  
## Data Modeling

I use a range of baseline algorithms before we move on to more sophisticated solutions. The algorithms considered in this section are: Logistic Regression, Random Forest, and, SVM.

## Important Features for Employee Turnover
Since this is my real project during my internship, I don't mention the exact result here, but I outlined some inportant features to predict the employee turnover. 
Based on ROC graph, the logistic regression showed higher AUC score compared to rendom forest.

As a concluded remark, as the company generates more data on its employees (on New Joiners and recent Leavers) the algorithm can be re-trained using the additional data and theoritically generate more accurate predictions to identify high-risk employees of leaving based on the probabilistic label assigned to each feature variable (i.e. employee) by the algorithm.

Employees can be assigning a "Risk Category" based on the predicted label such that:

* **Low-risk** for employees with label < 0.6
* **Medium-risk** for employees with label between 0.6 and 0.8
* **High-risk** for employees with label > 0.8

**A strategic "Retention Plan"** should be drawn for each Risk Category group. The face-to-face meetings between a HR representative and employees can be initiated for medium- and high-risk employees to discuss work conditions. Also, a meeting with those employee's Line Manager would allow to discuss the work environment within the team and whether steps can be taken to improve it.

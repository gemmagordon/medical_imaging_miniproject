
import pandas as pd 
import numpy as np 
import shutil, os

train_labels_df = pd.read_csv('train_labels.csv')

# split into cancer and noncancer
noncancer = train_labels_df.loc[train_labels_df['label'] == 0]
cancer = train_labels_df.loc[train_labels_df['label'] == 1]


# randomly divide noncancer set into training, validation and test
train_noncancer, validate_noncancer, test_noncancer = np.split(noncancer.sample(frac=1), [int(.6*len(noncancer)), int(.8*len(noncancer))])

print(len(train_noncancer))
print(len(test_noncancer))
print(len(validate_noncancer))

train_noncancer_f = train_noncancer.sample(6000)
test_noncancer_f = test_noncancer.sample(2000)
validate_noncancer_f = validate_noncancer.sample(2000)

print(len(train_noncancer_f))
print(len(test_noncancer_f))
print(len(validate_noncancer_f))

# randomly divide cancer set into training, validation and test
train_cancer, validate_cancer, test_cancer = np.split(cancer.sample(frac=1), [int(.6*len(cancer)), int(.8*len(cancer))])

print(len(train_cancer))
print(len(test_cancer))
print(len(validate_cancer))

train_cancer_f = train_cancer.sample(6000)
test_cancer_f = test_cancer.sample(2000)
validate_cancer_f = validate_cancer.sample(2000)

print(len(train_cancer_f))
print(len(test_cancer_f))
print(len(validate_cancer_f))


# create new dirs of images with ids corresponding to the df of train, validate, test lists
folders = ['train_noncancer', 'validate_noncancer', 'test_noncancer', 'train_cancer', 'validate_cancer', 'test_cancer']
dataframes = [train_noncancer_f, validate_noncancer_f, test_noncancer_f, train_cancer_f, validate_cancer_f, test_cancer_f]

for df, folder in zip(dataframes, folders):
    os.mkdir(folder)
    for entry in df['id']:
        entry_file_path = str('/Users/gemmagordon/Documents/OXFORD/MEDICAL_IMAGING/medical_imaging_miniproject/histopathologic-cancer-detection/train/' + entry + '.tif')
        shutil.copy(entry_file_path, folder)

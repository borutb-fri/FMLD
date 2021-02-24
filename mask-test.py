#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:57:43 2020
@author: borut batagelj
"""

import os

import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
from torch import nn

# Applying Transforms to the Data
image_transforms = { 
    'test': transforms.Compose([
        transforms.Resize(size=(224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])
}

# Load the Data
dataset = 'faces'
test_directory = os.path.join(dataset, 'test')

# Batch size
bs = 128

# Number of classes
num_classes = 2

# Load Data from folders
data = {
    'test': datasets.ImageFolder(root=test_directory, transform=image_transforms['test']),
}

class_names = data['test'].classes
transform=image_transforms['test']


# Get a mapping of the indices to the class names, in order to see the output classes of the test images.
idx_to_class = {v: k for k, v in data['test'].class_to_idx.items()}
print(idx_to_class)

# Size of Data, to be used for calculating Average Loss and Accuracy
test_data_size = len(data['test'])

# Create iterators for the Data loaded using DataLoader module
test_data_loader = DataLoader(data['test'], batch_size=bs, shuffle=False)

# Print the test set data sizes
print(test_data_size)

def computeTestSetAccuracy(model, loss_criterion, data_loader, data_size):
    '''
    Function to compute the accuracy on the test set
    Parameters
        :param model: Model to test
        :param loss_criterion: Loss Criterion to minimize
    '''

    test_acc = 0.0
    test_loss = 0.0

    # Validation - No gradient tracking needed
    with torch.no_grad():
        # Set to evaluation mode
        model.eval()

        # Validation loop
        for j, (inputs, labels) in enumerate(data_loader):
            inputs = inputs.to(device)
            labels = labels.to(device)

            # Forward pass - compute outputs on input data using the model
            outputs = model(inputs)

            # Compute loss
            #loss = loss_criterion(outputs, labels)

            # Compute the total loss for the batch and add it to valid_loss
            #test_loss += loss.item() * inputs.size(0)

            # Calculate validation accuracy
            ret, predictions = torch.max(outputs.data, 1)
            correct_counts = predictions.eq(labels.data.view_as(predictions))

            # Convert correct_counts to float and then compute the mean
            acc = torch.mean(correct_counts.type(torch.FloatTensor))

            # Compute total accuracy in the whole batch and add to valid_acc
            test_acc += acc.item() * inputs.size(0)

            
    # Find average test loss and test accuracy
    #avg_test_loss = test_loss/data_size
    avg_test_acc = test_acc/data_size
    return avg_test_acc



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
loss_func = nn.CrossEntropyLoss() #for a multi-class classification problem 
  
model_file = 'resnet152.pt'
if os.path.exists(model_file):    
    model = torch.load(model_file)
    model = model.to(device)
    avg_test_acc=computeTestSetAccuracy(model, loss_func, test_data_loader, test_data_size)
    print("Test accuracy : " + str(avg_test_acc))
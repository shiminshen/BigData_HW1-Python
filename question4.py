from loadFile import loadTaxiData
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# load taxi data
tData = loadTaxiData()
# get neccesary data
subData = tData[['trip_distance', 'tip_amount']]

# Fit line using all data
model = linear_model.LinearRegression()
model.fit(subData[['trip_distance']], subData[['tip_amount']])

# Robustly fit linear model with RANSAC algorithm
model_ransac = linear_model.RANSACRegressor(linear_model.LinearRegression())
model_ransac.fit(subData[['trip_distance']], subData[['tip_amount']])
inlier_mask = model_ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)

# Predict data of estimated models
line_X = np.arange(-5, 50)
line_y = model.predict(line_X[:, np.newaxis])
line_y_ransac = model_ransac.predict(line_X[:, np.newaxis])

# Compare estimated coefficients
print("Estimated coefficients (normal, RANSAC):")
print(model.coef_, model_ransac.estimator_.coef_)

plt.plot(subData[['trip_distance']][inlier_mask], subData[['tip_amount']][inlier_mask], '.g', label='Inliers')
plt.plot(subData[['trip_distance']][outlier_mask], subData[['tip_amount']][outlier_mask], '.r', label='Outliers')
plt.plot(line_X, line_y, '-k', label='Linear regressor')
plt.plot(line_X, line_y_ransac, '-b', label='RANSAC regressor')
plt.legend(loc='lower right')
plt.show()

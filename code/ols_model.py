import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

#load data
data = pd.read_csv("../data/training_data.csv")
training = data['time'].values
y_train = data['price'].values

testing_data = pd.read_csv("../data/testing_data.csv")
testing = testing_data['time'].values
y_test = testing_data['price'].values

x_training = sm.add_constant(training)

#ols model
ols_model = sm.OLS(y_train, x_training).fit()
print(ols_model.summary())

#save model
ols_model.save("./currentOlsSolution.xml")

#predictions
x_testing = sm.add_constant(testing)
y_pred = ols_model.predict(x_testing)

print(f"Mean squared error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"Coefficient of determination: {r2_score(y_test, y_pred):.2f}")

#scatterplot
plt.scatter(training, y_train, color='orange', label='Training Data', alpha=0.7)
plt.scatter(testing, y_test, color='blue', label='Testing Data')

fig = sm.graphics.abline_plot(model_results=ols_model, color='red', label="OLS regression", ax=plt.gca())

plt.xlabel('Time')
plt.ylabel('Price')
plt.title('OLS Regression Fit')
plt.legend()
#plt.show()
plt.tight_layout()
plt.savefig('scatterplot.pdf')

#diagnostics
import diagnostics_plots as dp
cls = dp.Linear_Reg_Diagnostic(ols_model)
cls(plot_context="seaborn-v0_8-paper")

cls.residual_plot()
plt.savefig('residual_plot.png', dpi=300, bbox_inches='tight')
plt.close()

cls.qq_plot()
plt.savefig('qq_plot.png', dpi=300, bbox_inches='tight')
plt.close()

cls.scale_location_plot()
plt.savefig('scale_location_plot.png', dpi=300, bbox_inches='tight')
plt.close()

cls.leverage_plot()
plt.savefig('leverage_plot.png', dpi=300, bbox_inches='tight')
plt.close()
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import diagnostics_plots as dp
from sklearn.metrics import mean_squared_error, r2_score

#load data
data = pd.read_csv("../data/training_data.csv")
training_value_x = data[['time', 'price_lag']].values
training_value_y = data['target_price'].values

testing_data = pd.read_csv("../data/testing_data.csv")
testing_value_x = testing_data[['time', 'price_lag']].values
testing_value_y = testing_data['target_price'].values

x_training = sm.add_constant(training_value_x)

#ols model
ols_model = sm.OLS(training_value_y, x_training).fit()
print(ols_model.summary())

#save model
ols_model.save("../images/knowledgeBase_energy_prediction/currentOlsSolution.xml")

#predictions
x_testing = sm.add_constant(testing_value_x)
y_pred = ols_model.predict(x_testing)

print(f"Mean squared error: {mean_squared_error(testing_value_y, y_pred):.2f}")
print(f"Coefficient of determination: {r2_score(testing_value_y, y_pred):.2f}")

#scatterplot
plt.figure(figsize=(14,5))
plt.scatter(training_value_x[:, 0], training_value_y, color='orange', label='Training Data', alpha=0.7)
plt.scatter(testing_value_x[:, 0], testing_value_y, color='blue', label='Testing Data')

plt.plot(testing_value_x[:, 0], y_pred, color='red', label='OLS Prediction Trend', linewidth=2)

plt.xlabel('Time')
plt.ylabel('Price')
plt.title('OLS Regression Fit')
plt.legend()
plt.tight_layout()
plt.savefig('scatterplot-time.png')

#scatterplot
plt.figure(figsize=(14,5))
plt.scatter(training_value_x[:, 1], training_value_y, color='orange', label='Training Data', alpha=0.7)
plt.scatter(testing_value_x[:, 1], testing_value_y, color='blue', label='Testing Data')

#fig = sm.graphics.abline_plot(model_results=ols_model, color='red', label="OLS regression", ax=plt.gca())
plt.plot(testing_value_x[:, 1], y_pred, color='red', label='OLS Prediction Trend', linewidth=2)

plt.xlabel('Price Lag')
plt.ylabel('Price')
plt.title('OLS Regression Fit')
plt.legend()
#plt.show()
plt.tight_layout()
plt.savefig('scatterplot-lag.png')

#diagnostics
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
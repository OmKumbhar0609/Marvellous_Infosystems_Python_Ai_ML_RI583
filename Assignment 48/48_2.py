# Calculate MSE and R² Score

X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

num = sum((X[i]-mean_x)*(Y[i]-mean_y) for i in range(len(X)))
den = sum((X[i]-mean_x)**2 for i in range(len(X)))

m = num / den
c = mean_y - m * mean_x

Y_pred = []

for x in X:
    Y_pred.append(m*x + c)

print("Predicted Values:", Y_pred)

mse = sum((Y[i]-Y_pred[i])**2 for i in range(len(Y))) / len(Y)

ss_total = sum((y-mean_y)**2 for y in Y)
ss_res = sum((Y[i]-Y_pred[i])**2 for i in range(len(Y)))

r2 = 1 - (ss_res/ss_total)

print("MSE =", round(mse,4))
print("R2 Score =", round(r2,4))
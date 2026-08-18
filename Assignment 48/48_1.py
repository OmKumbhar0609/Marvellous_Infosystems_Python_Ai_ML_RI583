# Simple Linear Regression Manually (Without ML Library)

X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

n = len(X)

mean_x = sum(X) / n
mean_y = sum(Y) / n

num = 0
den = 0

for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

m = num / den
c = mean_y - (m * mean_x)

print("Mean of X =", mean_x)
print("Mean of Y =", mean_y)
print("Slope (m) =", round(m, 2))
print("Intercept (c) =", round(c, 2))

print("\nRegression Equation:")
print(f"Y = {round(m,2)}X + {round(c,2)}")

x_new = 6
y_pred = m * x_new + c

print("\nPredicted Y for X = 6 :", round(y_pred, 2))

# Write a Python program using StandardScaler to perform feature scaling

from sklearn.preprocessing import StandardScaler

data = [
    [25, 20000],
    [30, 40000],
    [35, 80000]
]

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print("Scaled Dataset:")
print(scaled_data)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

iris = load_iris()
X = iris.data
y = iris.target

print("=" * 55)
print("  Project 2: Data Classification Using AI")
print("=" * 55)

print("\n-- Dataset Overview --")
print(f"  Total samples  : {X.shape[0]}")
print(f"  Features       : {X.shape[1]}")
print(f"  Classes        : {iris.target_names.tolist()}")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n-- Feature Scaling Applied (StandardScaler) --")
print("  Raw data normalized: mean=0, variance=1")

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, shuffle=True, random_state=42
)

print("\n-- Train/Test Split --")
print(f"  Training samples : {len(X_train)} (80%)")
print(f"  Testing samples  : {len(X_test)}  (20%)")

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

print("\n-- Model Training Complete --")
print("  Algorithm : K-Nearest Neighbors")
print("  K value   : 5")

predictions = model.predict(X_test)

print("\n-- Confusion Matrix --")
cm = confusion_matrix(y_test, predictions)
print(f"  {cm[0]}  <- Setosa")
print(f"  {cm[1]}  <- Versicolor")
print(f"  {cm[2]}  <- Virginica")
print("  [Setosa | Versicolor | Virginica] (predicted)")

print("\n-- Classification Report --")
print(classification_report(y_test, predictions, target_names=iris.target_names))

print("-- Single Prediction Example --")
sample = [[5.1, 3.5, 1.4, 0.2]]
sample_scaled = scaler.transform(sample)
result = model.predict(sample_scaled)
print(f"  Input    : sepal=5.1cm x 3.5cm | petal=1.4cm x 0.2cm")
print(f"  Predicted: {iris.target_names[result[0]]}")
print("\n" + "=" * 55)
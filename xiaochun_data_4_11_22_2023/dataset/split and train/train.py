from sklearn import svm
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib



# Load your training dataset
train_dataset_path = 'train_dataset_audio_only.csv'  # Update with your actual path
train_dataset = pd.read_csv(train_dataset_path)

# Load your testing dataset
test_dataset_path = 'test_dataset_audio_only.csv'  # Update with your actual path
test_dataset = pd.read_csv(test_dataset_path)

# Extract features (X) and labels (y) from the training dataset
exclude_columns = ['ID', 'label', 'name']
features_columns = [col for col in train_dataset.columns if col not in exclude_columns]

X_train = train_dataset[features_columns]  # Features
y_train = train_dataset['label']  # Labels

# Extract features (X) and labels (y) from the testing dataset
X_test = test_dataset[features_columns]  # Features
y_test = test_dataset['label']  # Labels

# Initialize the SVM model
svm_model = svm.SVC()

# Train the SVM model
svm_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm_model.predict(X_test)

# Calculate accuracy on the test set
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on the test set: {accuracy}")

# Save the trained SVM model to a file
joblib.dump(svm_model, 'svm_model_audio_only.joblib')

# -*- coding: utf-8 -*-
"""Submission 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S_FWmXmy4QRVtgw7xI1KHF55dbAmSkXm

#Import Library
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

"""#Load Data"""

df = pd.read_csv("https://raw.githubusercontent.com/mufidatuln/Laporan-Proyek-Machine-Learning-1/main/dataset/Medicaldataset.csv")
df.head()

"""#EDA"""

df.info()

"""Terdapat 9 Kolom dengan 5 kolom bertipe data integer, 3 kolom bertipe data float dan satu fitur target bertipe data object"""

df.describe()

"""Kita bisa melihat persebaran data secara umum pada setiap kolom

##Cleaning Data Null
"""

df.isnull().sum()

"""Pada Dataset ini tidak ditemukan nilai null

##Cleaning Data Duplikat
"""

df.duplicated().sum()

"""Tidak terdapat data duplikat dalam dataset

#Univeariate Analisis
"""

categorical_features= ['Result','Gender']

"""###Perserbaran Jumlah Diagnosis Berdasarkan Gender"""

# Membuat tabel silang
cross_tab = pd.crosstab(df["Gender"], df["Result"])

# Membuat subplot
fig, ax = plt.subplots(figsize=(8, 6))

# Melakukan visualisasi bar plot untuk tabel silang "Gender" vs "Result"
cross_tab.plot(kind="bar", ax=ax)
ax.set_title("Jumlah Hasil Diagnosis Pasien berdasarkan Gender")
ax.set_xlabel("Gender")
ax.set_ylabel("Count")
ax.legend(title="Result")
ax.set_xticklabels(['Laki-laki', 'Perempuan'], rotation=0)
for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()
plt.show()

df.groupby("Age").agg({
    "Result": lambda x: (x == "positif").count()
})

# Buat DataFrame contoh
# df = pd.DataFrame({'umur': [10, 25, 40, 60, 80]})

# Tentukan batas-batas untuk segmentasi umur
bins = [0, 12, 21, 60, 100]
labels = ['Anak-Anak', 'Remaja', 'Dewasa', 'Tua']

# Gunakan pd.cut untuk membuat kolom baru dengan kategori umur
df['segment_umur'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
df

"""Menambahkan satu fitur dengan nama segment_umur untuk mengkategorikan umur"""

segmentasi_umur = df.groupby("segment_umur").agg({
    "Result": lambda x: (x == "positif").count()
})

segmentasi = pd.DataFrame(segmentasi_umur).reset_index()
segmentasi

"""##Jumlah Pasien Positif Memiliki Penyakit Jantung Berdasarkan Segmentasi Umur"""

# Buat bar chart
plt.bar(segmentasi['segment_umur'], segmentasi['Result'])

# Tambahkan label dan judul
plt.xlabel('Segmentasi Umur')
plt.ylabel('Jumlah')
plt.title('Jumlah Pasien Positif Memiliki Penyakit Jantung Berdasarkan Segmentasi Umur')

# Tampilkan bar chart
plt.show()

numerical_features = ['Age','Heart rate','Systolic blood pressure','Diastolic blood pressure','Blood sugar','CK-MB','Troponin']

plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_features, 1):
    plt.subplot(4, 3, i)
    sns.histplot(df[col], bins=20, kde=True)
    plt.title(f'Distribusi Data {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

"""Usia: Distribusi usia tampak miring ke kanan, dengan lebih banyak orang dalam kelompok usia yang lebih tua. Denyut jantung, tekanan darah sistolik, tekanan darah diastolik: Distribusi faktor-faktor ini juga tampak miring ke kanan. Gula darah: Distribusi gula darah tampaknya relatif normal.

#Multivariate Analisis

Scatterplot untuk melihat persebaran data antara 2 fitur atau lebih
"""

data = df
# Scatter plot: Age vs. Heart rate
sns.scatterplot(x='Age', y='Heart rate', data=data)
plt.title('Scatter Plot: Usia vs. Detak Jantung ')
plt.xlabel('Usia')
plt.ylabel('Detak Jantung')
plt.show()

# Scatter plot: Systolic blood pressure vs. Diastolic blood pressure
sns.scatterplot(x='Systolic blood pressure', y='Diastolic blood pressure', data=data)
plt.title('Scatter Plot: Systolic blood pressure vs. Diastolic blood pressure')
plt.xlabel('Systolic blood pressure')
plt.ylabel('Diastolic blood pressure')
plt.show()



# Scatter plot: Age vs. Blood sugar
data = df
sns.scatterplot(x='Age', y='Blood sugar', data=data)
plt.title('Persebaran Data: Usia dan Gula Darah')
plt.xlabel('Usia')
plt.ylabel('Gula Darah')
plt.show()

"""Terdapat korelasi positif yang lemah antara usia dan gula darah. Ini berarti bahwa dengan bertambahnya usia, gula darah juga cenderung meningkat. Namun, korelasinya lemah, sehingga ada banyak variabilitas dalam data."""

# Scatter plot: CK-MB vs. Troponin
sns.scatterplot(x='CK-MB', y='Troponin', data=data)
plt.title('CK-MB vs. Troponin')
plt.xlabel('CK-MB')
plt.ylabel('Troponin')
plt.show()

"""Terdapat korelasi positif yang lemah antara kadar CK-MB dan kadar troponin. Ini berarti bahwa dengan meningkatnya kadar CK-MB, kadar troponin juga cenderung meningkat, tetapi korelasinya lemah.

##Data Preprosessing

Pada tahap ini dilakukan data preprosessing dengan split dataset dan melakukan standarisasi data
"""

#Copy the DataFrame for preprocessing
df_preprocessed = df.copy()
df_preprocessed = df_preprocessed.drop('segment_umur',axis=1)

# Encode categorical variables
label_encoder = LabelEncoder()
df_preprocessed['Result'] = label_encoder.fit_transform(df_preprocessed['Result'])

# Split the data into training and test sets
X = df_preprocessed.drop('Result', axis=1)
y = df_preprocessed['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize or standardize numerical attributes
scaler = StandardScaler()
numerical_cols = ['Age', 'Gender', 'Heart rate', 'Systolic blood pressure', 'Diastolic blood pressure', 'Blood sugar', 'CK-MB', 'Troponin']
X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

# Display the first few rows of the processed training data
X_train.head()

data = df_preprocessed.corr()

plt.figure(figsize=(15, 9))  # Optional: Adjust figure size
sns.heatmap(data, annot=True, cmap='ocean', linewidths=2, fmt=".2f", annot_kws={"size": 10})

# Add labels and title (customize as needed)
plt.title("Coorelation Antar Fitur")

# Show the plot
plt.show()

data = df_preprocessed[['Age','Troponin','CK-MB','Result']].corr()

plt.figure(figsize=(15, 9))  # Optional: Adjust figure size
sns.heatmap(data, annot=True, cmap='ocean', linewidths=2, fmt=".2f", annot_kws={"size": 10})

# Add labels and title (customize as needed)
plt.title("Coorelation Graph")

# Show the plot
plt.show()

"""#Model dan Evaluasi

##Logistic Regression
"""

#Initialize models
log_reg = LogisticRegression(max_iter=1000)
rf = RandomForestClassifier(n_estimators=100)
xgb_clf = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

"""##Random Forest"""

# Train and evaluate each model
log_reg.fit(X_train, y_train)
y_pred_log_reg = log_reg.predict(X_test)
y_proba_log_reg = log_reg.predict_proba(X_test)[:, 1]
log_reg_scores = {
    'Model': 'Random Forest',
    'Accuracy': accuracy_score(y_test, y_pred_log_reg),
    'Precision': precision_score(y_test, y_pred_log_reg),
    'Recall': recall_score(y_test, y_pred_log_reg),
    'F1-Score': f1_score(y_test, y_pred_log_reg),
    'AUC-ROC': roc_auc_score(y_test, y_proba_log_reg)
}
log_reg_df = pd.DataFrame([log_reg_scores])
log_reg_df

"""##XGBClassifier"""

# Train and evaluate each model
xgb_clf.fit(X_train, y_train)
y_pred_xgb_clf = xgb_clf.predict(X_test)
y_proba_xgb_clf = xgb_clf.predict_proba(X_test)[:, 1]
xgb_clf_scores = {
    'Model': 'XGBClassifier',
    'Accuracy': accuracy_score(y_test, y_pred_xgb_clf),
    'Precision': precision_score(y_test, y_pred_xgb_clf),
    'Recall': recall_score(y_test, y_pred_xgb_clf),
    'F1-Score': f1_score(y_test, y_pred_xgb_clf),
    'AUC-ROC': roc_auc_score(y_test, y_proba_xgb_clf)
}
xgb_clf_df = pd.DataFrame([xgb_clf_scores])
xgb_clf_df
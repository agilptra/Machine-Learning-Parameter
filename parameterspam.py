import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


data = {
    'email': ['Tanggal 27 praktikum diliburkan.',
              'Menangkan hadiah besar sekarang!',
              'Batas Waktu pengumpulan.',
              'Promo spesial untuk Anda!',
              'Tugas baru praktikum.'],
    'label': [0, 1, 0, 1, 0]  # 0: Normal, 1: Spam
}


emails = np.array(data['email'])
labels = np.array(data['label'])

X_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vectorized, y_train)


y_pred = model.predict(X_test_vectorized)

new_email = ['Promo sepesial untuk anda!']
new_email_vectorized = vectorizer.transform(new_email)
prediction = model.predict(new_email_vectorized)

if prediction[0] == 0:
    print('Email ini tidak masuk kategori spam.')
else:
    print('Email ini masuk kategori spam.')
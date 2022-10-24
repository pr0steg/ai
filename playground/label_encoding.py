import numpy as np
from sklearn import preprocessing


# Надання міток вхідних даних
input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']

# Створення кодувальника та встановлення відповідності
# між числа і мітками
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

print("\nLabel maping:")
for i, item in enumerate(encoder.classes_):
    print(item, '-->', i)

# test_labels = ['green', 'red', 'black']
# encoded_values = encoder.transform(test_labels)
# print(test_labels)
# print(encoded_values)
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print(encoded_values)
print(decoded_list)
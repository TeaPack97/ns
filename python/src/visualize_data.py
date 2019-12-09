import matplotlib.pyplot as plt
from src.import_data import get_all_data

images, age_labels, gender_labels = get_all_data()

plt.hist(age_labels)
plt.title('Age analysis')
plt.ylabel('Count')
plt.xlabel('Age')
plt.show()
plt.savefig('age_analysis.png')
plt.clf()

plt.hist(gender_labels)
plt.title('Gender analysis')
plt.ylabel('Count')
plt.xlabel('Gender')
plt.show()
plt.savefig('gender_analysis.png')
plt.clf()

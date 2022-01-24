from sklearn import svm, metrics
from joblib import dump, load
# from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import numpy as np
import cv2

data_path = "data/mnist/"
classifier_path = "data/classifier/test.joblib"

try:
    svm_classifier = load(classifier_path)
    print("found svm_classifier file")
    print("loaded svm_classifier.joblib")
except:
    print("found no classifier file")
    train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
    test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")

    fac = 0.99 / 255
    train_imgs = np.asfarray(train_data[:, 1:]) * fac  # + 0.01
    test_imgs = np.asfarray(test_data[:, 1:]) * fac  # + 0.01

    train_labels = np.asfarray(train_data[:, :1]).ravel()
    test_labels = np.asfarray(test_data[:, :1]).ravel()

    svm_classifier = svm.SVC(gamma=0.001)
    svm_classifier.fit(train_imgs, train_labels)

    print("classifier trained")
    dump(svm_classifier, classifier_path)
    print("classifier saved")

    predicted = svm_classifier.predict(test_imgs)
    _, axes = plt.subplots(2, 4)
    print("\nClassification report for classifier %s:\n%s\n" %
          (svm_classifier, metrics.classification_report(test_labels, predicted)))
    disp = metrics.plot_confusion_matrix(
        svm_classifier, test_imgs, test_labels)
    disp.figure_.suptitle("Confusion Matrix")
    print("\nConfusion matrix:\n%s" % disp.confusion_matrix)
    print("\nAccuracy of the Algorithm: ",
          svm_classifier.score(test_imgs, test_labels))
    plt.show()
for i in range(10):
    img_path = 'detection_test/picture_tests/' + str(i) + '.jpg'
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dim = (28, 28)
    small2 = cv2.resize(gray, dim, interpolation=cv2.INTER_AREA)
    small = np.asarray(small2)
    print(small)
    print(small.shape)
    cv2.imshow('orig', image)
    cv2.imshow('gray', gray)
    cv2.imshow('small', small)
    cv2.waitKey(0)
    print(svm_classifier.predict(small))

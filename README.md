# TBCNN-for-C-language-processing
Tree-based Convolutional Neural Networks

["Convolutional Neural Networks over Tree Structures for Programming Language Processing" Lili Mou, et al.](https://arxiv.org/pdf/1409.5718.pdf)

### Implement Tbcnn on C-Language Data Set

#### Requirements

```
tensorflow-gpu>=1.1.0rc1
scikit-learn
scipy
MySQL-python
sshtunnel
scrapy
pickle
pycparser
```

Remark: C language source code with no comment is recommended since pycparser might give an error when dealing with commented data.

#### Results(for reference only):

Training Data Set

```
Computing training accuracy...
('Accuracy:', 0.9656241194702733)
              precision    recall  f1-score   support

          10       0.96      0.95      0.96       371
           1       0.97      0.98      0.98       348
           3       0.99      0.96      0.98       377
           2       0.98      1.00      0.99       357
           5       0.99      0.99      0.99       350
           4       0.97      0.90      0.94       346
           7       0.99      0.98      0.98       347
           6       0.91      0.93      0.92       356
           9       0.98      0.98      0.98       352
           8       0.91      0.99      0.95       345

   micro avg       0.97      0.97      0.97      3549
   macro avg       0.97      0.97      0.97      3549
weighted avg       0.97      0.97      0.97      3549

[[353   2   0   0   0   2   1   1   4   8]
 [  2 341   0   1   0   1   0   2   0   1]
 [  1   0 363   0   2   1   1   1   0   8]
 [  0   0   0 356   0   0   0   0   1   0]
 [  0   1   2   1 346   0   0   0   0   0]
 [  1   1   0   0   0 312   0  26   1   5]
 [  2   0   0   1   0   0 340   0   1   3]
 [  4   4   1   2   0   4   2 331   0   8]
 [  4   0   0   3   0   0   0   0 344   1]
 [  0   1   0   1   0   0   0   1   1 341]]
```

Test Data Set

```
('Accuracy:', 0.9517574086836664)
              precision    recall  f1-score   support

          10       0.89      0.91      0.90       129
           1       0.98      0.96      0.97       152
           3       0.98      0.99      0.98       123
           2       0.94      0.99      0.96       143
           5       1.00      0.97      0.98       150
           4       0.96      0.93      0.94       154
           7       1.00      0.95      0.98       153
           6       0.95      0.89      0.92       144
           9       0.93      0.96      0.95       148
           8       0.89      0.97      0.93       155

   micro avg       0.95      0.95      0.95      1451
   macro avg       0.95      0.95      0.95      1451
weighted avg       0.95      0.95      0.95      1451

[[117   2   0   1   0   1   0   0   7   1]
 [  4 146   0   0   0   0   0   0   1   1]
 [  0   0 122   0   0   0   0   0   0   1]
 [  0   0   0 141   0   0   0   0   2   0]
 [  1   0   2   1 145   0   0   0   0   1]
 [  2   0   0   0   0 143   0   6   0   3]
 [  0   0   1   1   0   0 146   0   0   5]
 [  5   0   0   0   0   5   0 128   0   6]
 [  1   0   0   5   0   0   0   0 142   0]
 [  1   1   0   1   0   0   0   1   0 151]]
```


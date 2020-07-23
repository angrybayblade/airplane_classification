### Classifying Airplane Family Using CNN.

> Results 

| Aproach | Params | Traning Score | Validation Score |
|---------|--------|------|------------------|
| CNN With GlobalAveragaPooling                                         | 2.7 M | 92% | 21% |
| CNN With GlobalMaxPooling                                             | 2.7 M | 94% | 19% |
| CNN With GlobalAveragePooling ( Reduced Params With Regularizations ) | 1.9 M | 95% | 18% |
| CNN With GlobalMaxPooling ( Reduced Params With Regularizations )     | 1.9 M | 91% | 23% |
| CNN With DepthwiseConv2D                                              | 2.6 M | 88% | 25% |
| CNN With DepthwiseConv2D ( Reduced Parameters )                       | 1.4 M | 91% | 27% |
| CNN With DepthwiseConv2D ( Reduced Parameters )                       | 228 K | 89% | 31% |
| CNN With DepthwiseConv2D ( Reduced Parameters And Dropout)            | 228 K | 89% | 30% |


> I tried several CNN architectures with different training stratagies the best model to work so far was a cobination of stacked CNN and Depthwise Separable CNNs. First i tried some large nets with about 2.7 Mil. parameters. It converged faster but with a lot of overfitting so i tried adding regularizations such as adding weight regularization, biase regularization and activity regularization. Adding regularizations slowed down convergence increased training accuracy but reduced validation accuracy. 

> Then i tried stacking up CNN with Depthwise Separable CNNs it increase some accuracy but not good enough so i tried reducing parameters since it's a clear case of overfitting. So i significantly reduced the number of parameters about 200K. Training accuracy reduced by a small margin but validation accuracy increased by a good margin.

> Then i tried adding some dropout layers , both normal dropout and spatial dropout thi didn't improve the results at all. so finalized CNN with DepthwiseConv2D stcked for the submission.

> Given more time won't have any effect on the output since the data quality is fairly bad. Also images are very small and have very few features that represent their respective family classes. Almost every airplane looks same, the features that differenciate are very small details such as compony logo, small parts which are different for different classes and  some small difference in overall design. So in my opinion this dataset is prone to overfit.

> Cross Validation And Classwise Accuracy Analysis is included in notebook provided.

**This repo contains both of the final CNN models and training notebooks as well as inference scripts.**

> To run prediction script run following command

```bash
python3 predict.py path_to_image.jpg
```

for example

```bash
python3 predict.py ./images/000002.jpg
```

> To train the model copy data in current folder and train the model using the CNN + DepthwiseConv .ipynb. 

**This repo was trained and tested on following environment**

+ Python 3.8
+ Tensorflow 2.2.0
+ OpenCV 4.0.0
+ Nvidia CUDA 10.1
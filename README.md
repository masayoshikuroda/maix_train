# maix_train

https://github.com/sipeed/maix_train

## Build image

```
$ docker build . -t maix_train
```

## Run container
```
$ mkdir out
$ docker run -it --rm -v out:/root/maix_train/out maix_train
```

## Train
```
# python3 train.py -t classifier -z datasets/test_classifier_datasets.zip train
# exit

$ ls out
```

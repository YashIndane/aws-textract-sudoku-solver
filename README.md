![](https://img.shields.io/badge/Python-%F0%9F%90%8D-brightgreen)

# aws-textract-sudoku-solver

![tp](https://user-images.githubusercontent.com/53041219/207024049-5e100995-065b-4805-b3bb-0f35445892c8.png)

## Requirements

```
$ pip install awscli
```

```
$ pip install opencv-python
```

After installation of ```awscli```, login by

```
$ aws configure
```

Now create a bucket in AWS S3 by

```
$ aws s3api create-bucket --bucket <bucket-name> --region <region-name> --create-bucket-configuration LocationConstraint=<region-name>
```

## Working

The file ```detect.py```, saves the image of the board and uploads it to the S3 bucket in AWS. Now by using Textract API with boto3 this image is analyzed with ```FeatureTypes``` as ```TABLES```. The digits are then fed to the sudoku solver which solves and prints the solution.

## Usage

Run the file ```detect.py```, and put your phone with the sudoku board image in front of your webcam

solved sample->

![solved](https://user-images.githubusercontent.com/53041219/207025383-d2d14c91-5d91-49e4-a4a5-01c3b682a6e1.png)

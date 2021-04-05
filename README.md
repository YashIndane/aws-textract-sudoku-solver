![](https://img.shields.io/badge/Python-%F0%9F%90%8D-brightgreen)

# aws-textract-sudoku-solver

## Requirements

```
pip install awscli
```

After installation of ```awscli```, login by

```
aws configure
```

Now create a bucket in AWS S3 by

```
aws s3api create-bucket --bucket <bucket-name> --region <region-name> --create-bucket-configuration LocationConstraint=<region-name>
```

## Usage

Run the file ```detect.py```, and put your phone with the sudoku board image in front of your webcam




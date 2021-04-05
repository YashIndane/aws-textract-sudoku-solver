# aws-textract-sudoku-solver

## Requirements

```
pip install awscli
```

After installation of ```awscli``` login by

```
aws configure
```

Now create a bucket in AWS S3 by

```
aws s3api create-bucket --bucket <bucket-name> --region <region-name> --create-bucket-configuration LocationConstraint=<region-name>
```



# S3-API

## Technologies/Tools and Frameworks

* *Programming Language - Framework*: Python3.8 - Flask
* *Containerization*: Docker


### ECS TASK ROLE - IAM POLICY
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::fargate-app-bucket/*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::fargate-app-bucket"
        }
    ]
}

```
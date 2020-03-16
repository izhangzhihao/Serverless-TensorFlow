# Serverless-TensorFlow
Running TensorFlow on AWS Lambda(from this [blog](https://medium.com/@mike.p.moritz/running-tensorflow-on-aws-lambda-using-serverless-5acf20e00033))

## Build & run

```shell script
npm install -g serverless
```

To deploy you will need an AWS account and your credentials properly configured. For details see the [docs](https://serverless.com/framework/docs/providers/aws/guide/credentials/).

```shell script
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
serverless plugin install -n serverless-python-requirements
serverless deploy -v
```

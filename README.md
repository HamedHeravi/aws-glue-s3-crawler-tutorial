# AWS ML Pipeline with Python and Boto3
- aws-glue-s3-crawler-tutorial

This project is a beginner-friendly tutorial for automating a data engineering workflow for machine learning using AWS and Python.

You’ll learn how to:
- Create and manage an S3 bucket
- Upload datasets using the Boto3 SDK
- Use AWS Glue to crawl and catalog data automatically
- Set up a Python virtual environment

This project is for beginners aiming for the AWS Certified Machine Learning – Specialty exam prep or anyone building ML pipelines on AWS.

## Features

- S3: Raw data storage for machine learning
- Glue Crawler: Auto-discovers schema and catalogs data
- Python + Boto3: Fully scriptable workflow using AWS SDK
- Iris Dataset: Classic dataset for demos and ML experiments

## Project Structure

```
aws-ml-pipeline-boto3/
├── env/                      # Python virtual environment
├── scripts/
│   ├── create_s3_bucket.py
│   ├── upload_dataset.py
│   ├── create_glue_crawler.py
│   └── run_crawler.py
├── datasets/
│   └── iris.csv
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/aws-ml-pipeline-boto3.git
cd aws-ml-pipeline-boto3
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate        # For Linux/macOS
.\env\Scriptsctivate         # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the project step by step:
```bash
python scripts/create_s3_bucket.py
python scripts/upload_dataset.py
python scripts/create_glue_crawler.py
python scripts/run_crawler.py
```

## Dataset

The Iris dataset (included) is downloaded and uploaded to S3 during the setup. You can replace it with your dataset by updating the path in the scripts.

## Resources

- [AWS Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/)
- [AWS Certified ML Specialty](https://aws.amazon.com/certification/certified-machine-learning-specialty/)

## Contributing

Feel free to fork this repository and submit a pull request. Suggestions, issues, and improvements are always welcome!

## License

This project is licensed under the MIT License.

## End To End Sagemaker Project
* By Adam Lang
* Date: 3/6/2025

# Steps to setup
1. Create virtual environment: `conda create -p venv python==3.10 -y`
    * To listall venvs: `conda info --envs`
    * Make sure to select python env --> `jupyter kernel`
2. Make sure the `requirements.txt` is updated with all necessary packages.
    * Note: if you install `sagemaker` it should also co-install `boto3` sdk.

3. Activate the virtual environment: `conda activate venv/`

4. Install `requirements.txt` run this: `pip install -r requirements.txt`

5. Create `.ipynb` file: `research.ipynb`. We will use this to interact with AWS SageMaker.

6. Setup AWS CLI, run this command: `aws configure`
    * Follow directions for access keys.
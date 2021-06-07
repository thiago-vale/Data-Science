import os

# Super simple pipeline chaining the crawler, cleaning,
# removing outliers and training scripts

# os.system("python crawler.py")
os.system("python cleaning.py")
os.system("python removing_outliers.py")
os.system("python model_training.py")
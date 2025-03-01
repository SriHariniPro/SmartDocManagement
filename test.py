from transformers import pipeline

try:
    classifier = pipeline("sentiment-analysis")
    print(classifier("Hello, world!"))
except Exception as e:
    print("Error:", e)

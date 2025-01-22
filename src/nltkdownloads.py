import nltk 

resources = ["punkt","stopwords","wordnet"]
 
def install_nltk_resources():
    for resource in resources:
        try:
            # Check if the resource is already downloaded
            nltk.data.find(f'tokenizers/{resource}')
            print(f'{resource} is already installed.')
        except LookupError:
            # Download the resource if not found
            print(f'Downloading {resource}...')
            nltk.download(resource)

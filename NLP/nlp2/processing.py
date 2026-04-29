import preprocessing as PP

# Combination of all functions
def clean_text_pipeline(text, language="english"):
    # Step 1: Remove URLs
    text = PP.remove_urls(text)
    
    # Step 2: Remove HTML tags
    text = PP.remove_tags(text)
    
    # Step 3: Remove punctuation & special characters
    text = PP.RemoveChars(text)
    
    # Step 4: Convert to lowercase
    text = PP.ToLower(text)
    
    # Step 5: Remove stopwords
    text = PP.remove_stopwords(text, language)
    
    return text
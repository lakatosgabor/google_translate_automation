from googletrans import Translator
import pandas as pd
import time
# Load the TSV file into a DataFrame
file_path = 'output.csv'
df = pd.read_csv(file_path, delimiter='\t')

# Create a translator object
translator = Translator()

# Translate and update the 'query_short' column
for index, row in df.iterrows():
    english_text = row['query_long']
    try:
        translated_text = translator.translate(english_text, dest='hu').text
    except:
        translated_text = translator.translate(english_text, dest='hu').text
    finally:
        time.sleep(3)
        translated_text = translator.translate(english_text, dest='hu').text

    time.sleep(3)
    df.at[index, 'query_long'] = translated_text
    print(index)
    # Save the updated DataFrame back to the TSV file
    df.to_csv('output.csv', sep='\t', index=False)

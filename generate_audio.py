import requests
import json
import csv

def synthesize_voice(text, speaker, filename="output.wav"):
    
    query_payload = {'text': text, 'speaker': speaker}
    query_response = requests.post(f'http://localhost:50021/audio_query', params=query_payload)

    if query_response.status_code != 200:
        print(f"Error in audio_query: {query_response.text}")
        return

    query = query_response.json()

   
    synthesis_payload = {'speaker': speaker}
    synthesis_response = requests.post(f'http://localhost:50021/synthesis', params=synthesis_payload, json=query)

    if synthesis_response.status_code == 200:
        
        with open(filename, 'wb') as f:
            f.write(synthesis_response.content)
        print(f"音声が {filename} に保存されました。")
    else:
        print(f"Error in synthesis: {synthesis_response.text}")

if __name__ == "__main__":

    csv_file_path = 'your_file.csv'

    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        
        for row in csv_reader:
            for word in row:
        
                synthesize_voice(word, speaker=41, filename= word + '.mp3')

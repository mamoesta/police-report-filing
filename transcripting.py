import whisper
import os

def generate_transcript(input_files: list, output_directory: str,try_gpu = False):
    model = whisper.load_model("large-v2")
    ct = 0
    for item in input_files:
        print('transcribing: ', str(ct), ' out of ', len(input_files)) 
        print('file name: ', item)
        with open('./completed.txt', 'w') as f:
            f.write(item + '\n')
            f.close()
        res = model.transcribe(item, fp16=False, language = "english")
        destination = output_directory + os.path.basename(item) + '.txt'
        with open(destination, 'w') as f:
            f.write(res['text'])
            f.close()
        ct+=1
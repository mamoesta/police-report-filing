import whisper

def generate_transcript(input_files: list, output_directory: str,try_gpu = False):
    model = whisper.load_model("large-v2")
    with open(output_directory + 'manifest.txt', 'w') as f:
        f.write('\n'.join(input_files))
        f.close()
    ct = 36
    for item in input_files:
        print('transcribing: ', str(ct), ' out of ', len(input_files)) 
        print('file name: ', item)
        res = model.transcribe(item, fp16=False, language = "english")
        destination = output_directory + str(ct) + '.txt'
        with open(destination, 'w') as f:
            f.write(res['text'])
            f.close()
        ct+=1
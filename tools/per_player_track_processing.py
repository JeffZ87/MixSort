import os

def process_tracks(expn, file_ext):
    '''
    expn(experiment name): the name of experiment denoted by --expn
    file_ext: file name of track output with extention i.e. .txt

    example: process_tracks('yolox_x_sports_mix', 'tack_output.txt')
    '''
    root = f'./YOLOX_outputs/{expn}'
    prediction_path = f'{root}/track_vis'
    
    file_name = file_ext.split('.')[0]
    output_dir = f'{prediction_path}/{file_name}_player'
    os.makedirs(output_dir, exist_ok=True)

    file_ext = open(f'{prediction_path}/{file_ext}', 'r')
    for line in file_ext:
        predictions = line.split(',')
        output_file = f'{output_dir}/player_{predictions[1]}.txt'
        player_file = open(output_file, 'a+')
        player_file.write(line)
        player_file.close()

def process_all_tracks(expn):
    root = f'./YOLOX_outputs/{expn}'
    prediction_path = f'{root}/track_vis'
    prediction_files = get_txt_files(prediction_path)

    for file in prediction_files:
        process_tracks(expn, file)

def get_txt_files(dir_path):
    res = []
    # Iterate directory
    for file in os.listdir(dir_path):
        # check only text files
        if file.endswith('.txt'):
            res.append(file)

    return res

# if __name__ == '__main__':
#     process_tracks('yolox_x_sports_mix', '2024_02_28_22_20_16.txt')
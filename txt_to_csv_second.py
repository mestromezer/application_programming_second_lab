import csv
import os


def write_as_csv(path_to_dataset, paths_to_files):

    with open("dataset_csv_second.csv", "w+", encoding='utf-8', newline='') as file:
        csv_file = csv.writer(file, delimiter=';')
        csv_file.writerow(["Absolute path", "Relative path", "Class"])
        shift = -9

        for i in range(0, len(paths_to_files)):
            paths_to_files[i] = paths_to_files[i][0:shift] + \
                "_" + paths_to_files[i][shift+1:]
            csv_file.writerow([f'{path_to_dataset+paths_to_files[i]}',
                              f'../dataset{paths_to_files[i]}', f'{paths_to_files[i][1]}'])


def get_paths_to_files(path_to_dataset):

    paths_to_files = list()

    for folder_num in range(1, 6):
        folder_path = path_to_dataset+'/'+str(folder_num)
        num_of_files = sum(os.path.isfile(os.path.join(folder_path, f))
                           for f in os.listdir(folder_path)) + 1

        for file_num in range(1, num_of_files):
            path_to_file = folder_path+f'/{(file_num):04}'+'.txt'
            print(f'{folder_num} : {(file_num):04}')
            paths_to_files.append(path_to_file[len(path_to_dataset):])

    return paths_to_files


if __name__ == '__main__':

    path_to_dataset = os.path.abspath("../first_lab/dataset")
    paths_to_files = get_paths_to_files(path_to_dataset)

    write_as_csv(path_to_dataset, paths_to_files)

    print("Работа окончена")

import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for directory_name, subdirectories, filenames in os.walk('.'):

        for i in filenames:
             new_name = get_fixed_filename(i)
             print("Renaming {} to {}".format(i, new_name))

             full_name = os.path.join(directory_name, i)
             new_name = os.path.join(directory_name, get_fixed_filename(i))
             os.rename(full_name, new_name)


def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()

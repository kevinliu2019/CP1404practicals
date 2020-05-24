import os


def main():
    expansion_classification = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        expansion = filename.split('.')[-1]
        if expansion not in expansion_classification:
            classification = input("What category would you like to sort {} files into? ".format(expansion))
            expansion_classification[expansion] = classification
            try:
                os.mkdir(classification)
            except FileExistsError:
                pass

        os.rename = (filename, "{}/{}".format(expansion_classification[classification], filename))


main()

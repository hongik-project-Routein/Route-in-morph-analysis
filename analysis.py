def main():
    with open('result/mecab.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    morphemes = [line.strip().replace("'", "").split(',') for line in lines]

    with open('result.txt', 'w', encoding='UTF-8') as result_file:
        for line in morphemes:
            result_file.write(str(len(line)))
            result_file.write('\n')
                    
if __name__ == "__main__":
    main()
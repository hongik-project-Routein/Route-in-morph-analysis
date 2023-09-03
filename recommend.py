from konlpy.tag import Hannanum, Komoran, Kkma, Okt, Mecab
import time

def run_hannanum(lines):
    hannanum = Hannanum()
    File = open('result/hannanum.txt', 'w', encoding='UTF-8')
    
    start = time.time()

    for line in lines:
        if line != '\n':
            File.write(str(hannanum.morphs(line)))
            File.write('\n')

    File.write(f'실행시간 : {time.time() - start}')

    File.close()


# 특수문자와 이모티콘을 분석하지 못함 (사용 못할듯)
def run_komoran(lines):
    komoran = Komoran()
    File = open('result/komoran.txt', 'w', encoding='UTF-8')

    start = time.time()

    for line in lines:
        if line != '\n':
            File.write(str(komoran.morphs(line)))
            File.write('\n')
    
    File.write(f'실행시간 : {time.time() - start}')


    File.close()


# 특수문자와 이모티콘을 분석하지 못함 (사용 못할듯)
def run_Kkma(lines):
    kkma = Kkma()
    File = open('result/kkma.txt', 'w', encoding='UTF-8')

    start = time.time()

    for line in lines:
        if line != '\n':
            File.write(" ".join(kkma.morphs(line)))
            File.write('\n')
    
    File.write(f'실행시간 : {time.time() - start}')

    File.close()


def run_Okt(lines):
    okt = Okt()
    File = open('result/okt.txt', 'w', encoding='UTF-8')

    start = time.time()

    for line in lines:
        if line != '\n':
            File.write(str(okt.morphs(line)))
            File.write('\n')

    File.write(f'실행시간 : {time.time() - start}')

    File.close()


# 뭔가 다른 것을 설치하고 사용해야 함..
def run_Mecab(lines):
    mecab = Mecab()
    File = open('result/mecab.txt', 'w', encoding='UTF-8')

    for line in lines:
        if line != '\n':
            File.write(str(mecab.morphs(line)))
            File.write('\n')
    
    File.close()



def main():
    File = open('recommend.txt' ,'r', encoding='UTF-8')
    lines = File.readlines()
    run_hannanum(lines)
    run_Okt(lines)
    run_Kkma(lines)
    run_komoran(lines)
    # run_Mecab(lines)


    File.close()


if __name__ == "__main__":
    main()
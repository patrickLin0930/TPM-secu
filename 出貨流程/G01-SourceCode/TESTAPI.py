import subprocess,os,time
from API import verify,capture

def main():
    a,b,c,d=verify('sig','CO.dat','./','./')
    #a 為驗證數位簽章結果 
    #b 為數位簽章0~128字節
    #c 為數位簽章169~200字節
    #d 為數位簽章500~675字節

    if (a==True ): 
        print("成功 1")
        print("成功 2")
        print("成功 3")
        print("成功 4")
        print("成功 5")
        print("成功 6")
    else :
        os.exit(1)

main()


import subprocess,os,time


def capture(rssaname,filename,rssapath,filepath):##可彈性變數為數位簽章檔案名稱、被簽名的檔案名稱(包括副檔名)、數位簽章檔案路徑、被簽名的檔案路徑、上下文件名稱及路徑


    password = 'qqq123'

    commandnvread = ' > '+rssapath+rssaname+'.rssa'  ##建立空白.rssa檔案
    (status, result)=subprocess.getstatusoutput('echo %s| sudo -S %s' %(password,commandnvread))


    commandnvread = 'sudo tpm2_nvread -C o 0x01000001 -o '+rssapath+rssaname+'.rssa -P ownerauth'  ##>匯出nv內簽章到空白.rssa //-i 指定存放nv索引0x01000001內容的檔案
    (status, result)=subprocess.getstatusoutput('echo %s| sudo -S %s' %(password,commandnvread))


    commandverify = 'sudo tpm2_verifysignature -c 0x81010002'+' -g sha256 -m '+filepath+filename+' -s '+rssapath+rssaname+'.rssa'  ##驗證在外面的數位簽章  -m被簽名的文件檔  -s數位簽章檔案 -g數位簽章算法 -c上下文件檔
    (status, result)=subprocess.getstatusoutput('echo %s| sudo -S %s' %(password,commandverify))
    sign=result


    commandverify = 'sudo rm '+rssapath+rssaname+'.rssa'  ##刪掉外面的數位簽章檔案
    (status, result)=subprocess.getstatusoutput('echo %s| sudo -S %s' %(password,commandverify))


    return sign ##回傳驗證用變數 數字簽名驗證成功回傳Verify signature successed! /失敗回傳Verify signature failed!

def verify(rssaname,filename,rssapath,filepath): ##呼叫後回傳判斷結果，成功為finalresult 失敗則關閉程式。
  
    ver="Verify signature successed!" 

    if (ver==str(capture(rssaname,filename,rssapath,filepath))): 
        return True
    else :
        return False
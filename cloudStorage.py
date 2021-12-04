import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(fileFrom):
            for filename in files:
                with open('rb') as f:
                    dbx.files_upload(f.read(), mode=WriteMode('overwrite'))

def main():
    accessToken = 'sl.A9gQsjTRTcYHVfcbZ7i9zj-g9G192enxnNNI88uJXp06Sio4sARHa3vs-7ynOantwVkEvZOSf2TYJjpnuw14IFY9a-S1n89YtGt2l3fj0-0UT9XksVCU7B1GkQfj_xiEyIjSGO8'
    transferData = TransferData(accessToken)
    fileFrom = str(input("Enter The Folder Path :- "))
    fileTo = input("Enter The Path To Upload To Dropbox:- ")
    transferData.uploadFile(fileFrom, fileTo)
    print("File Has Been Transfered")

main()



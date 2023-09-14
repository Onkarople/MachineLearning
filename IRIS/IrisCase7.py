from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import os
from sys import *
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule


def Mailx(mailid,fname):
    from email import encoders
    mail_content = '''
    Thank You   
    '''
    #The mail addresses and password
    sender_address = 'opleonkar@gmail.com'
    sender_pass = 'zctfdfhevyzaxfgp'
    receiver_address = mailid
    #Setup the MIME

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'
    #The subject line
    #The body and the attachments for the mail

    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = fname
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename

    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')



def MarvellousKNeighborsCassifier(data,target):
   
    #2:manipulate the data
    Data_train,Data_test, Target_train,Target_test=train_test_split(data,target,test_size=0.5)   #divide the data in four set

    Classifier=KNeighborsClassifier()

    #3:Bulid the model
    Classifier.fit(Data_train,Target_train)

    #4:test the model
    predictions=Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test,predictions)

    #5:Improve---Missing

    return Accuracy

    

def main():
    Dataset=pd.read_csv(r"C:\Users\Onkar Ople\Desktop\iris.csv")     #1 load the data
    df=pd.DataFrame(Dataset,columns=['sepal.length','sepal.width','petal.length','petal.width','variety'])
    data=df[["sepal.length","sepal.width","petal.length","petal.width"]]
    target=df[["variety"]]

    schedule.every(1).minutes.do(lambda:MarvellousKNeighborsCassifier(data,target))

    Ret= MarvellousKNeighborsCassifier(data,target)
    Accuracy=Ret*100


    timestr = time.strftime("%Y%m%d-%H%M%S")
    FileName=os.path.join("log%s.txt"%(timestr))



    fd=open(FileName,'a')
    fd.write("Accuracy of Datasets:")
    fd.write("\n")
    fd.write("Accuracy of iris dataset with KNN is:")
    fd.write(str(Accuracy))
    print("Accuracy of iris dataset with KNN is:",Ret*100)

    mailid='marvellousinfosystem@gmail.com'

    schedule.every(1).minutes.do(Mailx,mailid,FileName)

    
    while(True):
        schedule.run_pending()
        time.sleep(10)

   

if __name__ =="__main__":
    main()
#Import Required data set
from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import os 
from sys import *
import hashlib
import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



#load the dataset
#Rough 1
#Smooth 0
#Tennis  1
#Cricket 2



def Mailx(mailid,fname):
    from email import encoders
    mail_content = '''
    Graph of BallCase Dataset
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


def BallPredictor(wight,surface):

    data=pd.read_csv('marvellous.csv',index_col=0)

    features_names=['Wight','Surface']

    Weight=data.Wight
    Surface=data.Surface
    type=data.Type

    features=list(zip(Weight,Surface))

    #decide the machine learing algorith
    obj=tree.DecisionTreeClassifier()

    #perform the trainning of model
    obj=obj.fit(features,type)

    #perform the testing
    Ret=obj.predict([[wight,surface]])

    if Ret == 1 :
        print("Your object looks like tennis ball")
    else:
        print("object looks like cricket ball")
    
    df=pd.DataFrame(data,columns=['Wight','Surface','Type'])

    df.plot(x="Type",y=['Wight','Surface'],kind="bar",colormap="green")

    timestr = time.strftime("%Y%m%d-%H%M%S")
    img=os.path.join("Ball%s.jpg"%(timestr))



    plt.savefig(img)
    plt.show()
    plt.close()


    return img

   


def main():
    print("-------------Ball predictor case study--------------")
    
    print("Please enter the weight of your object in grams")
    weight=int(input())

    print("please enter the type of surface of your object (Rough/Smooth) ")
    surface=input()

    if surface.lower()=="rough":
        surface=1
    elif surface.lower()=="smooth":
        surface=0
    else:
        print("Invalid type of surface")
        exit()

    MName="marvellousinfosystem@gmail.com"

    try:
        arr={}
        schedule.every(1).minutes.do(lambda:BallPredictor(weight,surface))


        ret=BallPredictor(weight,surface)

        schedule.every(1).minutes.do(lambda:Mailx(MName,ret))

        while(True):
            schedule.run_pending()
            return_value=arr
            time.sleep(10)
    

    except Exception as E: 
        print("Exception found",E)



    Mailx(MName,ret)


if __name__ =="__main__":
    main()
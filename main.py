
import schedule
import time
import json
from datetime import datetime
from twilio.rest import Client


def job():



    ## set twillo api key
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    ## get today's date. and use that to look up which exersice to do.
    curday = datetime.now().strftime("%m-%d-%Y")

    ## get data from days json file and pull up the activity for today's date.
    with open('./days.json', 'r') as days:
        day = json.loads(days.read())
        for keyval in day:
            if curday == keyval['Date']:
                activity =  keyval['Activity']
                daysTrained =  keyval['DaysTrained']
                dayWeek =  keyval['DayWeek']
                dayTrainNum = int(daysTrained)

    exerciseBlock = ("Hello! Here is your exercise plan for the day to keep you motivated! \nToday is " + dayWeek +",  "+ curday + ". You will be doing the following activity--" + activity + ". You have trained  " + daysTrained + " days so far! \n\n" )

    ## get the inspirational quote based on how many days trained so far.
    with open('./quotes.json', 'r') as quotes:
        file = json.loads(quotes.read())
        quote = file[dayTrainNum]['text']
        author = file[dayTrainNum]['author']
    quoteBlock = ("Inspirational quote of the day\n" + quote+ " --said by " + author )


    # get the youtube link of an exercise that needs a video to complete
    linkBlock = " "
    if activity == "barre":
        linkBlock = ("Here is a link to some YouTube videos for "+activity+ ": " +"https://www.youtube.com/results?search_query=barre+workout+20+minutes+" + " Enjoy your workout! \n\n")
    if activity == "yoga":
        linkBlock = ("Here is a link to some YouTube videos for "+activity+ ": " +"https://www.youtube.com/results?search_query=yoga+workout+30+minutes+" + " Enjoy your workout! \n\n")
    if activity == "HIIT":
        linkBlock = ("Here is a link to some YouTube videos for "+activity+ ": " +"https://www.youtube.com/results?search_query=hiit+workout+15+minutes+" + " Enjoy your workout! \n\n")

    # combine all of the messages to be ready to send with twilio
    body = (exerciseBlock+linkBlock+quoteBlock)
    print(body)

    # construct a message to send using twilio use the text as the body with the combinded messages
    message = client.messages.create(
                              from_='+',
                              body = body,
                              to ='+'
                          )
    print(message.sid)



## schedule a job to run at a certain interval this will then execute the job function
# schedule.every(10).seconds.do(job)
schedule.every().day.at("08:07").do(job)

# create an infinite loop that will always run the service
while True:
    schedule.run_pending()
    time.sleep(1)

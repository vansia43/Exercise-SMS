# Exercise SMS Reminders
You can use this Python script to send exercise reminders and motivation every day. The script uses the Twilio API to send scheduled SMS reminders and motivational quotes. The script can also be used to send links to predefined YouTube searches to help with finding an exercise video for certain activities. 
# Example SMS Message
> Here is your exercise plan for the day to keep you motivated!!
>
> Today is Tuesday, 06-30-2020. You will be doing the following activity: HITT
>
> You have trained 4 days so far. 
>
> Here is a link to some YouTube videos for HIIT: https://www.youtube.com/results?search_query=hiit+workout+15+minutes. Enjoy your workout! `
# Script Logic
## Prerequisites
This program requires a [Twilio license](https://www.twilio.com/pricing). You can obtain a trial version of Twilio. Note that your trial credit will be charged each time that you use the service.
## Converting Days to JSON
First, create the [.csv file](days.csv) with the date, day of the week, activity, and days trained. Then, use the [.csv to JSON](convert_training_days.py) script to convert the file to a [JSON format](days.json). The script calls the .csv file and restructures the data so that it exists as a set of date keys with the value as a dictionary of the different elements from the .csv file.
## Quotes JSON
You can download a [free inspirational quotes](https://forum.freecodecamp.org/t/free-api-inspirational-quotes-json-with-code-examples/311373) JSON file for the inspirational messages that are sent with each SMS. This information is stored in the quotes.json file.
## Constructing a Message
The [main.py](main.py) file uses both JSON files and the Twilio API to construct the SMS message. First, you need to set your Twilio API key that you obtained when creating your account. 
>        account_sid = ''
>        auth_token = ''
>        client = Client(account_sid, auth_token)

Enter your Twilio account ID and authorization token. This creates a client for you to have access to the Twilio API.

Then, the script calls the days.json file and uses the `if curday == keyval['Date']:` command to pull the activity that is associated with today's date. The `exerciseBlock` text is then constructed.
> `("Hello! Here is your exercise plan for the day to keep you motivated! \nToday is " + dayWeek +",  "+ curday + ". You will be doing the following activity--" + activity + ". You have trained  " + daysTrained + " days so far! \n\n" )`

Each of the elements in the `exerciseBlock` is derived from the days.json file.

The `quoteBlock` is then constructed. All elements are derived from the quotes.json file.
>`("Inspirational quote of the day\n" + quote+ " --said by " + author )`

Finally, the `linkBlock` is constructed, which checks to see if the `activity` element is either **barre**, **yoga**, or **HIIT**. A predefined YouTube search such as "HIIT workout 15 minutes" is returned. 

All elements are then combined to construct the message or `body` element. The `client.messages.create` function uses the Twilio API to send the message.  Replace the `+` in the `from` element with your Twilio-assigned number. Replace the `+` in the `to` element with the recipient's number.
>
>      message = client.messages.create(
>                                from_='+',
>                                body = body,
>                                to ='+'
>                             )


## Scheduling a Job
You can schedule the job to run every day at a particular time. For example, you can set the job to send an SMS at 8:00 AM:
> `schedule.every().day.at("08:00").do(job)`

An infinite loop is set that can always run the service with the following command:
>       while True:
>         schedule.run_pending()
>         time.sleep(1)

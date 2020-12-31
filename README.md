# Exercise SMS Reminders
You can use this module to send you exercise reminders and motivation everyday. The program uses the Twilio API to send scheduled SMS reminders and motivational quotes. The module is also set to send links to predefined YouTube searches to help with finding an exercise video for certain activities. 
# Example SMS Message
> Here is your exercise plan for the day to keep you motivated!!
>
> Today is Tuesday, 06-30-2020. You will be doing the following activity: HITT
>
> You have trained 4 days so far. 
>
> Here is a link to some YouTube videos for HIIT: https://www.youtube.com/results?search_query=hiit+workout+15+minutes. Enjoy your workout! `
# Module Logic
## Prerequisites
This module requires a [Twilio license](https://www.twilio.com/pricing). You can obtain a trial version of Twilio. Note that your trial credit will be charged each time that you use the service.
## Converting Days to JSON
First, I created a [.csv file](days.csv) with the date, day of the week, activity, and days trained. This file was easy to develop as I chose seven activities that would repeat each week. I used a [.csv to JSON](convert_training_days.py) module to convert my file to a [JSON format](days.json). The module takes the .csv file and restructures the data so that it exists as a set of date keys with the value as a dictionary of the different elements from the .csv file.
## Quotes JSON
I downloaded a [free inspirational quotes](https://forum.freecodecamp.org/t/free-api-inspirational-quotes-json-with-code-examples/311373) JSON file for the inspirational messages that would be sent with each SMS.
## Constructing a Message
The [main.py](main.py) file uses both JSON files and the Twilio API to construct the SMS message. First you need to set your Twilio API key that you obtained when creating your account. Then, the module calls the `days.json` file and uses the `if curday == keyval['Date']:` command to pull the activity that is associated with today's date. The `exerciseBlock` text is then constructed.
> `("Hello! Here is your exercise plan for the day to keep you motivated! \nToday is " + dayWeek +",  "+ curday + ". You will be doing the following activity--" + activity + ". You have trained  " + daysTrained + " days so far! \n\n" )`

Each of the elements in the `exerciseBlock` are derived from the days.json file.

The `quoteBlock` is then constructed. All elements are derived from the quotes.json file.
>`("Inspirational quote of the day\n" + quote+ " --said by " + author )`

Finally, the `linkBlock` is developed, which checks to see if the `activity` element is either **barre**, **yoga**, or **HIIT**. A predefined YouTube search such as "HIIT workout 15 minutes" is returned. 

All elements are then combined to construct the message or `body`. The following command send the message while replacing the `+` in the `to` element with the recipient's number.
>
>      message = client.messages.create(
>
>                                from_='+',
>
>                                body = body,
>
>                                to ='+'
>
>                             )


## Scheduling a Job
You can schedule the job to run everyday at a particular time. For example, you can set the job to send SMS at 8:00 AM:
> `schedule.every().day.at("08:07").do(job)`

An infinite loop is set that can always run the service with the following commands:
> `while True:
>   schedule.run_pending()
>   time.sleep(1)`

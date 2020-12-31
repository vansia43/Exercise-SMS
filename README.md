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
xx
## Scheduling a Job

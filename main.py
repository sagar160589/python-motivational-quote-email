import pandas,random,smtplib,datetime as dt,json

#Reading quotes.txt and converting to a list to pick random quotes
with open("quotes/quotes.txt") as quote:
    quote_list = quote.readlines()

names = pandas.read_csv("names/names.csv")


#Get todays date
curr_date = dt.datetime.now()
todays_date = curr_date.date()

#Get email configs- this should be from enviornment but for simplicity kept in a config file inside code
with open("email_config/config.json", mode='r') as email_config:
    email_config_json = json.load(email_config)
    from_email = email_config_json['from_email']
    password = email_config_json['password']

#Get dictionary out of the dataframe
name_dict = {row['name']:row['email'] for (index,row) in names.iterrows()}

#Send motivational quotes via email
try:
    for name,email in name_dict.items():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=from_email,password=password)
            connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:Motivational quote for today:\n\nHi {name},\n\n{random.choice(quote_list)}")
        print(f"Sent motivational quote to {name}")
except KeyError:
    print(f"Error in sending email to {name}")




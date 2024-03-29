Adjust sampledataset REST API repository.

Access current ad campaign data for any date, channel, os. 
Data is available in **JSON** format

Call data for the filtered parameters grouped and sorted according to the parameters specified

**API call**

Parameters shown in curly brackets are specified below

    127.0.0.1:8000/?show={show}&filter_param1={filter_param2}&filter_param2={filter_param2}&group_by={group_by}&order_by={order_by}&format={format}
_____________
**REQUEST PARAMETERS**

Filter parameters - one or more of the following:

    channel     optional    Channel name ("adcolony", "chartboost", "vungle", "apple_search_ads", "google" ,"facebook", "unityads")
    country     optional    Comma separated list of Two-letter country cods defined in ISO 3166-1 alpha-2
    os	    optional	Operating System name ("ios", "android")
    date_from   optional    Start of period YYYY-MM-DD (including). Example 2017-06-01
    date_to     optional    End of period YYYY-MM-DD (excluding). Example 2017-06-01

Grouping and Sorting parameters

    group_by    optional    Group data by columns. Comma separated list of columns (one or more of: date, channel, country, operating system)
    order_by    optional    Order by column. Comma separated list of columns plus cpi. Default ordering is ascending. Prefix '-' for descending order
                            cpi is derived metric CPI (cost per install) which is calculated as cpi = spend / installs

Format

    format     optional    'json' or 'api'. Default is 'api'

**Examples of API calls:**
___________

Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.

    127.0.0.1:8000/?show=impressions,clicks&date_to=2017-06-01&group_by=channel,country&order_by=-clicks&format=json

Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

    127.0.0.1:8000/?show=installs&date_from=2017-05-01&date_to=2017-05-31&group_by=date&order_by=date&format=json

Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

    127.0.0.1:8000/?show=revenue&country=US&date_from=2017-06-01&date_to=2017-06-01&group_by=os&order_by=-revenue&format=json

Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. 

    127.0.0.1:8000/?show=cpi,spend&country=CA&group_by=channel&order_by=-cpi&format=json

Columns that can be used in request (parameter 'columns') and be shown in resulting dataset
___________________
    date	channel	country	os	impressions	clicks	installs	spend	revenue

**Installation**

1. Open terminal and change directory for the one to be used for installation
2. Enter command `git clone git@github.com:rudotcom/adjust_api.git`
3. In case you use https: `git clone https://github.com/rudotcom/adjust_api.git`
4. Enter following commands:
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
5. Install PostgreSQL, create a user (role) 'adjust' with READ (and CREATE DATABASE for testing) privileges for table api_sampledataset and password specified in file AdjustAPI/settings.py
   Import dataset to the database
6. Run the server - `python manage.py runserver`
________

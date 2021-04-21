Adjust sampledataset REST API repository.

Access current ad campaign data for any date, channel, os. 
Data is available in **JSON** format

Call data for the filtered parameters grouped and sorted according to the parameters specified

**API call**

Parameters shown in curly brackets are specified below

    127.0.0.1:8000/api/sampledata?columns={show}&os={os}&date_from={date_from}&date_to={date_to}&group_by={group_by}&order_by={order_by}&order={order}
_____________
**PARAMETERS**

    columns        required    Fields to be shown in queryset. List of fields separated by comma. See below
Filter parameters

    channel     optional    Channel name ("adcolony", "chartboost", "vungle", "apple_search_ads", "google" ,"facebook", "unityads")
    country     optional    Two-letter country code defined in ISO 3166-1 alpha-2
    os	    optional	Operating System name
    date_from   optional    Start of period YYYY-MM-DD. Example 2017-06-01
    date_to     optional    End of period YYYY-MM-DD. Example 2017-06-01
    cpi         optional    Derived metric CPI (cost per install) which is calculated as cpi = spend / installs

Grouping and Sorting parameters

    group_by    optional    Group data by field. List of fields separated by comma
    order_by    optional    Order by column. List of fields separated by comma
    order       optional    Column order direction (asc, desc)

**Examples of API calls:**
___________

Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.

    127.0.0.1:8000/api/sampledata?show=impressions,clicks&date_to=2017-06-01&group_by=channel,country&order_by=clicks&order=desc

Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

    127.0.0.1:8000/api/sampledata?show=installs&date_from=2017-05-01&date_to=2017-05-31&group_by=date&order_by=date&order=desc

Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

    127.0.0.1:8000/api/sampledata?show=revenue&country=US&date_from=2017-06-01&date_to=2017-06-01&group_by=os&order_by=revenue&order=desc

Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. 

    127.0.0.1:8000/api/sampledata?show=cpi,spend&country=CA&group_by=channel&order_by=cpi&order=desc

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
5.  Change current directory for **AdjustAPI**
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
5. Run the server - `python manage.py runserver`

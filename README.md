# **Gettin Started**

Hi!
So I created this project because I was tired of logging in via Cowin using an OTP to check for availability of vaccines in my area.

Please feel free to clone this code and use for your own friends and family

Stay safe!!

## **How it works?**

So the program gets the vaccines available in an entire district using a district key- which depends on the state. 

You can get the your district key by running **getDistrictIDs.py**, and **replace** the value of StateID with your state ID from the table given below.

| State name                  | State id |
| --------------------------- | -------- |
| Andaman and Nicobar Islands | 1        |
| Andhra Pradesh              | 2        |
| Arunachal Pradesh           | 3        |
| Assam                       | 4        |
| Bihar                       | 5        |
| Chandigarh                  | 6        |
| Chhattisgarh                | 7        |
| Dadra and Nagar Haveli      | 8        |
| Daman and Diu               | 37       |
| Delhi                       | 9        |
| Goa                         | 10       |
| Gujarat                     | 11       |
| Haryana                     | 12       |
| Himachal Pradesh            | 13       |
| Jammu and Kashmir           | 14       |
| Jharkhand                   | 15       |
| Karnataka                   | 16       |
| Kerala                      | 17       |
| Ladakh                      | 18       |
| Lakshadweep                 | 19       |
| Madhya Pradesh              | 20       |
| Maharashtra                 | 21       |
| Manipur                     | 22       |
| Meghalaya                   | 23       |
| Mizoram                     | 24       |
| Nagaland                    | 25       |
| Odisha                      | 26       |
| Puducherry                  | 27       |
| Punjab                      | 28       |
| Rajasthan                   | 29       |
| Sikkim                      | 30       |
| Tamil Nadu                  | 31       |
| Telangana                   | 32       |
| Tripura                     | 33       |
| Uttar Pradesh               | 34       |
| Uttarakhand                 | 35       |
| West Bengal                 | 36       |


For example, if I my district lies in Delhi, I will run getDistrictIDs.py with the StateID value as 9
Upon running, you will recieve a table of the format below

```
$ python getDistrictIDs.py


Central Delhi                    141
East Delhi                       145
New Delhi                        140
North Delhi                      146
North East Delhi                 147
North West Delhi                 143
Shahdara                         148
South Delhi                      149
South East Delhi                 144
South West Delhi                 150
West Delhi                       142
```

Now take the ID to your respective district, and edit it in the Main.py code to get vaccines for your district.
Rum Main.py to get vaccine details in your district till the next five weeks.

###Some variables you can edit to get different results in Main.py

| Variable name    | Description                                    |
| ---------------- | ---------------------------------------------- |
| * **num_weeks**: | looks through certain number of weeks forward, |
 minimum value is 1. Default is 5.                                                       |
| * **district_id**: | enter the district_id of the district you want to get vaccination details of |
| * **age**:         | enter minimum age of vaccination for the slot.                               |
 Enter 18 for centers with vaccination for 18-44 years old, and 45 for 45+ years old. |



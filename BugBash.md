### URL to App
http://ec2-3-142-209-225.us-east-2.compute.amazonaws.com:8000/docs#/

This is our versionv1.0 after fixing issues and adding improvement, some nice-to-have features may be possible in the future:
 - Design the date time for transaction checking more flexible rather than using fixed patter of the datetime
 - Apply security practices to protect user data and the system from vulnerbilities
 - Add more functions in personalizing user profile

Apart from these nice-to-have features, we addressed all issues for this released version

### How to use the App
## User
# Create User

![image](https://github.com/cs5500-project/opp-api/assets/115593195/6bf6d0e0-5bd8-4052-aed7-9d903c81faa6)

To Create new user, type in the username and password
![image](https://github.com/cs5500-project/opp-api/assets/115593195/8f24a2af-39cf-4b18-805a-9f01c45f0b39)

User has been created successfully
![image](https://github.com/cs5500-project/opp-api/assets/115593195/5dbd2883-8cb8-4ee3-a575-6c94608cc3ab)

If the user is existing, an error message will show up
![image](https://github.com/cs5500-project/opp-api/assets/115593195/53a52177-bb95-4b9d-9c6f-1fbfd711797a)


# User Login
Type in the existing user information
![image](https://github.com/cs5500-project/opp-api/assets/115593195/dfaf6db4-7fa0-431b-bd69-1e2630824fc9)

User successfully login
![image](https://github.com/cs5500-project/opp-api/assets/115593195/e47eaa68-ed35-4984-af8f-b7765c90ffeb)

## Card

# Authenticate use before use apis

![image](https://github.com/cs5500-project/opp-api/assets/115593195/d5450046-832c-4707-b855-5952d50c1740)
![image](https://github.com/cs5500-project/opp-api/assets/115593195/b0a1058f-dc28-4119-b79d-fd7c4773a2fb)

# Create a new card

Put the card number and type to create a new card in system

![image](https://github.com/cs5500-project/opp-api/assets/115593195/d7907307-44d2-45b1-a4c3-94626c97344e)
![image](https://github.com/cs5500-project/opp-api/assets/115593195/048f1b5a-e47f-41cb-b425-0bc60f675609)

Add another card ends with 1054

![image](https://github.com/cs5500-project/opp-api/assets/115593195/4eb87c82-d932-4ed3-a97a-ef32eecf9481)

# Get cards

![image](https://github.com/cs5500-project/opp-api/assets/115593195/25d56c10-6c62-4d8c-b146-fb9cf2ad6d50)

After adding another card, there is another card shown in the system

![image](https://github.com/cs5500-project/opp-api/assets/115593195/4f6f2714-61e4-4ab9-bb6e-ebccb7560b7c)

# Get card by Id

The example card id is 1

![image](https://github.com/cs5500-project/opp-api/assets/115593195/881bb1c6-25ec-447e-ac7a-c655702521ce)

If the user put an id that does not exist, an error message will be returned

![image](https://github.com/cs5500-project/opp-api/assets/115593195/4a96af8d-521b-4bd3-9993-b087a473e83d)


# Get card by last four digits

The last four digits of example card is 1053

![image](https://github.com/cs5500-project/opp-api/assets/115593195/1c2a0284-1f44-4493-8eef-2660697cd471)

If the user put the digits that refers to card that does not exist, an error message will be returned

![image](https://github.com/cs5500-project/opp-api/assets/115593195/e7ff1000-6438-48a5-a84b-f56f94bde343)

# Delete card by last four digits

Delete the card ends with 1054

![image](https://github.com/cs5500-project/opp-api/assets/115593195/6db8b127-142b-4ec0-a11a-25de824855b9)

Check the card status
![image](https://github.com/cs5500-project/opp-api/assets/115593195/9e49a256-7d5d-4224-bbdb-d2690844785f)

# Delete card by id

Delete the card with id 1

![image](https://github.com/cs5500-project/opp-api/assets/115593195/37e78fa6-8b1d-47ca-a64f-184b427ec239)

There is no card in the system now

![image](https://github.com/cs5500-project/opp-api/assets/115593195/73b0dbf2-7fa3-47bb-b254-2853beb4634b)

## Transaction 

Add the card ends with 1053 back to show the transaction part

# Create transaction 

Type in the card number, amount and card type, the order has been added into the system

![image](https://github.com/cs5500-project/opp-api/assets/115593195/9a5ce8bc-597c-45cd-92f3-4ca4108d6c8e)

# Get transaction by user

![image](https://github.com/cs5500-project/opp-api/assets/115593195/4c60b333-f895-4e5c-a155-91c22b32a3cf)

# Get all pending transactions

Since this new transaction added with credit card type, it shows up in the pending list

![image](https://github.com/cs5500-project/opp-api/assets/115593195/a8c263a4-f76b-4af9-8a39-8a97fff71ac7)

# Get all processed transactions

There is no debit card yet so right now there is no transaction processed

![image](https://github.com/cs5500-project/opp-api/assets/115593195/a5b1d38f-1692-4602-bd68-22a1cef6fede)

if we add a debit card transaction

![image](https://github.com/cs5500-project/opp-api/assets/115593195/938925a9-3306-4750-864a-3de4171daaf4)

And we can see the transaction is shown here

![image](https://github.com/cs5500-project/opp-api/assets/115593195/fa78235d-3038-4718-9c47-e94ce7f3a6fc)

# Get current balance for processed transactions

We added a debit card transaciton with amount of 100, so the total balance now is 100

![image](https://github.com/cs5500-project/opp-api/assets/115593195/baac3151-c135-42cc-a1e8-cdd4412e870c)

# Check status and update for credit card transaction

the transaction created at date: Wed,06 Dec 2023 09:26:01 GMT, it takes two days to process so right now there is no result yet

![image](https://github.com/cs5500-project/opp-api/assets/115593195/84f39271-3e9d-45d8-81f8-68850af81277)


# Get current balance processed transactions with time period

There is an error if the user does not put valid date time 

![image](https://github.com/cs5500-project/opp-api/assets/115593195/17820e86-2188-4f48-a265-0c3d17f04e4a)

By putting time with format: start format: 2023-11-13 00:00:00 end format: 2023-11-13 23:59:59, the transaction is returned

![image](https://github.com/cs5500-project/opp-api/assets/115593195/6e45b28a-1d5e-41b6-b078-c0525f247faf)


# Get transaction by id

Now we have two transaction with id 81 and 82, by typing 81, we get a transaction returned

![image](https://github.com/cs5500-project/opp-api/assets/115593195/ad82bec7-ab4e-4f4a-a90a-cff26809a768)

# Delete transaction by id

If the user wants to delete a transaction, for example 82 

![image](https://github.com/cs5500-project/opp-api/assets/115593195/ee046752-8eb9-487a-b2db-b2dff01c97df)

And the transaction with id 82 has been deleted

![image](https://github.com/cs5500-project/opp-api/assets/115593195/1e4ad57a-a3c7-45df-bf8b-da6cdb4811db)


### Link to issue page
https://github.com/cs5500-project/opp-api/issues





















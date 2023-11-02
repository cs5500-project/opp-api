# Low-leval Design
## ERD
[Link to LucidChart](https://lucid.app/lucidchart/46d3f75f-e18d-434b-a764-33db2f0f6cc6/edit?viewport_loc=-7087%2C-2325%2C3369%2C3123%2C0_0&invitationId=inv_1814f6ab-0de8-45a3-8abf-234cca2ee2c0)
## ReST API design and specifications
### Order
GET /api/order/{user_id}

get_order_by_user()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| User id       | int        | Logged-in user id |

POST /api/order/{user_id}

create_order_by_user()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| User id       | int        | Logged-in user id |

Delete /api/order/{user_id}

delete_order_by_user()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| User id       | int        | Logged-in user id |

Get /api/order/{user_id}/?time=

get_order_by_user_within_time_period()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| User id       | int        | Logged-in user id |
| time          | TimeStamp  | Time of the order placed  |

### Card Validation
Get /api/card_validation/{card_number}/?type=

get_validation_status_by_number()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| card_number   | int        | Card number input by user |
| type          | string     | Card type: debit or credit  |

### User Authentication
Get /api/users/{user_id}

get_user_by_id()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| User id       | int        | Unique identification id for registered user  |

Get /api/users/{user_name}

get_user_by_name()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| user_name     | string     | User name for registered user |

Get /api/users/

get_users()


Put /api/users/{password}

update_user_password()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| password      | string     | Password set by user |

Post /api/users

register_user()

Post /api/auth/login

user_login_validation()

Description: Allow users to log in and obtain an authentication token.
Request: JSON payload with username and password.
Response: JSON with an authentication token.

### Transactions
GET /api/transaction/{user_id}/?processed=

get_current_fully_processed_balance()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| User id       | int        | Logged-in user id |
| processed     | string     | Processed status  |


| Response Field          | Field Type | Field Description |
| --------                | -------    |   -------         |
| Fully processed balance | float      | Fully processed balance |


GET /api/transaction/{user_id}/?date=&?processed=

get_fully_processed_balance_with_date()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| User id       | int        | Logged-in user id |
| date          | datetime   | date requested    |
| processed     | str        | fetch only processed transactions |

| Response Field                    | Field Type | Field Description |
| --------                          | -------    |   -------         |
| Fully processed balance with date | float      | Fully processed balance |


GET /api/transaction/{user_id}/?=processed

get_fully_processed_transactions_list()

| Request Field | Field Type | Field Description |
| --------      | -------    |   -------         |
| User id       | int        | Logged-in user id |
| processed     | string     | Processed status  |

| Response Field                | Field Type | Field Description |
| --------                      | -------    |   -------         |
| Fully processed transactions  | list       | Fully processed transactions |


GET /api/transaction/{user_id}/?=in-processing

get_account_receivables_list()

| Request Field     | Field Type | Field Description  |
| --------          | -------    |   -------          |
| User id           | int        | Logged-in user id  |
| in-processing     | string     | processing status  |

| Response Field       | Field Type | Field Description |
| --------             | -------    |   -------         |
| account receivables  | list       | list of receivables   |


PUT /api/transaction/debit/{merchant_id - from order}

update_balance_debit_card()

| Request Field     | Field Type | Field Description  |
| --------          | -------    |   -------          |
| merchant id       | int        | merchant id registered for the order  |
| amount_paid       | float      | amount paid by customer  |

| Response Field  | Field Type | Field Description |
| --------        | -------    |   -------         |
| success/failed  | json       | success/failed update |


PUT /api/transaction/credit/{merchant_id - from order}

update_balance_credit_card()

| Request Field     | Field Type | Field Description  |
| --------          | -------    |   -------          |
| merchant id       | int        | merchant id registered for the order  |
| amount_paid       | float      | amount paid by customer  |

| Response Field  | Field Type | Field Description |
| --------        | -------    |   -------         |
| success/failed  | json       | success/failed update |

#### potential error messages, HTML code: 400 bad request, 401 unauthorized, 500 Internal server

### Merchants
    None for now

## API Sequence Diagram
[Link to LucidChart](https://lucid.app/lucidchart/a70e3c66-9187-4fe6-9096-4d59370e7682/edit?viewport_loc=-1623%2C-1069%2C2246%2C2082%2C0_0&invitationId=inv_bde619a4-b2c6-4636-9f13-85367c327943)
## Backend Module Description
### Class Diagram
[Link to LucidChart](https://lucid.app/lucidchart/46d3f75f-e18d-434b-a764-33db2f0f6cc6/edit?viewport_loc=-7087%2C-2325%2C3369%2C3123%2C0_0&invitationId=inv_1814f6ab-0de8-45a3-8abf-234cca2ee2c0)



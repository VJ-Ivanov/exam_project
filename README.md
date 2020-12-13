# exam_project
Project in connection with a course examination to prove and showcase understanding of the Django framework

The main goal of this application is to facilitate the work between 3 parts of the transport chain - Sales, Pricing and Operations.

Sales will create Customer, Warehouse and Request instances that will in turn need to be quoted. 
This is then done via the Pricing user who creates an offer instance connected to the request.

The Pricing user has a view where he can see which requests remain open so he can give a quote.
In Turn the Sales user can decide wen to publish a customer instance with all its associated offers.
When this happens they are active and shown in the main ListView to be used by Operations users.

The logic for the three user groups is still implicit as the business case would require a third party to verify that status.
That is why a user can not choose his department at first and is automatically assigned to Operations. 

Every user is responsible for his own data and has full CRUD over it. Operation users have most GET permissions.
Sales and Pricing can GET everything but are only able to POST their respective fields.

'Master Data' like the Seaports and Countries is only available in the admin view. As these values are considered constants
with the option of expanding them. Another important value - the direction (Import and Export) is hardcoded in the model
as it is a fixed constant like left and right.

The benefit of this app is to facilitate work between the three types of users when there are more that one person in a department.
Everybody will have access to the information he would need to work on his part of the transport chain. 

AIM💕:
   
   To scrape data from Redbus web app and to create a interactive Streamlit application to visualise the bus details of Ten different government transport corporations.Operations involved are Collection of Data,Stroing the data in local database and Creating a Streamlit application to visualise the data.

Technologies🐱‍🏍:
   
   *IDE's Used-Jupyter Notebook,VS Code,MYSQL Workbench
   
   *Language-Python with necessary primary libraries like Selenium,Streamlit,Pandas,SQLalchemy and some of secondary libraries/modules are also used for supporting the project which you could see clearly in the Jupyter Notebook and VS code files that I have attached above.In addition to this SQL quries are also used to retrieve the data from the database.

Procedural Explaination✔:(1st file-Jupyter Notebook🎈)==>Redbus_project.ipynb FILE

   1.Imported necessary libraries for this project.Selenium is the major one among the others, that is used for automation of Scaraping the data from the web app(Redbus) with the help of Chrome webdriver.The aim is to collect the bus details available in Ten different Government Transport Corporations.Each corporation provide services for different routes.For all the available routes,there will be huge number of Government buses and private buses functioning.The necessary details of each and every buses are scraped and are stored in different dataframes each for a Corporation.

   2.Then the 10 different dataframes each for 10 Transport corporation, containing the route details and bus details, are all combined to get a clear view of all the bus routes and the buses operating for the specific routes in a single dataframe.Then the data collected is efficently stored in local data base for future retrieval and visualisation in the Streamlit application.MYSQL Workbench is used for data storage.A Database Connection is established from Jupyter Notebook to the workbench containing local database and Data migration is done with the help of Engine created using SQLalchemy engine.

   3.In this file,the code and functions used for all the above process are available clearly with the clear explanation.The Jupyter notebook itself has a clear step by step procedure from Data Collection to the Storage.Comments are also used for line by line explanation.Five different Cells are used for five different process and all the cell explanations are also given clearly for better understanding.Lastly, half of the need of this project ,from Data retrieval to Data Storage is achieved in this file of Jupyter notebook.


Procedural Explanation✔:(2nd file-VS Code🎈)==>bus_booking_app.py FILE

   1.Imported necessary libraries for this project,Streamlit is the major one among the others,that is used for developing an interactive application(GUI).This application is used to retrieve the data from the database and visualise the data according to the user's request.Here,the user can search for a specific route and the application will visualise all the buses providing service for that specific route.This application also consist of different filters for the user, to get visual of a specific type of buses that match their needs for the route they searched.

  2.The filters available are developed with the help of Streamlit inbuilt functions.The filters used in this application are min_price,max_price,min_star_rating,bus_types in specific to a route.With filters min_price and max_price the user can visualise the buses available within the price range.With help of min_rating he can set a threshold for star rating and only the buses greater than that star rating will be visualised.Finally, using the bus_type filter, the user can visualise the buses of his convenient bus types alone.Irrespective of Visualisation the user can select the bus he need to travel using bus id and can book the bus from this application.

  3.As a final result the seat no and the details of the bus, the user booked will be displayed.This is the complete working of the application and some of the screenshots are attached below for a understanding of working of the application.The database connection is also established here in VS Code using mysql connector for data retrieval.Some of the queries are also used for retrieval and visualisation of the data.Lastly,in this file,the code and functions used for all the above process are available clearly with line by line explaination with the help of comments.Using VS Code IDE the other half of this project i.e., Data retrieval and Visualisation is achieved.


Screenshots of Streamlit Application🏁:

   Step 1:
         The homepage of the streamlit application where the users can search for route names to get the visualisation of the bus details available for the route.

         ![Screenshot (138)](https://github.com/user-attachments/assets/ff37bdbe-4400-4ecb-8f6f-d54dfd45d17c)

   Step 2:
         After searching the routename.Below of the search bar you would get the bus details.In the side navigation bar you can see the filters that can be applied.

         ![Screenshot (139)](https://github.com/user-attachments/assets/00fd2cc5-42ee-42c2-90e3-dd240376a1c8)

   Step 3:
         The user can apply the filters and visualise.For example I have applied the price limit,star rating filter and bus_type that I prefer for a single instance and attached the Screenshot of how the resultant visualisation appears.The user can alter it as per his/her wish for any route available.

         1.You can see the bus_type filter that captured in the screenshot.

         ![Screenshot (140)](https://github.com/user-attachments/assets/0c86c8a1-93fc-44a0-9b86-a89b4fcc23f3)

         2.You can see the price range of the bus that have been retrieved and the star rating as per we have applied.This Screenshot has same functionality of above screenshot.The continuation of the Screenshot captured to show the visualisation of all filters applied successfully.

         ![Screenshot (141)](https://github.com/user-attachments/assets/75303d48-10cf-42e2-8c54-a6644b4b4166)




         


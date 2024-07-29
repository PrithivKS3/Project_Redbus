import mysql.connector
import streamlit as st           #Importing neccessary packages
import pandas as pd
import numpy as np
mydb = mysql.connector.connect( host="localhost",
                                user="root",            #Establishing Connection with the database
                                password="1818", 
                                database="demo" ) 
mycursor=mydb.cursor()#Creating a cursor


def fetch_buses(route_name):#Function to retrieve the details of available buses for the respective route name
    query = "SELECT * FROM bus_details WHERE bus_route = %s" 
    mycursor.execute(query, (route_name,))#executing the query for retrieval
    buses = mycursor.fetchall() 
    return buses


def filt_buses(buses,min_price,max_price,min_rating):#Function to apply the filters excluding bus_type alone.
    filtered_buses = [bus for bus in buses if (min_price <= bus[9] <= max_price) and (bus[8] >= min_rating)]
    return filtered_buses
def filter_buses(buses,min_price,max_price,min_rating,bus_types):#Function to apply all available filters.
    filtered_buses = [bus for bus in buses if (min_price <= bus[9] <= max_price) and (bus[8] >= min_rating) and (bus[4] in bus_types)]
    return filtered_buses
st.title("Bus Booking Application")#Title of the GUI application


st.sidebar.title("Filters")#Title of side navigation bar consisting of filters
min_price = st.sidebar.number_input("Minimum Price:", value=0,step=200) 
max_price = st.sidebar.number_input("Maximum Price:", value=5000,step=200)     #Creating Filters that can be applied by users of the application excluding bus_type alone 
min_rating = st.sidebar.number_input("Minimum Star Rating:", value=0.0, step=1.0, format="%.1f")#each route name has different set of bus types.So that filter is created in latter part of this code


mycursor.execute("SELECT * FROM bus_details")
df_bus=mycursor.fetchall()#Getting all the data from the database to create a dataframe
df=pd.DataFrame(df_bus,columns=["bus_id","bus_route","route_link","bus_names","bus_type","depart_time","duration","reach_time","star_rate","price","seats_available"])
route_name=st.selectbox("Select the Bus Route:", df["bus_route"].unique())#Creating a select box(Search box) consisting of all route names for which the bus service is provided         



if route_name:
    buses = fetch_buses(route_name)#calling the function to retrieve the bus_details associated to a specified route name.
    df2=pd.DataFrame(buses,columns=["bus_id","bus_route","route_link","bus_names","bus_type","depart_time","duration","reach_time","star_rate","price","seats_available"])
    bus_types=df2["bus_type"].unique()[1:]
    selected_bus_types=st.sidebar.multiselect("Select Bus Type:",bus_types)#Creating bus types filter that I specified earlier
    st.write(f"Available Buses for Route '{route_name}':") 

    if len(selected_bus_types)>0:
        filtered_buses=filter_buses(buses,min_price,max_price,min_rating,selected_bus_types)#if bus type filter is applied this function is called.
    else:
        filtered_buses=filt_buses(buses,min_price,max_price,min_rating)#if bus type filter is not applied then this function is called.
    
    df1=pd.DataFrame(filtered_buses,columns=["bus_id","bus_route","route_link","bus_names","bus_type","depart_time","duration","reach_time","star_rate","price","seats_available"])
    df1.drop('route_link',axis = 1, inplace = True)
    st.dataframe(df1) #Resultant Data frame to be displayed in the application
    bus_selection = st.selectbox("Select Bus ID to Book:", df1["bus_id"]) #Creating a select box for selecting the bus to be booked.
    
    if st.button("Book Bus"): #button to book the bus selected
        selected_bus = df1.loc[df1['bus_id']==bus_selection,:] 
        seat_no=np.random.randint(40) #seat no allocation
        st.write("Bus Booked!")
        st.write("Seat No= ",seat_no) 
        st.dataframe(selected_bus) #displaying selected bus details
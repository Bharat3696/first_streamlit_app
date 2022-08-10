import streamlit

streamlit.title('This is my sample code')


streamlit.header('Footaball')
streamlit.text(' 🐔 PSG Messi 30')
streamlit.text(':goat: MANU CR7 07')              
streamlit.text(':racehorse: PSG Neymar 10')               


streamlit.header(' Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("pick fruits:", list (my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


streamlit.multiselect("pick fruits:", list (my_fruit_list.index),['Apple','Banana'])
streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("pick fruits:", list (my_fruit_list.index),['Apple','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

import requests 

import snowflake.connetor
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

import snowflake.connetor
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


import os
import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
import sqlalchemy

# Faz a conexão com o banco de dados
def create_connection():
         return sqlalchemy.create_engine('')

def get_data():
    connection = create_connection()
    # Lista de consultas SQL (Adicione mais consultas conforme necessário)
    queries = {
        "tenants":"SELECT * FROM tenants",
        "items":"SELECT * FROM items WHERE tenant_id=1",
        "components_out":"SELECT * FROM components WHERE tenant_id=1 AND type='OUT'",
        "components_in": "SELECT * FROM components WHERE tenant_id=1 AND type='IN'",# não esquecer de colocar o filtro de type in novamente
        "collaborators":"SELECT * FROM collaborators WHERE tenant_id=1",
        "machines":"SELECT * FROM machines WHERE tenant_id=1",
        }

    dataframes = {}

    for table_name, query in queries.items():
        df = pd.read_sql(query, connection)
        dataframes[table_name] = df

 #   total_price_per_item = dataframes['components_in'].groupby('item_id')['unit_price'].sum()

    # Converter total_price_per_item em um DataFrame
  #  total_price_per_item_df = total_price_per_item.reset_index()
   # total_price_per_item_df.rename(columns={'unit_price': 'total_price'}, inplace=True)

    # Mesclar com o DataFrame components_in
    #dataframes['components_in'] = pd.merge(dataframes['components_in'], total_price_per_item_df, on='item_id', how='right')

    # Adicionar este DataFrame atualizado de volta ao dicionário queries
    #queries['components_in'] = dataframes['components_in']




    return dataframes['components_in']

# Código main do dashboard
def main():
    st.set_page_config(layout="wide")
    data = get_data()
    st.write(data)
if __name__ == "__main__":
    main()
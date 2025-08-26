# IMPORT LIBRARY
import streamlit as st

import pandas as pd
import matplotlib
import numpy as np
import os
import time
import plotly.express as px
import plotly.graph_objects as go
from datetime import timedelta, datetime
import math
import os
from dotenv import load_dotenv
import yaml
from yaml.loader import SafeLoader
from itertools import product

from io import BytesIO
import xlsxwriter
import datetime
from PIL import Image


st.markdown(f"<h1 style='text-align: center;'>WELCOME TO E-MONITORING PRODUKSI<br>DUNIA KIMIA JAYA</h1>", unsafe_allow_html=True)



# Halaman Awal

if "page" not in st.session_state:
    st.session_state["page"] = 0

if st.session_state["page"] == 0 :
    tombol_mulai = st.button(type="primary", label='Mulai')
    if tombol_mulai:
        st.session_state.page = 1
        st.rerun()


# Halaman 1

if st.session_state["page"] == 1:

    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 1</h3>", unsafe_allow_html=True)


    with st.form(key='form_page_1', clear_on_submit=False):
        nama_operator = st.text_input("Nama Operator", key="nama_operator")


        col_1, col_2, col_3 = st.columns([1, 1, 1])

        with col_1:
            machine_options = ["E01", "E02", "E03", "E05", "E06"]
            machine_selected_options = st.radio('Mesin', machine_options, key="machine_selected_options")

        with col_2:
            shift_options = ["1", "2", "3"]
            shift_selected_options = st.radio('Shift', shift_options, key="shift_selected_options")

        with col_3:
            group_options = ["Kuning", "Hijau", "Merah", "Biru"]
            group_selected_options = st.radio('Grup', group_options, key="group_selected_options")


        col_4, col_5 = st.columns([1, 1])

        with col_4:
            date_input = st.date_input("Tanggal Pengisian")

        with col_5 :
            time_input = st.time_input("Jam Pengisian",step=3600)

        nama_produk = st.text_input("Nama Produk (Tuliskan angka belakang saja, CONTOH : Untuk produk ASITHYLEN P White 9440 A, tuliskan : 9440 A", key="nama_produk")

        kondisi_mesin_options = ["Running", "Stop"]
        kondisi_mesin_selected_options = st.pills('Kondisi Mesin', options=kondisi_mesin_options, key="kondisi_mesin_selected_options")


        can_submit = True

        if not nama_operator:
            st.warning('Isi bagian "Nama Operator"!')
            can_submit = False
        
        if not machine_selected_options:
            st.warning('Isi bagian "Mesin"!')
            can_submit = False

        if not shift_selected_options:
            st.warning('Isi bagian "Shift"!')
            can_submit = False

        if not group_selected_options:
            st.warning('Isi bagian "Grup"!')
            can_submit = False

        if not date_input:
            st.warning('Isi bagian "Tanggal Pengisian"!')
            can_submit = False

        if not time_input:
            st.warning('Isi bagian "Jam Pengisian"!')
            can_submit = False

        if not nama_produk:
            st.warning('Isi bagian "Nama Produk"!')
            can_submit = False

        if not kondisi_mesin_selected_options:
            st.warning('Isi bagian "Kondisi Mesin"!')
            can_submit = False

        submit_button_1_1 = st.form_submit_button(label='Submit')

        if submit_button_1_1:

            if can_submit == False:
                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
            else:
                nama_kolom_page_1 = {
                    "Nama Operator": [], 
                    "Mesin": [], 
                    "Shift": [], 
                    "Tanggal Pengisian": [], 
                    "Jam Pengisian": [],
                    "Nama Produk": [],
                    "Kondisi Mesin": []
                    }
                df_data_page_1 = pd.DataFrame(nama_kolom_page_1)

                new_row_page_1 = pd.DataFrame(
                {"Nama Operator": [nama_operator],
                "Mesin": [machine_selected_options],
                "Shift": [shift_selected_options],
                "Tanggal Pengisian": [date_input],
                "Jam Pengisian": [time_input],
                "Nama Produk": [nama_produk],
                "Kondisi Mesin": [kondisi_mesin_selected_options]
                })
                df_data_page_1 = pd.concat([df_data_page_1, new_row_page_1]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_1)
                st.session_state.df_data_page_1 = df_data_page_1
                



    submit_button_1_2 = st.button(type="primary", label='Next Page')
    if submit_button_1_2:
        if "df_data_page_1" not in st.session_state:
            st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit"sebelum menekan tombol "Next Page"!')
        else:
            st.session_state.page = 2
            st.rerun()
                


if st.session_state["page"] == 2:
    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 2 : MESIN FEEDER</h3>", unsafe_allow_html=True)
    # st.markdown(f"<h3 style='text-align: center;'>MESIN FEEDER<br></h3>", unsafe_allow_html=True)
    
    # st.write(df_all_data)



    with st.form(key='form_page_2'):
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Output Feeder 1 - F1 (kg/jam)</h5>", unsafe_allow_html=True)

            col_2_1, col_2_2 = st.columns([1, 1])
            with col_2_1:
                set_output_feeder_1 = st.number_input("", value=None, placeholder="SET POINT", key="set_output_feeder_1")


            with col_2_2 :
                actual_output_feeder_1 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_output_feeder_1")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Output Feeder 2 - F2 (kg/jam)</h5>", unsafe_allow_html=True)

            col_2_3, col_2_4 = st.columns([1, 1])
            with col_2_3:
                set_output_feeder_2 = st.number_input("", value=None, placeholder="SET POINT", key="set_output_feeder_2")

            with col_2_4 :
                actual_output_feeder_2 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_output_feeder_2")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Output Feeder 3 - F3 (kg/jam)</h5>", unsafe_allow_html=True)

            col_2_5, col_2_6 = st.columns([1, 1])
            with col_2_5:
                set_output_feeder_3 = st.number_input("", value=None, placeholder="SET POINT", key="set_output_feeder_3")


            with col_2_6 :
                actual_output_feeder_3 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_output_feeder_3")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Output Feeder 4 - F4 (kg/jam)</h5>", unsafe_allow_html=True)

            col_2_7, col_2_8 = st.columns([1, 1])
            with col_2_7:
                set_output_feeder_4 = st.number_input("", value=None, placeholder="SET POINT", key="set_output_feeder_4")

            with col_2_8 :
                actual_output_feeder_4 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_output_feeder_4")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Output Feeder Jotam S50 (kg/jam)</h5>", unsafe_allow_html=True)

            col_2_9, col_2_10 = st.columns([1, 1])
            with col_2_9:
                set_output_feeder_jotam_s50 = st.number_input("", value=None, placeholder="SET POINT", key="set_output_feeder_jotam_s50")

            with col_2_10 :
                actual_output_feeder_jotam_s50 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_output_feeder_jotam_s50")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Output Feeder Jotam S90 - Resin (kg/jam)</h5>", unsafe_allow_html=True)

            col_2_11, col_2_12 = st.columns([1, 1])
            with col_2_11:
                set_output_feeder_jotam_s90_resin = st.number_input("", value=None, placeholder="SET POINT", key="set_output_feeder_jotam_s90_resin")

            with col_2_12 :
                actual_output_feeder_jotam_s90_resin = st.number_input("", value=None, placeholder="AKTUAL", key="actual_output_feeder_jotam_s90_resin")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Output Feeder Jotam S90 - Aditif (kg/jam)</h5>", unsafe_allow_html=True)

            col_2_13, col_2_14 = st.columns([1, 1])
            with col_2_13:
                set_output_feeder_jotam_s90_aditif = st.number_input("", value=None, placeholder="SET POINT", key="set_output_feeder_jotam_s90_aditif")

            with col_2_14 :
                actual_output_feeder_jotam_s90_aditif = st.number_input("", value=None, placeholder="AKTUAL", key="actual_output_feeder_jotam_s90_aditif")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Output Liquid Feeder (kg/jam)</h5>", unsafe_allow_html=True)

            col_2_15, col_2_16 = st.columns([1, 1])
            with col_2_15:
                set_output_liquid_feeder = st.number_input("", value=None, placeholder="SET POINT", key="set_output_liquid_feeder")

            with col_2_16 :
                actual_output_liquid_feeder = st.number_input("", value=None, placeholder="AKTUAL", key="actual_output_liquid_feeder")


            tekanan_liquid_feeder = st.number_input("Tekanan liquid feeder", value=None, placeholder="", key="tekanan_liquid_feeder")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Main Feeder / Feeder 1</h5>", unsafe_allow_html=True)

            col_2_17, col_2_18 = st.columns([1, 1])
            with col_2_17:
                rpm_main_feeder = st.number_input("RPM main feeder", value=None, placeholder="", key="rpm_main_feeder")

            with col_2_18 :
                ampere_main_feeder = st.number_input("Ampere main feeder", value=None, placeholder="", key="ampere_main_feeder")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Feeder Rework</h5>", unsafe_allow_html=True)
            rpm_feeder_rework = st.number_input("RPM feeder rework", value=None, placeholder="", key="rpm_feeder_rework")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Side Feeder</h5>", unsafe_allow_html=True)
            rpm_side_feeder = st.number_input("RPM side feeder", value=None, placeholder="", key="rpm_side_feeder")
        

        can_submit = True

        if not set_output_feeder_1:
            st.warning('Isi bagian "Set Point Output Feeder 1 - F1"!')
            can_submit = False
        
        if not actual_output_feeder_1:
            st.warning('Isi bagian "Aktual Output Feeder 1 - F1"!')
            can_submit = False

        if not set_output_feeder_2:
            st.warning('Isi bagian "Set Point Output Feeder 2 - F2"!')
            can_submit = False

        if not actual_output_feeder_2:
            st.warning('Isi bagian "Aktual Output Feeder 2 - F2"!')
            can_submit = False

        if not set_output_feeder_3:
            st.warning('Isi bagian "Set Point Output Feeder 3 - F3"!')
            can_submit = False

        if not actual_output_feeder_3:
            st.warning('Isi bagian "Aktual Output Feeder 3 - F3"!')
            can_submit = False

        if not set_output_feeder_4:
            st.warning('Isi bagian "Set Point Output Feeder 4 - F4"!')
            can_submit = False

        if not actual_output_feeder_4:
            st.warning('Isi bagian "Aktual Output Feeder 4 - F4"!')
            can_submit = False

        if not set_output_feeder_jotam_s50:
            st.warning('Isi bagian "Set Point Output Feeder Jotam S50"!')
            can_submit = False

        if not actual_output_feeder_jotam_s50:
            st.warning('Isi bagian "Aktual Output Feeder Jotam S50"!')
            can_submit = False

        if not set_output_feeder_jotam_s90_resin:
            st.warning('Isi bagian "Set Point Output Feeder Jotam S90 Resin"!')
            can_submit = False

        if not actual_output_feeder_jotam_s90_resin:
            st.warning('Isi bagian "Aktual Output Feeder Jotam S90 Resin"!')
            can_submit = False

        if not set_output_feeder_jotam_s90_aditif:
            st.warning('Isi bagian "Set Point Output Feeder Jotam S90 Aditif"!')
            can_submit = False

        if not actual_output_feeder_jotam_s90_aditif:
            st.warning('Isi bagian "Aktual Output Feeder Jotam S90 Aditif"!')
            can_submit = False

        if not set_output_liquid_feeder:
            st.warning('Isi bagian "Set Point Output Liquid Feeder"!')
            can_submit = False

        if not actual_output_liquid_feeder:
            st.warning('Isi bagian "Aktual Output Liquid Feeder"!')
            can_submit = False

        if not tekanan_liquid_feeder:
            st.warning('Isi bagian "Tekanan Liquid Feeder"!')
            can_submit = False

        if not rpm_main_feeder:
            st.warning('Isi bagian "RPM main feeder"!')
            can_submit = False

        if not ampere_main_feeder:
            st.warning('Isi bagian "Ampere main feeder"!')
            can_submit = False

        if not rpm_feeder_rework:
            st.warning('Isi bagian "RPM Feeder Rework"!')
            can_submit = False

        if not rpm_side_feeder:
            st.warning('Isi bagian "RPM Side Feeder"!')
            can_submit = False


        submit_button_2_1 = st.form_submit_button(label='Submit')

        if submit_button_2_1:

            if can_submit == False:
                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
            else:
                nama_kolom_page_2 = {
                    "Set Point Output Feeder 1 - F1 (kg/jam)": [], 
                    "Aktual Output Feeder 1 - F1 (kg/jam)": [], 
                    "Set Point Output Feeder 2 - F2 (kg/jam)": [], 
                    "Aktual Output Feeder 2 - F2 (kg/jam)": [], 
                    "Set Point Output Feeder 3 - F3 (kg/jam)": [], 
                    "Aktual Output Feeder 3 - F3 (kg/jam)": [], 
                    "Set Point Output Feeder 4 - F4 (kg/jam)": [], 
                    "Aktual Output Feeder 4 - F4 (kg/jam)": [], 
                    "Set Point Output Feeder Jotam S50 (kg/jam)": [], 
                    "Aktual Output Feeder Jotam S50 (kg/jam)": [], 
                    "Set Point Output Feeder Jotam S90 - Resin (kg/jam)": [], 
                    "Aktual Output Feeder Jotam S90 - Resin (kg/jam)": [], 
                    "Set Point Output Feeder Jotam S90 - Aditif (kg/jam)": [], 
                    "Aktual Output Feeder Jotam S90 - Aditif (kg/jam)": [], 
                    "Set Point Output Liquid Feeder (kg/jam)": [], 
                    "Aktual Output Liquid Feeder (kg/jam)": [], 
                    "Tekanan Liquid Feeder": [], 
                    "RPM Main Feeder": [], 
                    "Ampere Main Feeder": [], 
                    "RPM Feeder Rework": [], 
                    "RPM Side Feeder": [] 
                    }
                df_data_page_2 = pd.DataFrame(nama_kolom_page_2)

                new_row_page_2 = pd.DataFrame({
                    "Set Point Output Feeder 1 - F1 (kg/jam)": [set_output_feeder_1], 
                    "Aktual Output Feeder 1 - F1 (kg/jam)": [actual_output_feeder_1], 
                    "Set Point Output Feeder 2 - F2 (kg/jam)": [set_output_feeder_2], 
                    "Aktual Output Feeder 2 - F2 (kg/jam)": [actual_output_feeder_2], 
                    "Set Point Output Feeder 3 - F3 (kg/jam)": [set_output_feeder_3], 
                    "Aktual Output Feeder 3 - F3 (kg/jam)": [actual_output_feeder_3], 
                    "Set Point Output Feeder 4 - F4 (kg/jam)": [set_output_feeder_4], 
                    "Aktual Output Feeder 4 - F4 (kg/jam)": [actual_output_feeder_4], 
                    "Set Point Output Feeder Jotam S50 (kg/jam)": [set_output_feeder_jotam_s50], 
                    "Aktual Output Feeder Jotam S50 (kg/jam)": [actual_output_feeder_jotam_s50], 
                    "Set Point Output Feeder Jotam S90 - Resin (kg/jam)": [set_output_feeder_jotam_s90_resin], 
                    "Aktual Output Feeder Jotam S90 - Resin (kg/jam)": [actual_output_feeder_jotam_s90_resin], 
                    "Set Point Output Feeder Jotam S90 - Aditif (kg/jam)": [set_output_feeder_jotam_s90_aditif], 
                    "Aktual Output Feeder Jotam S90 - Aditif (kg/jam)": [actual_output_feeder_jotam_s90_aditif], 
                    "Set Point Output Liquid Feeder (kg/jam)": [set_output_liquid_feeder], 
                    "Aktual Output Liquid Feeder (kg/jam)": [actual_output_liquid_feeder], 
                    "Tekanan Liquid Feeder": [tekanan_liquid_feeder], 
                    "RPM Main Feeder": [rpm_main_feeder], 
                    "Ampere Main Feeder": [ampere_main_feeder], 
                    "RPM Feeder Rework": [rpm_feeder_rework], 
                    "RPM Side Feeder": [rpm_side_feeder] 
                })
                df_data_page_2 = pd.concat([df_data_page_2, new_row_page_2]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_2)
                st.session_state.df_data_page_2 = df_data_page_2
    
    submit_button_2_2 = st.button(type="primary", label='Next Page')
    if submit_button_2_2:
        if "df_data_page_2" not in st.session_state:
            st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit" sebelum menekan tombol "Next Page"!')
        else:
            st.session_state.page = 3
            st.rerun()


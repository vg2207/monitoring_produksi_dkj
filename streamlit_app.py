# IMPORT LIBRARY
import streamlit as st

import pandas as pd
import numpy as np
import os
import xlsxwriter



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
                

#Halaman 2
if st.session_state["page"] == 2:


    df_data_page_1 = st.session_state.df_data_page_1
    # st.write(df_data_page_1["Mesin"][0])

    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 2 : MESIN FEEDER</h3>", unsafe_allow_html=True)
    # st.markdown(f"<h3 style='text-align: center;'>MESIN FEEDER<br></h3>", unsafe_allow_html=True)
    
    # st.write(df_all_data)



    with st.form(key='form_page_2'):
        if df_data_page_1["Mesin"][0] == 'E06':
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

        else :
            pass

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
            
            if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
                with col_2_17:
                    rpm_main_feeder = st.number_input("RPM main feeder", value=None, placeholder="", key="rpm_main_feeder")
            else :
                pass

            with col_2_18 :
                ampere_main_feeder = st.number_input("Ampere main feeder", value=None, placeholder="", key="ampere_main_feeder")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Feeder Rework</h5>", unsafe_allow_html=True)
            rpm_feeder_rework = st.number_input("RPM feeder rework", value=None, placeholder="", key="rpm_feeder_rework")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Side Feeder</h5>", unsafe_allow_html=True)
            rpm_side_feeder = st.number_input("RPM side feeder", value=None, placeholder="", key="rpm_side_feeder")
        

        can_submit = True
        
        if df_data_page_1["Mesin"][0] == 'E06':
            if set_output_feeder_1 is None:
                st.warning('Isi bagian "Set Point Output Feeder 1 - F1"!')
                can_submit = False
                
            if actual_output_feeder_1 is None:
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
        
        else:
            pass

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
            st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit"sebelum menekan tombol "Next Page"!')
        else:
            st.session_state.page = 3
            st.rerun()

#Halaman 3
if st.session_state["page"] == 3:
    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 3 : EXTRUDER</h3>", unsafe_allow_html=True)
    # st.markdown(f"<h3 style='text-align: center;'>EXTRUDER<br></h3>", unsafe_allow_html=True)
    # st.write(df_all_data)



    with st.form(key='form_page_3'):
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Output Mesin (kg/jam)</h5>", unsafe_allow_html=True)

            col_3_1, col_3_2 = st.columns([1, 1])
            with col_3_1:
                set_output_mesin_extruder = st.number_input("", value=None, placeholder="SET POINT", key="set_output_mesin_extruder")


            with col_3_2 :
                actual_output_mesin_extruder = st.number_input("", value=None, placeholder="AKTUAL", key="actual_output_mesin_extruder")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Ampere & RPM Extruder</h5>", unsafe_allow_html=True)

            col_3_3, col_3_4 = st.columns([1, 1])
            with col_3_3:
                set_ampere_RPM_extruder = st.number_input("", value=None, placeholder="AMPERE/TORSI", key="set_ampere_RPM_extruder")

            with col_3_4 :
                actual_ampere_RPM_extruder = st.number_input("", value=None, placeholder="RPM", key="actual_ampere_RPM_extruder")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>SEI (KWh/kg)</h5>", unsafe_allow_html=True)
            specific_energy_index = st.text_input("", key="specific_energy_index")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Melt Temperature - Pressure Ekstruder</h5>", unsafe_allow_html=True)

            col_3_5, col_3_6 = st.columns([1, 1])
            with col_3_5:
                set_melt_temperature_pressure = st.number_input("", value=None, placeholder="MELT TEMPERATURE", key="set_melt_temperature_pressure")

            with col_3_6 :
                actual_melt_temperature_pressure = st.number_input("", value=None, placeholder="MELT PRESSURE", key="actual_melt_temperature_pressure")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Kondisi Valve Pendingin Barrel Zone 1</h5>", unsafe_allow_html=True)
            valve_condition_options = ["OPEN", "CLOSE"]
            valve_condition_options = st.radio('', valve_condition_options, key="valve_condition_options")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 1</h5>", unsafe_allow_html=True)

            col_3_7, col_3_8 = st.columns([1, 1])
            with col_3_7:
                set_temperature_zone_1 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_1")

            with col_3_8 :
                actual_temperature_zone_1 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_1")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 2</h5>", unsafe_allow_html=True)

            col_3_9, col_3_10 = st.columns([1, 1])
            with col_3_9:
                set_temperature_zone_2 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_2")

            with col_3_10 :
                actual_temperature_zone_2 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_2")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 3</h5>", unsafe_allow_html=True)

            col_3_11, col_3_12 = st.columns([1, 1])
            with col_3_11:
                set_temperature_zone_3 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_3")

            with col_3_12 :
                actual_temperature_zone_3 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_3")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 4</h5>", unsafe_allow_html=True)

            col_3_13, col_3_14 = st.columns([1, 1])
            with col_3_13:
                set_temperature_zone_4 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_4")

            with col_3_14 :
                actual_temperature_zone_4 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_4")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 5</h5>", unsafe_allow_html=True)

            col_3_15, col_3_16 = st.columns([1, 1])
            with col_3_15:
                set_temperature_zone_5 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_5")

            with col_3_16 :
                actual_temperature_zone_5 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_5")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 6</h5>", unsafe_allow_html=True)

            col_3_17, col_3_18 = st.columns([1, 1])
            with col_3_17:
                set_temperature_zone_6 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_6")

            with col_3_18 :
                actual_temperature_zone_6 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_6")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 7</h5>", unsafe_allow_html=True)

            col_3_19, col_3_20 = st.columns([1, 1])
            with col_3_19:
                set_temperature_zone_7 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_7")

            with col_3_20 :
                actual_temperature_zone_7 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_7")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 8</h5>", unsafe_allow_html=True)

            col_3_21, col_3_22 = st.columns([1, 1])
            with col_3_21:
                set_temperature_zone_8 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_8")

            with col_3_22 :
                actual_temperature_zone_8 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_8")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 9</h5>", unsafe_allow_html=True)

            col_3_23, col_3_24 = st.columns([1, 1])
            with col_3_23:
                set_temperature_zone_9 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_9")

            with col_3_24 :
                actual_temperature_zone_9 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_9")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 10</h5>", unsafe_allow_html=True)

            col_3_25, col_3_26 = st.columns([1, 1])
            with col_3_25:
                set_temperature_zone_10 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_10")

            with col_3_26 :
                actual_temperature_zone_10 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_10")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 11</h5>", unsafe_allow_html=True)

            col_3_27, col_3_28 = st.columns([1, 1])
            with col_3_27:
                set_temperature_zone_11 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_11")

            with col_3_28 :
                actual_temperature_zone_11 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_11")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 12</h5>", unsafe_allow_html=True)

            col_3_29, col_3_30 = st.columns([1, 1])
            with col_3_29:
                set_temperature_zone_12 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_zone_12")

            with col_3_30 :
                actual_temperature_zone_12 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_zone_12")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature 8.0</h5>", unsafe_allow_html=True)

            col_3_31, col_3_32 = st.columns([1, 1])
            with col_3_31:
                set_temperature_8 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_8")

            with col_3_32 :
                actual_temperature_8 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_8")
        
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Input Screen Changer</h5>", unsafe_allow_html=True)

            col_3_33, col_3_34 = st.columns([1, 1])
            with col_3_33:
                set_temperature_input_screen_changer = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_input_screen_changer")

            with col_3_34 :
                actual_temperature_input_screen_changer = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_input_screen_changer")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature TSW / Screen Changer 1</h5>", unsafe_allow_html=True)

            col_3_35, col_3_36 = st.columns([1, 1])
            with col_3_35:
                set_temperature_TSW_screen_changer_1 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_TSW_screen_changer_1")

            with col_3_36 :
                actual_temperature_TSW_screen_changer_1 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_TSW_screen_changer_1")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Screen Changer 2</h5>", unsafe_allow_html=True)

            col_3_37, col_3_38 = st.columns([1, 1])
            with col_3_37:
                set_temperature_screen_changer_2 = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_screen_changer_2")

            with col_3_38 :
                actual_temperature_screen_changer_2 = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_screen_changer_2")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Cooling Barrell Mesin</h5>", unsafe_allow_html=True)

            col_3_39, col_3_40 = st.columns([1, 1])
            with col_3_39:
                temperature_cooling_barrel_mesin = st.number_input("", value=None, placeholder="TEMPERATURE", key="temperature_cooling_barrel_mesin")

            with col_3_40 :
                pressure_cooling_barrel_mesin = st.number_input("", value=None, placeholder="TEKANAN AIR", key="pressure_cooling_barrel_mesin")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Parameter Gearbox Mesin</h5>", unsafe_allow_html=True)

            col_3_41, col_3_42 = st.columns([1, 1])
            with col_3_41:
                temperature_gearbox_oil = st.number_input("", value=None, placeholder="TEMPERATURE OLI GEARBOX", key="temperature_gearbox_oil")

            with col_3_42 :
                pressure_gearbox_oil = st.number_input("", value=None, placeholder="TEKANAN OLI GEARBOX", key="pressure_gearbox_oil")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Parameter Vacuum System</h5>", unsafe_allow_html=True)

            col_3_43, col_3_44 = st.columns([1, 1])
            with col_3_43:
                vacuum_bar_value = st.number_input("", value=None, placeholder="VACUUM BAR", key="vacuum_bar_value")

            with col_3_44 :
                pressure_vacuum_system_water = st.number_input("", value=None, placeholder="TEKANAN AIR VACUUM SYSTEM", key="pressure_vacuum_system_water")

        can_submit = True

        if not set_output_mesin_extruder:
            st.warning('Isi bagian "Set Point Output Mesin"!')
            can_submit = False
        
        if not actual_output_mesin_extruder:
            st.warning('Isi bagian "Aktual Output Mesin"!')
            can_submit = False

        if not set_ampere_RPM_extruder:
            st.warning('Isi bagian "Set Point Ampere & RPM Extruder"!')
            can_submit = False

        if not actual_ampere_RPM_extruder:
            st.warning('Isi bagian "Aktual Ampere & RPM Extruder"!')
            can_submit = False

        if not specific_energy_index:
            st.warning('Isi bagian "SEI"!')
            can_submit = False

        if not set_melt_temperature_pressure:
            st.warning('Isi bagian "Melt Temperature Extruder"!')
            can_submit = False

        if not set_melt_temperature_pressure:
            st.warning('Isi bagian "Melt Pressure Extruder"!')
            can_submit = False

        if not valve_condition_options:
            st.warning('Isi bagian "Kondisi Valve Pendingin Barrel Zone 1"!')
            can_submit = False

        if not set_temperature_zone_1:
            st.warning('Isi bagian "Set Point Temperature Zone 1"!')
            can_submit = False

        if not actual_temperature_zone_1:
            st.warning('Isi bagian "Aktual Temperature Zone 1"!')
            can_submit = False

        if not set_temperature_zone_2:
            st.warning('Isi bagian "Set Point Temperature Zone 2"!')
            can_submit = False

        if not actual_temperature_zone_2:
            st.warning('Isi bagian "Aktual Temperature Zone 2"!')
            can_submit = False

        if not set_temperature_zone_3:
            st.warning('Isi bagian "Set Point Temperature Zone 3"!')
            can_submit = False

        if not actual_temperature_zone_3:
            st.warning('Isi bagian "Aktual Temperature Zone 3"!')
            can_submit = False

        if not set_temperature_zone_4:
            st.warning('Isi bagian "Set Point Temperature Zone 4"!')
            can_submit = False

        if not actual_temperature_zone_4:
            st.warning('Isi bagian "Aktual Temperature Zone 4"!')
            can_submit = False

        if not set_temperature_zone_5:
            st.warning('Isi bagian "Set Point Temperature Zone 5"!')
            can_submit = False

        if not actual_temperature_zone_5:
            st.warning('Isi bagian "Aktual Temperature Zone 5"!')
            can_submit = False

        if not set_temperature_zone_6:
            st.warning('Isi bagian "Set Point Temperature Zone 6"!')
            can_submit = False

        if not actual_temperature_zone_6:
            st.warning('Isi bagian "Aktual Temperature Zone 6"!')
            can_submit = False

        if not set_temperature_zone_7:
            st.warning('Isi bagian "Set Point Temperature Zone 7"!')
            can_submit = False
        
        if not actual_temperature_zone_7:
            st.warning('Isi bagian "Aktual Temperature Zone 7"!')
            can_submit = False

        if not set_temperature_zone_8:
            st.warning('Isi bagian "Set Point Temperature Zone 8"!')
            can_submit = False

        if not actual_temperature_zone_8:
            st.warning('Isi bagian "Aktual Temperature Zone 8"!')
            can_submit = False

        if not set_temperature_zone_9:
            st.warning('Isi bagian "Set Point Temperature Zone 9"!')
            can_submit = False

        if not actual_temperature_zone_9:
            st.warning('Isi bagian "Aktual Temperature Zone 9"!')
            can_submit = False

        if not set_temperature_zone_10:
            st.warning('Isi bagian "Set Point Temperature Zone 10"!')
            can_submit = False
        
        if not actual_temperature_zone_10:
            st.warning('Isi bagian "Aktual Temperature Zone 10"!')
            can_submit = False

        if not actual_temperature_zone_11:
            st.warning('Isi bagian "Aktual Temperature Zone 11"!')
            can_submit = False

        if not set_temperature_zone_12:
            st.warning('Isi bagian "Set Point Temperature Zone 12"!')
            can_submit = False

        if not actual_temperature_zone_12:
            st.warning('Isi bagian "Aktual Temperature Zone 12"!')
            can_submit = False

        if not set_temperature_8:
            st.warning('Isi bagian "Set Point Temperature 8.0"!')
            can_submit = False

        if not actual_temperature_8:
            st.warning('Isi bagian "Aktual Temperature 8.0"!')
            can_submit = False

        if not set_temperature_input_screen_changer:
            st.warning('Isi bagian "Set Point Temperature Input Screen Changer"!')
            can_submit = False

        if not actual_temperature_input_screen_changer:
            st.warning('Isi bagian "Aktual Temperature Input Screen Changer"!')
            can_submit = False

        if not set_temperature_TSW_screen_changer_1:
            st.warning('Isi bagian "Set Point Temperature TSW / Screen Changer 1"!')
            can_submit = False

        if not actual_temperature_TSW_screen_changer_1:
            st.warning('Isi bagian "Aktual Temperature TSW / Screen Changer 1"!')
            can_submit = False
        
        if not set_temperature_screen_changer_2:
            st.warning('Isi bagian "Set Point Temperature Screen Changer 2"!')
            can_submit = False

        if not actual_temperature_screen_changer_2:
            st.warning('Isi bagian "Aktual Temperature Screen Changer 2"!')
            can_submit = False

        if not temperature_cooling_barrel_mesin:
            st.warning('Isi bagian "Temperature Air Cooling Barrel Mesin"!')
            can_submit = False

        if not pressure_cooling_barrel_mesin:
            st.warning('Isi bagian "Tekanan Air Cooling Barrel Mesin"!')
            can_submit = False

        if not temperature_gearbox_oil:
            st.warning('Isi bagian "Temperature Oli Gearbox"!')
            can_submit = False

        if not pressure_gearbox_oil:
            st.warning('Isi bagian "Tekanan Oli Gearbox"!')
            can_submit = False

        if not vacuum_bar_value:
            st.warning('Isi bagian "Vacuum Bar"!')
            can_submit = False
        
        if not pressure_vacuum_system_water:
            st.warning('Isi bagian "Tekanan Air Vacuum System"!')
            can_submit = False

        submit_button_3_1 = st.form_submit_button(label='Submit')

        if submit_button_3_1:

            if can_submit == False:
                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
            else:
                nama_kolom_page_3 = {
                    "Set Point Output Mesin": [], 
                    "Aktual Output Mesin": [], 
                    "Set Point Ampere & RPM Extruder": [], 
                    "Aktual Ampere & RPM Extruder": [], 
                    "SEI": [], 
                    "Melt Temperature Extruder": [], 
                    "Melt Pressure Extruder": [], 
                    "Kondisi Valve Pendingin Barrel Zone 1": [], 
                    "Set Point Temperature Zone 1": [], 
                    "Aktual Temperature Zone 1": [],
                    "Set Point Temperature Zone 2": [], 
                    "Aktual Temperature Zone 2": [],
                    "Set Point Temperature Zone 3": [], 
                    "Aktual Temperature Zone 3": [], 
                    "Set Point Temperature Zone 4": [], 
                    "Aktual Temperature Zone 4": [],
                    "Set Point Temperature Zone 5": [], 
                    "Aktual Temperature Zone 5": [],
                    "Set Point Temperature Zone 6": [], 
                    "Aktual Temperature Zone 6": [],
                    "Set Point Temperature Zone 7": [], 
                    "Aktual Temperature Zone 7": [],
                    "Set Point Temperature Zone 8": [], 
                    "Aktual Temperature Zone 8": [],
                    "Set Point Temperature Zone 9": [], 
                    "Aktual Temperature Zone 9": [],
                    "Set Point Temperature Zone 10": [], 
                    "Aktual Temperature Zone 10": [],
                    "Set Point Temperature Zone 11": [], 
                    "Aktual Temperature Zone 11": [],
                    "Set Point Temperature Zone 12": [], 
                    "Aktual Temperature Zone 12": [],
                    "Set Point Temperature 8.0": [], 
                    "Aktual Temperature 8.0": [], 
                    "Set Point Temperature Input Screen Changer": [], 
                    "Aktual Temperature Input Screen Changer": [], 
                    "Set Point Temperature TSW / Screen Changer 1": [], 
                    "Aktual Temperature TSW / Screen Changer 1": [], 
                    "Set Point Temperature Screen Changer 2": [], 
                    "Aktual Temperature Screen Changer 2": [], 
                    "Temperature Air Cooling Barrel Mesin": [], 
                    "Tekanan Air Cooling Barrel Mesin": [], 
                    "Temperature Oli Gearbox": [] ,
                    "Vacuum Bar": [],
                    "Tekanan Air Vacuum System":[]
                    }
                df_data_page_3 = pd.DataFrame(nama_kolom_page_3)

                new_row_page_3 = pd.DataFrame({
                    "Set Point Output Mesin": [set_output_mesin_extruder], 
                    "Aktual Output Mesin": [actual_output_mesin_extruder], 
                    "Set Point Ampere & RPM Extruder": [set_ampere_RPM_extruder], 
                    "Aktual Ampere & RPM Extruder": [actual_ampere_RPM_extruder], 
                    "SEI": [specific_energy_index], 
                    "Melt Temperature Extruder": [set_melt_temperature_pressure], 
                    "Melt Pressure Extruder": [set_melt_temperature_pressure], 
                    "Kondisi Valve Pendingin Barrel Zone 1": [valve_condition_options], 
                    "Set Point Temperature Zone 1": [set_temperature_zone_1], 
                    "Aktual Temperature Zone 1": [actual_temperature_zone_1],
                    "Set Point Temperature Zone 2": [set_temperature_zone_2], 
                    "Aktual Temperature Zone 2": [actual_temperature_zone_2],
                    "Set Point Temperature Zone 3": [set_temperature_zone_3], 
                    "Aktual Temperature Zone 3": [actual_temperature_zone_3], 
                    "Set Point Temperature Zone 4": [set_temperature_zone_4], 
                    "Aktual Temperature Zone 4": [actual_temperature_zone_4],
                    "Set Point Temperature Zone 5": [set_temperature_zone_5], 
                    "Aktual Temperature Zone 5": [actual_temperature_zone_5],
                    "Set Point Temperature Zone 6": [set_temperature_zone_6], 
                    "Aktual Temperature Zone 6": [actual_temperature_zone_6],
                    "Set Point Temperature Zone 7": [set_temperature_zone_7], 
                    "Aktual Temperature Zone 7": [actual_temperature_zone_7],
                    "Set Point Temperature Zone 8": [set_temperature_zone_8], 
                    "Aktual Temperature Zone 8": [actual_temperature_zone_8],
                    "Set Point Temperature Zone 9": [set_temperature_zone_9], 
                    "Aktual Temperature Zone 9": [actual_temperature_zone_9],
                    "Set Point Temperature Zone 10": [set_temperature_zone_10], 
                    "Aktual Temperature Zone 10": [actual_temperature_zone_10],
                    "Set Point Temperature Zone 11": [set_temperature_zone_11], 
                    "Aktual Temperature Zone 11": [actual_temperature_zone_11],
                    "Set Point Temperature Zone 12": [set_temperature_zone_12], 
                    "Aktual Temperature Zone 12": [actual_temperature_zone_12],
                    "Set Point Temperature 8.0": [set_temperature_8], 
                    "Aktual Temperature 8.0": [actual_temperature_8], 
                    "Set Point Temperature Input Screen Changer": [set_temperature_input_screen_changer], 
                    "Aktual Temperature Input Screen Changer": [actual_temperature_input_screen_changer], 
                    "Set Point Temperature TSW / Screen Changer 1": [set_temperature_TSW_screen_changer_1], 
                    "Aktual Temperature TSW / Screen Changer 1": [actual_temperature_TSW_screen_changer_1], 
                    "Set Point Temperature Screen Changer 2": [set_temperature_screen_changer_2], 
                    "Aktual Temperature Screen Changer 2": [actual_temperature_screen_changer_2], 
                    "Temperature Air Cooling Barrel Mesin": [temperature_cooling_barrel_mesin], 
                    "Tekanan Air Cooling Barrel Mesin": [pressure_cooling_barrel_mesin], 
                    "Temperature Oli Gearbox": [temperature_gearbox_oil] ,
                    "Vacuum Bar": [vacuum_bar_value],
                    "Tekanan Air Vacuum System":[pressure_vacuum_system_water] 
                })
                df_data_page_3 = pd.concat([df_data_page_3, new_row_page_3]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_3)
                st.session_state.df_data_page_3 = df_data_page_3
    
    submit_button_2_3 = st.button(type="primary", label='Next Page')
    if submit_button_2_3:
        if "df_data_page_3" not in st.session_state:
            st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit"sebelum menekan tombol "Next Page"!')
        else:
            st.session_state.page = 4
            st.rerun()

#Halaman 4
if st.session_state["page"] == 4:
    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 4 : UWP-PELLETIZER</h3>", unsafe_allow_html=True)
    # st.markdown(f"<h3 style='text-align: center;'>EXTRUDER<br></h3>", unsafe_allow_html=True)
    # st.write(df_all_data)

    with st.form(key='form_page_4'):
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Adapter</h5>", unsafe_allow_html=True)

            col_4_1, col_4_2 = st.columns([1, 1])
            with col_4_1:
                set_temperature_adapter = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_adapter")


            with col_4_2 :
                actual_temperature_adapter = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_adapter")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>PoDV</h5>", unsafe_allow_html=True)

            col_4_3, col_4_4 = st.columns([1, 1])
            with col_4_3:
                set_temperature_podv = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_podv")

            with col_4_4 :
                actual_temperature_podv = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_podv")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Die Plate</h5>", unsafe_allow_html=True)

            col_4_5, col_4_6 = st.columns([1, 1])
            with col_4_5:
                set_temperature_die_plate = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_die_plate")

            with col_4_6 :
                actual_temperature_die_plate = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_die_plate")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Water Tank</h5>", unsafe_allow_html=True)

            col_4_7, col_4_8 = st.columns([1, 1])
            with col_4_7:
                set_temperature_water_tank = st.number_input("", value=None, placeholder="SET POINT", key="set_temperature_water_tank")

            with col_4_8 :
                actual_temperature_water_tank = st.number_input("", value=None, placeholder="AKTUAL", key="actual_temperature_water_tank")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Jenis Die Plate</h5>", unsafe_allow_html=True)
            die_plate_options = ["E01; 2.8 mm; 10 hole", "E02; 2 mm; 20 hole","E02; 3.5 mm; 17 hole","E02; 4 mm; 9 hole","E03; 2 mm; 20 hole",
            "E03; 4 mm; 15 hole","E03; 3.5 mm; 7 hole","E05; 2.8 mm; 20 hole","E05; 2.8 mm; 10 hole","E05; 3.2 mm; 10 hole","E06; 2 mm; 48 hole",
            "E06; 2.8 mm; 24 hole"]
            die_plate_options = st.radio('', die_plate_options, key="die_plate_options")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Cutter</h5>", unsafe_allow_html=True)

            col_4_9, col_4_10, col_4_11, col_4_12 = st.columns([1, 1, 1, 1])
            with col_4_9:
                ampere_cutter = st.number_input("", value=None, placeholder="AMPERE/TORSI CUTTER", key="ampere_cutter")

            with col_4_10:
                rpm_cutter = st.number_input("", value=None, placeholder="RPM CUTTER", key="rpm_cutter")

            with col_4_11:
                setting_cutter = st.number_input("", value=None, placeholder="SETTING MAJU CUTTER", key="setting_cutter")

            with col_4_12:
                percentage_cutter = st.number_input("", value=None, placeholder="% PANJANG CUTTER", key="percentage_cutter")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Air Proses UWP</h5>", unsafe_allow_html=True)

            col_4_13, col_4_14 = st.columns([1, 1])
            with col_4_13:
                uwp_water_pressure = st.number_input("", value=None, placeholder="TEKANAN AIR PROSES UWP", key="uwp_water_pressure")

            with col_4_14:
                uwp_water_flow = st.number_input("", value=None, placeholder="FLOW/DEBIT AIR PROSES UWP", key="uwp_water_flow")

        
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Jenis Cutter Hub</h5>", unsafe_allow_html=True)
            cutter_hub_options = ["E05; Blade 10","E06; Blade 6","E06; Blade 9"]
            cutter_hub_options = st.radio('', cutter_hub_options, key="cutter_hub_options")

        
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Mesh Screen</h5>", unsafe_allow_html=True)
            mesh_screen_options = ["SUS 403; 20 mesh","SUS 403; 40 mesh","SUS 403; 60 mesh","SUS 403; 80 mesh","SUS 403; 100 mesh",
            "SUS 403; 120 mesh","SUS 403; 250 mesh","Dutch Weave; 80 mesh","Dutch Weave; 100 mesh","Dutch Weave; 250 mesh"]
            mesh_screen_options = st.radio('', mesh_screen_options, key="mesh_screen_options")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Air Proses UWP</h5>", unsafe_allow_html=True)

            col_4_15, col_4_16 = st.columns([1, 1])
            with col_4_15:
                temperature_in_proses = st.number_input("", value=None, placeholder="TEMPERATURE IN AIR PROSES", key="temperature_in_proses")

            with col_4_16 :
                temperature_out_proses = st.number_input("", value=None, placeholder="TEMPERATURE OUT AIR PROSES", key="temperature_out_proses")


        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Air Cooling Tower - HE UWP</h5>", unsafe_allow_html=True)

            col_4_17, col_4_18 = st.columns([1, 1])
            with col_4_17:
                temperature_in_cooling_water = st.number_input("", value=None, placeholder="TEMPERATURE IN AIR COOLING TOWER", key="temperature_in_cooling_water")

            with col_4_18 :
                temperature_out_cooling_water = st.number_input("", value=None, placeholder="TEMPERATURE OUT AIR COOLING TOWER", key="temperature_out_cooling_water")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Parameter Produk FG</h5>", unsafe_allow_html=True)

            col_4_19, col_4_20 = st.columns([1, 1])
            with col_4_19:
                actual_output_finished_good = st.number_input("", value=None, placeholder="OUTPUT AKTUAL FG", key="actual_output_finished_good")

            with col_4_20 :
                granule_number = st.number_input("", value=None, placeholder="JUMLAH GRANULE PER GRAM", key="granule_number")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>JUMLAH DIE HOLE TERBUKA</h5>", unsafe_allow_html=True)
            die_hole_open_calc = st.number_input("HASIL PERHITUNGAN", key="die_hole_open_calc")

        can_submit = True

        if not set_temperature_adapter:
            st.warning('Isi bagian "Set Point Temperature Adapter"!')
            can_submit = False
        
        if not actual_temperature_adapter:
            st.warning('Isi bagian "Aktual Temperature Adapter"!')
            can_submit = False

        if not set_temperature_podv:
            st.warning('Isi bagian "Set Point Temperature PoDV"!')
            can_submit = False

        if not actual_temperature_podv:
            st.warning('Isi bagian "Aktual Temperature PoDV"!')
            can_submit = False

        if not set_temperature_die_plate:
            st.warning('Isi bagian "Set Point Temperature Die Plate"!')
            can_submit = False

        if not actual_temperature_die_plate:
            st.warning('Isi bagian "Aktual Temperature Die Plate"!')
            can_submit = False

        if not set_temperature_water_tank:
            st.warning('Isi bagian "Set Point Temperature Water Tank"!')
            can_submit = False

        if not actual_temperature_water_tank:
            st.warning('Isi bagian "Aktual Temperature Water Tank"!')
            can_submit = False

        if not die_plate_options:
            st.warning('Isi bagian "Jenis Die Plate"!')
            can_submit = False

        if not ampere_cutter:
            st.warning('Isi bagian "Ampere/Torsi Cutter"!')
            can_submit = False

        if not rpm_cutter:
            st.warning('Isi bagian "RPM Cutter"!')
            can_submit = False

        if not setting_cutter:
            st.warning('Isi bagian "Setting Maju Cutter"!')
            can_submit = False

        if not percentage_cutter:
            st.warning('Isi bagian "% Panjang Cutter"!')
            can_submit = False

        if not uwp_water_pressure:
            st.warning('Isi bagian "Tekanan Air Proses UWP"!')
            can_submit = False

        if not uwp_water_flow:
            st.warning('Isi bagian "Flow Air Proses UWP"!')
            can_submit = False

        if not cutter_hub_options:
            st.warning('Isi bagian "Jenis Cutter Hub"!')
            can_submit = False

        if not mesh_screen_options:
            st.warning('Isi bagian "Mesh Screen"!')
            can_submit = False

        if not temperature_in_proses:
            st.warning('Isi bagian "Temperature In Air Proses"!')
            can_submit = False

        if not temperature_out_proses:
            st.warning('Isi bagian "Temperature Out Air Proses"!')
            can_submit = False

        if not temperature_in_cooling_water:
            st.warning('Isi bagian "Temperature In Air Cooling Tower"!')
            can_submit = False
        
        if not temperature_out_cooling_water:
            st.warning('Isi bagian "Temperature Out Air Cooling Tower"!')
            can_submit = False

        if not actual_output_finished_good:
            st.warning('Isi bagian "Output Aktual FG"!')
            can_submit = False

        if not granule_number:
            st.warning('Isi bagian "Jumlah Granule per Gram"!')
            can_submit = False

        if not die_hole_open_calc:
            st.warning('Isi bagian "Perhitungan Jumlah Die Hole Terbuka"!')
            can_submit = False


        submit_button_4_1 = st.form_submit_button(label='Submit')

        if submit_button_4_1:

            if can_submit == False:
                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
            else:
                nama_kolom_page_4 = {
                    "Set Point Temperature Adapter": [], 
                    "Aktual Temperature Adapter": [], 
                    "Set Point Temperature PoDV": [], 
                    "Aktual Temperature PoDV": [], 
                    "Set Point Temperature Die Plate": [], 
                    "Aktual Temperature Die Plate": [], 
                    "Set Point Temperature Water Tank": [], 
                    "Aktual Temperature Water Tank": [], 
                    "Ampere/Torsi Cutter": [], 
                    "RPM Cutter": [],
                    "Setting Maju Cutter": [], 
                    "% Panjang Cutter": [],
                    "Tekanan Air Proses UWP": [], 
                    "Flow Air Proses UWP": [], 
                    "Temperature In Air Proses": [], 
                    "Temperature Out Air Proses": [],
                    "Temperature In Air Cooling Tower": [], 
                    "Temperature Out Air Cooling Tower": [],
                    "Output Aktual FG": [], 
                    "Jumlah Granule per Gram": [],
                    "Perhitungan Jumlah Die Hole Terbuka": [], 
                    }
                df_data_page_4 = pd.DataFrame(nama_kolom_page_4)

                new_row_page_4 = pd.DataFrame({
                    "Set Point Temperature Adapter": [set_temperature_adapter], 
                    "Aktual Temperature Adapter": [actual_temperature_adapter], 
                    "Set Point Temperature PoDV": [set_temperature_podv], 
                    "Aktual Temperature PoDV": [actual_temperature_podv], 
                    "Set Point Temperature Die Plate": [set_temperature_die_plate], 
                    "Aktual Temperature Die Plate": [actual_temperature_die_plate], 
                    "Set Point Temperature Water Tank": [set_temperature_water_tank], 
                    "Aktual Temperature Water Tank": [actual_temperature_water_tank], 
                    "Ampere/Torsi Cutter": [ampere_cutter], 
                    "RPM Cutter": [rpm_cutter],
                    "Setting Maju Cutter": [setting_cutter], 
                    "% Panjang Cutter": [percentage_cutter],
                    "Tekanan Air Proses UWP": [uwp_water_pressure], 
                    "Flow Air Proses UWP": [uwp_water_flow], 
                    "Temperature In Air Proses": [temperature_in_proses], 
                    "Temperature Out Air Proses": [temperature_out_proses],
                    "Temperature In Air Cooling Tower": [temperature_in_cooling_water], 
                    "Temperature Out Air Cooling Tower": [temperature_out_cooling_water],
                    "Output Aktual FG": [actual_output_finished_good], 
                    "Jumlah Granule per Gram": [granule_number],
                    "Perhitungan Jumlah Die Hole Terbuka": [die_hole_open_calc] 
                })
                df_data_page_4 = pd.concat([df_data_page_4, new_row_page_4]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_4)
                st.session_state.df_data_page_4 = df_data_page_4
    
    submit_button_2_4 = st.button(type="primary", label='Next Page')
    if submit_button_2_4:
        if "df_data_page_4" not in st.session_state:
            st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit"sebelum menekan tombol "Next Page"!')
        else:
            st.session_state.page = 5
            st.rerun()


#Halaman 5
if st.session_state["page"] == 5:
    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 5 : QUANTITY REWORK</h3>", unsafe_allow_html=True)
    # st.markdown(f"<h3 style='text-align: center;'>EXTRUDER<br></h3>", unsafe_allow_html=True)
    # st.write(df_all_data)

    with st.form(key='form_page_5'):
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK TAILING</h5>", unsafe_allow_html=True)
            tailing_rework = st.number_input("", key="tailing_rework")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK GANDENG/DEMPET</h5>", unsafe_allow_html=True)
            gandeng_rework = st.number_input("", key="gandeng_rework")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK HAZY</h5>", unsafe_allow_html=True)
            hazy_rework = st.number_input("", key="hazy_rework")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK DISPERSE</h5>", unsafe_allow_html=True)
            disperse_rework = st.number_input("", key="disperse_rework")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK GRAMASI</h5>", unsafe_allow_html=True)
            gramasi_rework = st.number_input("", key="gramasi_rework")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK HOMOGEN</h5>", unsafe_allow_html=True)
            homogen_rework = st.number_input("", key="homogen_rework")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK PHOROUS</h5>", unsafe_allow_html=True)
            phorous_rework = st.number_input("", key="phorous_rework")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK REKONDISI</h5>", unsafe_allow_html=True)
            rekondisi_rework = st.number_input("", key="rekondisi_rework")


        can_submit = True

        if tailing_rework is None:
            st.warning('Isi bagian "Quantity Rework Tailing"!')
            can_submit = False
        
        if gandeng_rework is None:
            st.warning('Isi bagian "Quantity Rework Gandeng/Dempet"!')
            can_submit = False

        if hazy_rework is None:
            st.warning('Isi bagian "Quantity Rework Hazy"!')
            can_submit = False

        if not disperse_rework:
            st.warning('Isi bagian "Quantity Rework Disperse"!')
            can_submit = False

        if not gramasi_rework:
            st.warning('Isi bagian "Quantity Rework Gramasi"!')
            can_submit = False

        if not homogen_rework:
            st.warning('Isi bagian "Quantity Rework Homogen"!')
            can_submit = False

        if not phorous_rework:
            st.warning('Isi bagian "Quantity Rework Phorous"!')
            can_submit = False

        if not rekondisi_rework:
            st.warning('Isi bagian "Quantity Rework Rekondisi"!')
            can_submit = False

        submit_button_5_1 = st.form_submit_button(label='Submit')

        if submit_button_5_1:

            if can_submit == False:
                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
            else:
                nama_kolom_page_5 = {
                    "Quantity Rework Tailing": [], 
                    "Quantity Rework Gandeng/Dempet": [], 
                    "Quantity Rework Hazy": [], 
                    "Quantity Rework Disperse": [], 
                    "Quantity Rework Gramasi": [], 
                    "Quantity Rework Homogen": [], 
                    "Quantity Rework Phorous": [], 
                    "Quantity Rework Rekondisi": [],  
                    }
                df_data_page_5 = pd.DataFrame(nama_kolom_page_5)

                new_row_page_5 = pd.DataFrame({
                    "Quantity Rework Tailing": [tailing_rework], 
                    "Quantity Rework Gandeng/Dempet": [gandeng_rework], 
                    "Quantity Rework Hazy": [hazy_rework], 
                    "Quantity Rework Disperse": [disperse_rework], 
                    "Quantity Rework Gramasi": [gramasi_rework], 
                    "Quantity Rework Homogen": [homogen_rework], 
                    "Quantity Rework Phorous": [phorous_rework], 
                    "Quantity Rework Rekondisi": [rekondisi_rework] 
                })
                df_data_page_5 = pd.concat([df_data_page_5, new_row_page_5]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_5)
                st.session_state.df_data_page_5 = df_data_page_5
    
    submit_button_2_5 = st.button(type="primary", label='Next Page')
    if submit_button_2_5:
        if "df_data_page_5" not in st.session_state:
            st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit"sebelum menekan tombol "Next Page"!')
        else:
            st.session_state.page = 4
            st.rerun()




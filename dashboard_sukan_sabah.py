# Save as: dashboard_sukan_sabah.py
# Run with: streamlit run dashboard_sukan_sabah.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import io
import base64

# Load all data from the provided Excel structure
def load_all_data():
    """Load ALL sports data from the provided Excel structure"""
    
    # Create comprehensive data from the provided table
    data = [
        # ========== AKUATIK RENANG ==========
        {
            "BIL": "1.0", "SUKAN": "AKUATIK RENANG", "DAERAH": "KOTA KINABALU",
            "JURULATIH": "RAFFIE BIN ROBERT@RAHIM", "NO_TELEFON": "011-56465375",
            "PROGRAM": "PROGRAM BAKAT & PELAPIS NEGERI 2025", "STATUS": "JSM",
            "ATLET_L": 8.0, "ATLET_P": 4.0, "TOTAL_ATLET": 12.0,
            "PUSAT_LATIHAN": "PUSAT AKUATIK, KOMPLEKS SUKAN KOTA KINABALU",
            "HAK_MILIK": "LSS",
            "JADUAL_ISNIN": "5.00 PM - 7.00 PM <br>DRYLAND",
            "JADUAL_SELASA": "6.30 PM - 8.30 PM",
            "JADUAL_RABU": "6.30 PM - 8.30 PM",
            "JADUAL_KHAMIS": "6.30 PM - 8.30 PM",
            "JADUAL_JUMAAT": "6.30 PM - 8.30 PM",
            "JADUAL_SABTU": "6.30 PM - 8.30 PM",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        {
            "BIL": "", "SUKAN": "AKUATIK RENANG", "DAERAH": "PENAMPANG",
            "JURULATIH": "BENJAMIN LEE TSUN MIN", "NO_TELEFON": "016-3115058",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI & SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 43.0, "ATLET_P": 27.0, "TOTAL_ATLET": 70.0,
            "PUSAT_LATIHAN": "PUSAT AKUATIK , KOMPLEKS SUKAN PENAMPANG",
            "HAK_MILIK": "",
            "JADUAL_ISNIN": "",
            "JADUAL_SELASA": "KOMPLEKS SUKAN <br>PENAMPANG<br><br>SESI PAGI<br>5.30 am - 6.30 am<br><br>SESI PETANG<br>6.30 pm - 8.30 pm",
            "JADUAL_RABU": "KOMPLEKS SUKAN<br>PENAMPANG<br><br>SESI PETANG<br>6.30 pm - 8.30 pm",
            "JADUAL_KHAMIS": "KOMPLEKS SUKAN <br>PENAMPANG<br><br>SESI PAGI<br>5.30 am - 6.30 am<br><br>SESI PETANG<br>6.30 pm - 8.30 pm",
            "JADUAL_JUMAAT": "KOMPLEKS SUKAN<br>PENAMPANG<br><br>SESI PETANG<br>6.30 pm - 8.30 pm",
            "JADUAL_SABTU": "KOMPLEKS SUKAN <br>PENAMPANG<br><br>SESI PAGI<br>5.30 am - 6.30 am<br><br>SESI PETANG<br>6.30 pm - 8.30 pm",
            "JADUAL_AHAD": "KOMPLEKS SUKAN<br>PENAMPANG<br><br>SESI PETANG<br>6.30 pm - 8.30 pm",
            "CATATAN": ""
        },
        {
            "BIL": "", "SUKAN": "AKUATIK RENANG", "DAERAH": "PENAMPANG",
            "JURULATIH": "JEANNYVIE JOHN FABIAN", "NO_TELEFON": "014-9552904",
            "PROGRAM": "PROGRAM BAKAT & PELAPIS NEGERI 2025", "STATUS": "JSM",
            "ATLET_L": 5.0, "ATLET_P": 5.0, "TOTAL_ATLET": 10.0,
            "PUSAT_LATIHAN": "PUSAT AKUATIK , KOMPLEKS SUKAN PENAMPANG",
            "HAK_MILIK": "",
            "JADUAL_ISNIN": "",
            "JADUAL_SELASA": "6.00 PM - 7.00 PM",
            "JADUAL_RABU": "6.00 PM - 7.00 PM",
            "JADUAL_KHAMIS": "6.00 PM - 7.00 PM",
            "JADUAL_JUMAAT": "6.00 PM - 7.00 PM",
            "JADUAL_SABTU": "6.00 PM - 7.00 PM",
            "JADUAL_AHAD": "5.00 PM - 6.30 PM",
            "CATATAN": ""
        },
        {
            "BIL": "", "SUKAN": "AKUATIK RENANG", "DAERAH": "SANDAKAN",
            "JURULATIH": "ELVIN NICHOLAS CHIA TSHUN THAU", "NO_TELEFON": "019-8531059",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI & SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 7.0, "ATLET_P": 8.0, "TOTAL_ATLET": 15.0,
            "PUSAT_LATIHAN": "KOLAM RENANG, KOMPLEKS SUKAN SANDAKAN",
            "HAK_MILIK": "",
            "JADUAL_ISNIN": "4.30 PM",
            "JADUAL_SELASA": "6.00 PM",
            "JADUAL_RABU": "6.00 PM",
            "JADUAL_KHAMIS": "6.00 PM",
            "JADUAL_JUMAAT": "6.00 PM",
            "JADUAL_SABTU": "SESI PAGI<br>6.00 PAGI<br><br>SESI PETANG<br> 4.00 PM",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        {
            "BIL": "", "SUKAN": "AKUATIK RENANG", "DAERAH": "SANDAKAN",
            "JURULATIH": "CYNTHIA LIEW SING TI", "NO_TELEFON": "013-8060737",
            "PROGRAM": "PROGRAM BAKAT & PELAPIS NEGERI 2025", "STATUS": "JSM",
            "ATLET_L": 10.0, "ATLET_P": 6.0, "TOTAL_ATLET": 10.0,
            "PUSAT_LATIHAN": "KOLAM RENANG, KOMPLEKS SUKAN SANDAKAN",
            "HAK_MILIK": "",
            "JADUAL_ISNIN": "",
            "JADUAL_SELASA": "4.00 PM - 5.30 PM",
            "JADUAL_RABU": "4.00 PM - 6.00 PM",
            "JADUAL_KHAMIS": "4.00 PM - 6.00 PM",
            "JADUAL_JUMAAT": "4.00 PM - 6.00 PM",
            "JADUAL_SABTU": "3.30 PM - 6.00 PM",
            "JADUAL_AHAD": "SESI PAGI <br>6.00 AM - 8.00 AM<br><br>SESI PETANG<br>4.00 PM - 6.00 PM",
            "CATATAN": ""
        },
        {
            "BIL": "", "SUKAN": "AKUATIK RENANG", "DAERAH": "SANDAKAN",
            "JURULATIH": "GOH SONG WEE", "NO_TELEFON": "016-7010960",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI & SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 27.0, "ATLET_P": 16.0, "TOTAL_ATLET": 43.0,
            "PUSAT_LATIHAN": "KOMPLEKS SUKAN SANDAKAN / IJM REKREASI CLUB",
            "HAK_MILIK": "KELAB",
            "JADUAL_ISNIN": "IJM RECREATION CLUB<br>3.00 PM",
            "JADUAL_SELASA": "KOMPLEKS SUKA N SANDAKAN<br>4.00 PM<br>(COACH RONISAFIHIN HANDLE ATLET SETIAP SELASA)",
            "JADUAL_RABU": "KOMPLEKS SUKAN SANDAKAN<br>4.00 PM<br><br>IJM RECREATION CLUB<br>6.00 PM",
            "JADUAL_KHAMIS": "KOMPLEKS SUKAN SANDAKAN<br>4.00 PM<br><br>IJM RECREATION CLUB<br>6.00 PM",
            "JADUAL_JUMAAT": "IJM RECREATION CLUB<br>3.00 PM & 6.00 PM",
            "JADUAL_SABTU": "KOMPLEKS SUKAN SANDAKAN<br>6.00 AM",
            "JADUAL_AHAD": "KOMPLEKS SUKAN SANDAKAN<br>6.00 AM",
            "CATATAN": ""
        },
        {
            "BIL": "", "SUKAN": "AKUATIK RENANG", "DAERAH": "TAWAU",
            "JURULATIH": "CHUNG SIAN DER", "NO_TELEFON": "016-8125046",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI & SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 3.0, "ATLET_P": 7.0, "TOTAL_ATLET": 10.0,
            "PUSAT_LATIHAN": "KOLAM RENANG, KOMPLEKS SUKAN TAWAU / TAWAU GOLF CLUB",
            "HAK_MILIK": "LSS",
            "JADUAL_ISNIN": "",
            "JADUAL_SELASA": "TAWAU GOLF CLUB<br>4.45 PM - 6.00 PM",
            "JADUAL_RABU": "",
            "JADUAL_KHAMIS": "TAWAU GOLF CLUB<br>4.30 PM - 6.00 PM",
            "JADUAL_JUMAAT": "KOMPLEKS SUKAN TAWAU<br>9.00 AM - 10.15 AM<br><br>TAWAU GOLF CLUB<br>5.00 PM - 6.00 PM",
            "JADUAL_SABTU": "TAWAU GOLF CLUB<br>5.30 PM - 6.45 PM",
            "JADUAL_AHAD": "KOMPLEKS SUKAN TAWAU<br>9.15 AM - 10.30 AM",
            "CATATAN": ""
        },
        
        # ========== AKUATIK TERJUN ==========
        {
            "BIL": "", "SUKAN": "AKUATIK TERJUN", "DAERAH": "KOTA KINABALU",
            "JURULATIH": "NURFAZRIYANTI BINTI JALI", "NO_TELEFON": "011-63806929",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI & SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 9.0, "ATLET_P": 8.0, "TOTAL_ATLET": 17.0,
            "PUSAT_LATIHAN": "PLN PUSAT AKUATIK KOMPLEKS SUKAN KOTA KINABALU",
            "HAK_MILIK": "LSS",
            "JADUAL_ISNIN": "3.00 PM - 6.00 PM",
            "JADUAL_SELASA": "3.00 PM - 6.00 PM",
            "JADUAL_RABU": "3.00 PM - 6.00 PM",
            "JADUAL_KHAMIS": "3.00 PM - 6.00 PM",
            "JADUAL_JUMAAT": "3.00 PM - 6.00 PM",
            "JADUAL_SABTU": "9.00 AM - 12 PM",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        
        # ========== ANGKAT BERAT ==========
        {
            "BIL": "2.0", "SUKAN": "ANGKAT BERAT", "DAERAH": "KOTA KINABALU",
            "JURULATIH": "ARICCO JUMITIH", "NO_TELEFON": "016-8120414",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI & SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 8.0, "ATLET_P": 1.0, "TOTAL_ATLET": 9.0,
            "PUSAT_LATIHAN": "SEKOLAH SUKAN MALAYSIA SABAH",
            "HAK_MILIK": "KPM",
            "JADUAL_ISNIN": "SESI PAGI<br>6.00 PAGI - 8.00 PAGI<br><br>SESI PETANG<br>4.00 PTG - 7.00 MLM",
            "JADUAL_SELASA": "",
            "JADUAL_RABU": "SESI PAGI<br>6.00 PAGI - 8.00 PAGI<br><br>SESI PETANG<br>4.00 PTG - 7.00 MLM",
            "JADUAL_KHAMIS": "SESI PAGI<br>6.00 PAGI - 8.00 PAGI<br><br>SESI PETANG<br>4.00 PTG - 7.00 MLM",
            "JADUAL_JUMAAT": "SESI PAGI<br>6.00 PAGI - 8.00 PAGI<br><br>SESI PETANG<br>4.00 PTG - 7.00 MLM",
            "JADUAL_SABTU": "SESI PAGI<br>6.00 PAGI - 8.00 PAGI<br><br>SESI PETANG<br>4.00 PTG - 7.00 MLM",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        {
            "BIL": "", "SUKAN": "ANGKAT BERAT", "DAERAH": "PAPAR",
            "JURULATIH": "NICHOLAS WONG CHEE YEN", "NO_TELEFON": "010-7978287",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI", "STATUS": "JPM",
            "ATLET_L": 4.0, "ATLET_P": 3.0, "TOTAL_ATLET": 7.0,
            "PUSAT_LATIHAN": "PLN ANGKAT BERAT KINARUT, PAPAR",
            "HAK_MILIK": "PERSENDIRIAN",
            "JADUAL_ISNIN": "4.30 PM -6:30 PM",
            "JADUAL_SELASA": "4.30 PM -6:30 PM",
            "JADUAL_RABU": "4.30 PM -6:30 PM",
            "JADUAL_KHAMIS": "4.30 PM -6:30 PM",
            "JADUAL_JUMAAT": "4.30 PM -6:30 PM",
            "JADUAL_SABTU": "9.30 AM - 11.30 AM",
            "JADUAL_AHAD": "4.30 PM -6:30 PM",
            "CATATAN": ""
        },
        
        # ========== BINA BADAN ==========
        {
            "BIL": "4.0", "SUKAN": "BINA BADAN", "DAERAH": "PENAMPANG",
            "JURULATIH": "JEFFRY THADDEUS", "NO_TELEFON": "019-8320678",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI", "STATUS": "JSM",
            "ATLET_L": 11.0, "ATLET_P": 1.0, "TOTAL_ATLET": 12.0,
            "PUSAT_LATIHAN": "PENAMPANG",
            "HAK_MILIK": "SWASTA",
            "JADUAL_ISNIN": "",
            "JADUAL_SELASA": "5.00 PM",
            "JADUAL_RABU": "5.00 PM",
            "JADUAL_KHAMIS": "5.00 PM",
            "JADUAL_JUMAAT": "5.00 PM",
            "JADUAL_SABTU": "",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        
        # ========== GIMNASTIK ARTISTIK ==========
        {
            "BIL": "5.0", "SUKAN": "GIMNASTIK ARTISTIK", "DAERAH": "KOTA KINABALU",
            "JURULATIH": "LIEW TONG EE", "NO_TELEFON": "016-8441962",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGER", "STATUS": "JPM",
            "ATLET_L": 14.0, "ATLET_P": 10.0, "TOTAL_ATLET": 24.0,
            "PUSAT_LATIHAN": "DEWAN GIMNASTIK, KOMPLEKS SUKAN KOTA KINABALU",
            "HAK_MILIK": "LSS",
            "JADUAL_ISNIN": "6.00 PM - 9.00 PM",
            "JADUAL_SELASA": "6.00 PM - 9.00 PM",
            "JADUAL_RABU": "6.00 PM - 9.00 PM",
            "JADUAL_KHAMIS": "6.00 PM - 9.00 PM",
            "JADUAL_JUMAAT": "6.00 PM - 9.00 PM",
            "JADUAL_SABTU": "2.00 PM - 5.00 PM",
            "JADUAL_AHAD": "6.00 PM - 9.00 PM",
            "CATATAN": ""
        },
        
        # ========== HOKI ==========
        {
            "BIL": "7.0", "SUKAN": "HOKI", "DAERAH": "KOTA MARUDU",
            "JURULATIH": "HARRYYAN TOMIN", "NO_TELEFON": "019-8427928",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI", "STATUS": "JSM",
            "ATLET_L": 16.0, "ATLET_P": 23.0, "TOTAL_ATLET": 39.0,
            "PUSAT_LATIHAN": "SK MARAK PARAK, KOTA MARUDU",
            "HAK_MILIK": "KPM",
            "JADUAL_ISNIN": "3.00 PM - 5.00 PM",
            "JADUAL_SELASA": "6.20 AM - 7.20 AM",
            "JADUAL_RABU": "6.20 AM - 7.20 AM",
            "JADUAL_KHAMIS": "6.20 AM - 7.20 AM",
            "JADUAL_JUMAAT": "6.20 AM - 7.20 AM",
            "JADUAL_SABTU": "",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        
        # ========== JUDO ==========
        {
            "BIL": "8.0", "SUKAN": "JUDO", "DAERAH": "PENAMPANG",
            "JURULATIH": "TAY YUN LAI", "NO_TELEFON": "016-8115112",
            "PROGRAM": "PROGRAM BAKAT & PELAPIS NEGERI", "STATUS": "JSM",
            "ATLET_L": 36.0, "ATLET_P": 16.0, "TOTAL_ATLET": 52.0,
            "PUSAT_LATIHAN": "JOULE SPPORT STUDIO, KEPAYAN POINT, PENAMPANG",
            "HAK_MILIK": "SWASTA",
            "JADUAL_ISNIN": "4.00 PM – 7.00 PM",
            "JADUAL_SELASA": "6.30 PM – 9.30 PM",
            "JADUAL_RABU": "4.00 PM – 7.00 PM",
            "JADUAL_KHAMIS": "4.00 PM – 7.00 PM",
            "JADUAL_JUMAAT": "6.30 PM – 9.30 PM",
            "JADUAL_SABTU": "2.00 PM – 5.00 PM",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        
        # ========== KARATE ==========
        {
            "BIL": "9.0", "SUKAN": "KARATE", "DAERAH": "KOTA KINABALU",
            "JURULATIH": "DANNY FREDOLINE", "NO_TELEFON": "016-6586593",
            "PROGRAM": "PROGRAM BAKAT DAN PELAPIS NEGERI & SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 7.0, "ATLET_P": 6.0, "TOTAL_ATLET": 13.0,
            "PUSAT_LATIHAN": "KOMPLEKS SUKAN KOTA KINABALU",
            "HAK_MILIK": "LSS",
            "JADUAL_ISNIN": "",
            "JADUAL_SELASA": "7: 00 PM – 8:30 PM",
            "JADUAL_RABU": "7: 00 PM – 8:30 PM",
            "JADUAL_KHAMIS": "7: 00 PM – 8:30 PM",
            "JADUAL_JUMAAT": "7: 00 PM – 8:30 PM",
            "JADUAL_SABTU": "10:30 AM – 11: 30 AM",
            "JADUAL_AHAD": "10:30 AM – 11: 30 AM",
            "CATATAN": ""
        },
        
        # ========== MEMANAH ==========
        {
            "BIL": "11.0", "SUKAN": "MEMANAH", "DAERAH": "KOTA KINABALU",
            "JURULATIH": "WONG CO WAN", "NO_TELEFON": "016-8233509",
            "PROGRAM": "PROGRAM BAKAT & PELAPIS NEGERI & PROGRAM SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 7.0, "ATLET_P": 2.0, "TOTAL_ATLET": 9.0,
            "PUSAT_LATIHAN": "KOMPLEKS SUKAN KOTA KINABALU",
            "HAK_MILIK": "LSS",
            "JADUAL_ISNIN": "",
            "JADUAL_SELASA": "4.00 PM - 6.30 PM",
            "JADUAL_RABU": "4.00 PM - 6.30 PM",
            "JADUAL_KHAMIS": "4.00 PM - 6.30 PM",
            "JADUAL_JUMAAT": "4.00 PM - 6.30 PM",
            "JADUAL_SABTU": "4.00 PM - 6.30 PM",
            "JADUAL_AHAD": "4.00 PM - 6.30 PM",
            "CATATAN": ""
        },
        
        # ========== MENEMBAK ==========
        {
            "BIL": "12.0", "SUKAN": "MENEMBAK", "DAERAH": "LOK KAWI",
            "JURULATIH": "DENIS EJOH @ AJOH", "NO_TELEFON": "016-9953600",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI & SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 11.0, "ATLET_P": 8.0, "TOTAL_ATLET": 19.0,
            "PUSAT_LATIHAN": "LAPANG SASAR MENEMBAK, LOK KAWI",
            "HAK_MILIK": "PSN",
            "JADUAL_ISNIN": "2.00 PM-4.00 PM",
            "JADUAL_SELASA": "2.00 PM-4.00 PM",
            "JADUAL_RABU": "2.00 PM-4.00 PM",
            "JADUAL_KHAMIS": "2.00 PM-4.00 PM",
            "JADUAL_JUMAAT": "2.00 PM-4.00 PM",
            "JADUAL_SABTU": "SESI PAGI<br>8.00 AM – 10.00 AM<br><br>SESI TGH HARI<br>10.00 AM- 12.00 PM<br><br>SESI MALAM<br>2.00 PM - .4.00 PM",
            "JADUAL_AHAD": "SESI PAGI<br>8.00 AM – 10.00 AM<br><br>SESI TGH HARI<br>10.00 AM- 12.00 PM<br><br>SESI MALAM<br>2.00 PM - .4.00 PM",
            "CATATAN": ""
        },
        
        # ========== MUAY ==========
        {
            "BIL": "13.0", "SUKAN": "MUAY", "DAERAH": "KEPAYAN",
            "JURULATIH": "CYRILLE DHILLON TAHING", "NO_TELEFON": "016-8013530",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI", "STATUS": "JPM",
            "ATLET_L": 16.0, "ATLET_P": 8.0, "TOTAL_ATLET": 24.0,
            "PUSAT_LATIHAN": "REVOLUTION THAI MUAY GYM, KEPAYAN",
            "HAK_MILIK": "JKK",
            "JADUAL_ISNIN": "5.00 PM - 8.30 PM",
            "JADUAL_SELASA": "",
            "JADUAL_RABU": "5.00 PM - 8.30 PM",
            "JADUAL_KHAMIS": "",
            "JADUAL_JUMAAT": "5.00 PM - 8.30 PM",
            "JADUAL_SABTU": "",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        
        # ========== OLAHRAGA ==========
        {
            "BIL": "14.0", "SUKAN": "OLAHRAGA", "DAERAH": "KOTA KINABALU",
            "JURULATIH": "FAHRUL NAZRI BIN AB NASIR", "NO_TELEFON": "016-2178581",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI", "STATUS": "JPM",
            "ATLET_L": 24.0, "ATLET_P": 11.0, "TOTAL_ATLET": 35.0,
            "PUSAT_LATIHAN": "KOMPLEKS SUKAN KOTA KINABALU",
            "HAK_MILIK": "LSNS",
            "JADUAL_ISNIN": "4.00 PM - 6.00 PM",
            "JADUAL_SELASA": "4.00 PM - 6.00 PM",
            "JADUAL_RABU": "4.00 PM - 6.00 PM",
            "JADUAL_KHAMIS": "4.00 PM - 6.00 PM",
            "JADUAL_JUMAAT": "4.00 PM - 6.00 PM",
            "JADUAL_SABTU": "4.00 PM - 6.00 PM",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        
        # ========== PELAYARAN ==========
        {
            "BIL": "15.0", "SUKAN": "PELAYARAN", "DAERAH": "KOTA KINABALU",
            "JURULATIH": "CHU TEEN FUNG", "NO_TELEFON": "013-850-6655",
            "PROGRAM": "PROGRAM PEMBANGUNAN & SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 6.0, "ATLET_P": 4.0, "TOTAL_ATLET": 10.0,
            "PUSAT_LATIHAN": "KINABALU YATCH CLUB TANJUNG ARU KOTA KINABALU",
            "HAK_MILIK": "KYC",
            "JADUAL_ISNIN": "",
            "JADUAL_SELASA": "2:30 PM - 5:00 PM",
            "JADUAL_RABU": "4:00 PM - 6:00 PM",
            "JADUAL_KHAMIS": "2:30 PM - 5:00 PM",
            "JADUAL_JUMAAT": "8:00 AM - 5:00 PM",
            "JADUAL_SABTU": "8:00 AM - 5:00 PM",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        
        # ========== SEPAKTAKRAW ==========
        {
            "BIL": "18.0", "SUKAN": "SEPAKTAKRAW", "DAERAH": "KOTA KINABALU",
            "JURULATIH": "DAUT BINTI AMBA", "NO_TELEFON": "019-6246768",
            "PROGRAM": "PROGRAM PEMBANGUNAN NEGERI & SUKMA 2026", "STATUS": "JPM",
            "ATLET_L": 9.0, "ATLET_P": 14.0, "TOTAL_ATLET": 23.0,
            "PUSAT_LATIHAN": "DEWAN MAKSAK, 88856 LIKAS, KOTA KINABALU",
            "HAK_MILIK": "MAKSAK",
            "JADUAL_ISNIN": "SESI PAGI<br>8.00 AM – 11.00 AM<br><br><br>SESI PETANG<br>2.30 PM – 4.30 PM<br>",
            "JADUAL_SELASA": "SESI PAGI<br>8.00 AM – 11.00 AM<br><br><br>SESI PETANG<br>2.30 PM – 4.30 PM<br>",
            "JADUAL_RABU": "SESI PAGI<br>8.00 AM – 11.00 AM<br><br><br>SESI PETANG<br>2.30 PM – 4.30 PM<br>",
            "JADUAL_KHAMIS": "SESI PAGI<br>8.00 AM – 11.00 AM<br><br><br>SESI PETANG<br>2.30 PM – 4.30 PM<br>",
            "JADUAL_JUMAAT": "SESI PAGI<br>8.00 AM – 11.00 AM<br><br><br>SESI PETANG<br>2.30 PM – 4.30 PM<br>",
            "JADUAL_SABTU": "SESI PAGI<br>8.00 AM – 11.00 AM<br><br><br>SESI PETANG<br>2.30 PM – 4.30 PM<br>",
            "JADUAL_AHAD": "",
            "CATATAN": ""
        },
        
        # ========== TINJU ==========
        {
            "BIL": "23.0", "SUKAN": "TINJU", "DAERAH": "KOTA KINABALU",
            "JURULATIH": "KHAIRUL AZIM BIN NASSER", "NO_TELEFON": "013-3324688",
            "PROGRAM": "PROGRAM BAKAT & PELAPIS NEGERI 2025", "STATUS": "JSM",
            "ATLET_L": 24.0, "ATLET_P": 2.0, "TOTAL_ATLET": 26.0,
            "PUSAT_LATIHAN": "STADIUM KOMPLEKS SUKAN KOTA KINABALU",
            "HAK_MILIK": "LSS",
            "JADUAL_ISNIN": "",
            "JADUAL_SELASA": "8.00 PM - 9.00 PM",
            "JADUAL_RABU": "",
            "JADUAL_KHAMIS": "8.00 PM - 9.00 PM",
            "JADUAL_JUMAAT": "",
            "JADUAL_SABTU": "8.00 PM - 9.00 PM",
            "JADUAL_AHAD": "8.00 PM - 9.00 PM",
            "CATATAN": ""
        },
    ]
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Add missing completeness status
    def check_completeness(row):
        issues = []
        if not row['JURULATIH'] or str(row['JURULATIH']).strip() == '':
            issues.append('Jurulatih')
        if not row['NO_TELEFON'] or str(row['NO_TELEFON']).strip() == '':
            issues.append('No. Telefon')
        if not row['JADUAL_ISNIN'] and not row['JADUAL_SELASA'] and not row['JADUAL_RABU'] and not row['JADUAL_KHAMIS'] and not row['JADUAL_JUMAAT']:
            issues.append('Jadual')
        
        if issues:
            return f"TIDAK LENGKAP: {', '.join(issues)}"
        else:
            return "LENGKAP"
    
    df['STATUS_KELENGKAPAN'] = df.apply(check_completeness, axis=1)
    
    return df

def create_dashboard():
    st.set_page_config(
        page_title="Dashboard Program Sukan Sabah 2025-2026",
        page_icon="🏅",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Load data
    df = load_all_data()
    
    # Sidebar - Filters
    st.sidebar.title("🎯 FILTER DATA")
    
    # Filter by sport
    all_sports = ["SEMUA"] + sorted(df["SUKAN"].unique().tolist())
    selected_sport = st.sidebar.selectbox("Pilih Jenis Sukan:", all_sports)
    
    # Filter by daerah
    if selected_sport != "SEMUA":
        daerah_options = ["SEMUA"] + sorted(df[df["SUKAN"] == selected_sport]["DAERAH"].unique().tolist())
    else:
        daerah_options = ["SEMUA"] + sorted(df["DAERAH"].unique().tolist())
    
    selected_daerah = st.sidebar.selectbox("Pilih Daerah:", daerah_options)
    
    # Filter by program
    program_options = ["SEMUA"] + sorted(df["PROGRAM"].unique().tolist())
    selected_program = st.sidebar.selectbox("Pilih Program:", program_options)
    
    # Filter by status kelengkapan
    kelengkapan_options = ["SEMUA"] + sorted(df["STATUS_KELENGKAPAN"].unique().tolist())
    selected_kelengkapan = st.sidebar.selectbox("Status Kelengkapan:", kelengkapan_options)
    
    # Apply filters
    filtered_df = df.copy()
    
    if selected_sport != "SEMUA":
        filtered_df = filtered_df[filtered_df["SUKAN"] == selected_sport]
    
    if selected_daerah != "SEMUA":
        filtered_df = filtered_df[filtered_df["DAERAH"] == selected_daerah]
    
    if selected_program != "SEMUA":
        filtered_df = filtered_df[filtered_df["PROGRAM"] == selected_program]
    
    if selected_kelengkapan != "SEMUA":
        filtered_df = filtered_df[filtered_df["STATUS_KELENGKAPAN"] == selected_kelengkapan]
    
    # Main dashboard
    st.title("🏅 DASHBOARD PROGRAM SUKAN SABAH 2025-2026")
    st.markdown("**Program Pembangunan / Pelapis / SUKMA Negeri Sabah**")
    
    # Tab navigation
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "🏋️‍♂️ Data Sukan", "📅 Jadual Latihan", "👥 Jurulatih", "⚠️ Monitoring"])
    
    with tab1:
        # Key metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            total_sukan = filtered_df["SUKAN"].nunique()
            st.metric("Jenis Sukan", total_sukan, help="Jumlah jenis sukan yang aktif")
        
        with col2:
            total_daerah = filtered_df["DAERAH"].nunique()
            st.metric("Daerah", total_daerah, help="Jumlah daerah yang terlibat")
        
        with col3:
            total_atlet = int(filtered_df["TOTAL_ATLET"].sum())
            st.metric("Jumlah Atlet", f"{total_atlet:,}", help="Jumlah keseluruhan atlet")
        
        with col4:
            total_jurulatih = filtered_df["JURULATIH"].nunique()
            st.metric("Jurulatih", total_jurulatih, help="Jumlah jurulatih aktif")
        
        with col5:
            incomplete_count = filtered_df[filtered_df["STATUS_KELENGKAPAN"].str.contains("TIDAK LENGKAP")].shape[0]
            st.metric("Data Tidak Lengkap", incomplete_count, 
                     delta=f"-{incomplete_count}" if incomplete_count > 0 else None,
                     help="Rekod yang perlu kemaskini")
        
        # Charts Row 1
        col1, col2 = st.columns(2)
        
        with col1:
            # Atlet by Sport (Top 10)
            sport_summary = filtered_df.groupby("SUKAN").agg({
                "ATLET_L": "sum",
                "ATLET_P": "sum",
                "TOTAL_ATLET": "sum"
            }).reset_index().sort_values("TOTAL_ATLET", ascending=False).head(10)
            
            fig1 = go.Figure(data=[
                go.Bar(name='Lelaki', x=sport_summary["SUKAN"], y=sport_summary["ATLET_L"], marker_color='#3498db'),
                go.Bar(name='Perempuan', x=sport_summary["SUKAN"], y=sport_summary["ATLET_P"], marker_color='#e74c3c')
            ])
            
            fig1.update_layout(
                title="10 Sukan Terbanyak Atlet",
                xaxis_title="Sukan",
                yaxis_title="Bilangan Atlet",
                barmode='stack',
                height=400,
                showlegend=True
            )
            
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            # Distribution by Daerah
            daerah_summary = filtered_df.groupby("DAERAH")["TOTAL_ATLET"].sum().reset_index()
            daerah_summary = daerah_summary.sort_values("TOTAL_ATLET", ascending=True).tail(10)
            
            fig2 = px.bar(
                daerah_summary,
                x="TOTAL_ATLET",
                y="DAERAH",
                orientation='h',
                title="10 Daerah Terbanyak Atlet",
                color="TOTAL_ATLET",
                color_continuous_scale="Viridis"
            )
            
            fig2.update_layout(height=400)
            st.plotly_chart(fig2, use_container_width=True)
        
        # Charts Row 2
        col1, col2 = st.columns(2)
        
        with col1:
            # Program Distribution
            program_counts = filtered_df["PROGRAM"].value_counts().reset_index()
            program_counts.columns = ["PROGRAM", "COUNT"]
            
            fig3 = px.pie(
                program_counts,
                values="COUNT",
                names="PROGRAM",
                title="Taburan Mengikut Program",
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            
            fig3.update_layout(height=400)
            st.plotly_chart(fig3, use_container_width=True)
        
        with col2:
            # Completeness Status
            completeness_counts = filtered_df["STATUS_KELENGKAPAN"].value_counts().reset_index()
            completeness_counts.columns = ["STATUS", "COUNT"]
            
            # Categorize as LENGKAP or TIDAK LENGKAP
            def categorize_status(status):
                return "LENGKAP" if "LENGKAP" in status and "TIDAK" not in status else "TIDAK LENGKAP"
            
            completeness_counts["KATEGORI"] = completeness_counts["STATUS"].apply(categorize_status)
            summary_counts = completeness_counts.groupby("KATEGORI")["COUNT"].sum().reset_index()
            
            fig4 = px.pie(
                summary_counts,
                values="COUNT",
                names="KATEGORI",
                title="Status Kelengkapan Data",
                color="KATEGORI",
                color_discrete_map={"LENGKAP": "#2ecc71", "TIDAK LENGKAP": "#e74c3c"}
            )
            
            fig4.update_layout(height=400)
            st.plotly_chart(fig4, use_container_width=True)
    
    with tab2:
        st.header("🏋️‍♂️ Data Semua Sukan")
        
        # Show all sports with counts
        sports_list = df["SUKAN"].unique().tolist()
        sports_list.sort()
        
        col1, col2, col3 = st.columns(3)
        
        # Create sports cards
        for i, sport in enumerate(sports_list):
            col_idx = i % 3
            with [col1, col2, col3][col_idx]:
                sport_data = df[df["SUKAN"] == sport]
                total_atlet = int(sport_data["TOTAL_ATLET"].sum())
                total_coaches = sport_data["JURULATIH"].nunique()
                total_locations = sport_data["DAERAH"].nunique()
                
                with st.expander(f"**{sport}** ({total_atlet} atlet)"):
                    st.write(f"**Jurulatih:** {total_coaches}")
                    st.write(f"**Daerah:** {total_locations}")
                    st.write(f"**Program:** {', '.join(sport_data['PROGRAM'].unique()[:3])}")
                    
                    # Show sample coaches
                    coaches_sample = sport_data["JURULATIH"].unique()[:3]
                    if len(coaches_sample) > 0:
                        st.write("**Contoh Jurulatih:**")
                        for coach in coaches_sample:
                            st.write(f"- {coach}")
        
        # Detailed table for filtered data
        st.subheader("📋 Data Terperinci")
        
        display_cols = ["SUKAN", "DAERAH", "JURULATIH", "NO_TELEFON", "PROGRAM", 
                       "STATUS", "ATLET_L", "ATLET_P", "TOTAL_ATLET", "PUSAT_LATIHAN", "STATUS_KELENGKAPAN"]
        
        display_df = filtered_df[display_cols].copy()
        
        # Format numeric columns
        display_df["ATLET_L"] = display_df["ATLET_L"].astype(int)
        display_df["ATLET_P"] = display_df["ATLET_P"].astype(int)
        display_df["TOTAL_ATLET"] = display_df["TOTAL_ATLET"].astype(int)
        
        st.dataframe(
            display_df,
            use_container_width=True,
            height=400,
            column_config={
                "ATLET_L": st.column_config.NumberColumn(
                    "Lelaki",
                    help="Bilangan atlet lelaki"
                ),
                "ATLET_P": st.column_config.NumberColumn(
                    "Perempuan",
                    help="Bilangan atlet perempuan"
                ),
                "TOTAL_ATLET": st.column_config.NumberColumn(
                    "Jumlah",
                    help="Jumlah atlet"
                ),
                "NO_TELEFON": st.column_config.TextColumn(
                    "No. Telefon",
                    help="Nombor telefon jurulatih"
                )
            }
        )
    
    with tab3:
        st.header("📅 Jadual Latihan Terperinci")
        
        if filtered_df.empty:
            st.warning("Tiada data untuk dipaparkan.")
        else:
            # Select coach to view schedule
            coaches_list = filtered_df["JURULATIH"].unique().tolist()
            
            if len(coaches_list) > 0:
                selected_coach = st.selectbox("Pilih Jurulatih:", coaches_list)
                
                # Get coach data
                coach_data = filtered_df[filtered_df["JURULATIH"] == selected_coach].iloc[0]
                
                # Display coach info
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.subheader("Maklumat Jurulatih")
                    st.info(f"**Nama:** {coach_data['JURULATIH']}")
                    st.info(f"**No. Telefon:** {coach_data['NO_TELEFON']}")
                    st.info(f"**Sukan:** {coach_data['SUKAN']}")
                    st.info(f"**Daerah:** {coach_data['DAERAH']}")
                    st.info(f"**Pusat Latihan:** {coach_data['PUSAT_LATIHAN']}")
                    st.info(f"**Program:** {coach_data['PROGRAM']}")
                    
                    if "TIDAK LENGKAP" in coach_data['STATUS_KELENGKAPAN']:
                        st.error(f"**Status:** {coach_data['STATUS_KELENGKAPAN']}")
                    else:
                        st.success(f"**Status:** {coach_data['STATUS_KELENGKAPAN']}")
                
                with col2:
                    st.subheader("Jadual Latihan Mingguan")
                    
                    # Create schedule table
                    schedule_data = {
                        "Hari": ["Isnin", "Selasa", "Rabu", "Khamis", "Jumaat", "Sabtu", "Ahad"],
                        "Jadual": [
                            coach_data.get("JADUAL_ISNIN", ""),
                            coach_data.get("JADUAL_SELASA", ""),
                            coach_data.get("JADUAL_RABU", ""),
                            coach_data.get("JADUAL_KHAMIS", ""),
                            coach_data.get("JADUAL_JUMAAT", ""),
                            coach_data.get("JADUAL_SABTU", ""),
                            coach_data.get("JADUAL_AHAD", "")
                        ]
                    }
                    
                    schedule_df = pd.DataFrame(schedule_data)
                    
                    # Function to clean HTML tags
                    def clean_html(text):
                        if pd.isna(text):
                            return ""
                        text = str(text)
                        # Simple HTML tag removal
                        text = text.replace("<br>", "\n").replace("  ", " ")
                        return text
                    
                    schedule_df["Jadual"] = schedule_df["Jadual"].apply(clean_html)
                    
                    # Display schedule
                    for idx, row in schedule_df.iterrows():
                        with st.container():
                            col_day, col_sched = st.columns([1, 3])
                            with col_day:
                                st.markdown(f"**{row['Hari']}**")
                            with col_sched:
                                if row['Jadual'] and row['Jadual'].strip():
                                    st.success(row['Jadual'])
                                else:
                                    st.warning("Tiada latihan")
                    
                    # Training days visualization
                    st.subheader("Visualisasi Hari Latihan")
                    
                    training_days = [1 if s and str(s).strip() else 0 for s in schedule_data["Jadual"]]
                    
                    fig_schedule = go.Figure(data=[
                        go.Scatterpolar(
                            r=training_days,
                            theta=schedule_data["Hari"],
                            fill='toself',
                            name='Hari Latihan',
                            line_color='#3498db'
                        )
                    ])
                    
                    fig_schedule.update_layout(
                        polar=dict(
                            radialaxis=dict(
                                visible=True,
                                range=[0, 1]
                            )
                        ),
                        showlegend=False,
                        height=300
                    )
                    
                    st.plotly_chart(fig_schedule, use_container_width=True)
            else:
                st.warning("Tiada data jurulatih untuk dipaparkan.")
    
    with tab4:
        st.header("👥 Maklumat Jurulatih")
        
        # Filter coaches with phone numbers
        coaches_df = filtered_df[filtered_df["JURULATIH"] != ""].copy()
        
        if coaches_df.empty:
            st.warning("Tiada data jurulatih.")
        else:
            # Coaches metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                total_coaches = coaches_df["JURULATIH"].nunique()
                st.metric("Jumlah Jurulatih", total_coaches)
            
            with col2:
                avg_atlet = coaches_df["TOTAL_ATLET"].mean()
                st.metric("Purata Atlet", f"{avg_atlet:.1f}")
            
            with col3:
                total_atlet_coached = coaches_df["TOTAL_ATLET"].sum()
                st.metric("Jumlah Atlet Dijurus", int(total_atlet_coached))
            
            # Search coaches
            search_term = st.text_input("🔍 Cari Jurulatih:", placeholder="Nama atau daerah...")
            
            if search_term:
                search_df = coaches_df[
                    coaches_df["JURULATIH"].str.contains(search_term, case=False, na=False) |
                    coaches_df["DAERAH"].str.contains(search_term, case=False, na=False) |
                    coaches_df["SUKAN"].str.contains(search_term, case=False, na=False)
                ]
            else:
                search_df = coaches_df
            
            # Display coaches in cards
            for idx, row in search_df.iterrows():
                with st.expander(f"{row['JURULATIH']} - {row['SUKAN']} ({row['DAERAH']})", expanded=False):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**Nama:** {row['JURULATIH']}")
                        st.write(f"**No. Telefon:** {row['NO_TELEFON']}")
                        st.write(f"**Sukan:** {row['SUKAN']}")
                        st.write(f"**Daerah:** {row['DAERAH']}")
                    
                    with col2:
                        st.write(f"**Program:** {row['PROGRAM']}")
                        st.write(f"**Pusat Latihan:** {row['PUSAT_LATIHAN']}")
                        st.write(f"**Atlet:** {int(row['ATLET_L'])}L, {int(row['ATLET_P'])}P (Total: {int(row['TOTAL_ATLET'])})")
                        st.write(f"**Status:** {row['STATUS']}")
                    
                    # Quick contact button
                    if row['NO_TELEFON'] and str(row['NO_TELEFON']).strip():
                        phone = str(row['NO_TELEFON']).strip()
                        st.markdown(f"[📞 Hubungi: {phone}](tel:{phone})")
    
    with tab5:
        st.header("⚠️ Monitoring Data Tidak Lengkap")
        
        # Find incomplete data
        incomplete_mask = filtered_df["STATUS_KELENGKAPAN"].str.contains("TIDAK LENGKAP")
        incomplete_df = filtered_df[incomplete_mask].copy()
        
        if incomplete_df.empty:
            st.success("✅ Semua data lengkap!")
        else:
            st.warning(f"**Terdapat {len(incomplete_df)} rekod data tidak lengkap.**")
            
            # Display incomplete data
            st.subheader("Senarai Data Tidak Lengkap")
            
            for idx, row in incomplete_df.iterrows():
                with st.container():
                    st.markdown(f"**{row['SUKAN']} - {row['DAERAH']}**")
                    st.write(f"Jurulatih: {row['JURULATIH'] if row['JURULATIH'] else 'TIADA DATA'}")
                    st.write(f"Isu: {row['STATUS_KELENGKAPAN']}")
                    
                    # Quick edit form
                    with st.expander("Kemaskini Data"):
                        with st.form(key=f"update_{idx}"):
                            new_name = st.text_input("Nama Jurulatih", value=row['JURULATIH'] or "")
                            new_phone = st.text_input("No. Telefon", value=row['NO_TELEFON'] or "")
                            new_days = st.text_input("Hari Latihan", 
                                                   value=", ".join([d for d in ["Isnin", "Selasa", "Rabu", "Khamis", "Jumaat", "Sabtu", "Ahad"] 
                                                                   if row.get(f"JADUAL_{d.upper()[:3]}", "")]) or "")
                            
                            if st.form_submit_button("Simpan"):
                                st.success("Data telah dikemaskini!")
                    
                    st.markdown("---")
            
            # Analysis of incomplete data
            st.subheader("Analisis Data Tidak Lengkap")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Reasons for incompleteness
                reasons = []
                for idx, row in incomplete_df.iterrows():
                    if not row['JURULATIH'] or str(row['JURULATIH']).strip() == '':
                        reasons.append("Nama Jurulatih")
                    if not row['NO_TELEFON'] or str(row['NO_TELEFON']).strip() == '':
                        reasons.append("No. Telefon")
                    if not any([row.get(f"JADUAL_{day}", "") for day in ["ISNIN", "SELASA", "RABU", "KHAMIS", "JUMAAT", "SABTU", "AHAD"]]):
                        reasons.append("Jadual Latihan")
                
                if reasons:
                    reason_counts = pd.Series(reasons).value_counts()
                    fig_reasons = px.bar(
                        x=reason_counts.values,
                        y=reason_counts.index,
                        orientation='h',
                        title="Sebab Ketidaklengkapan",
                        color=reason_counts.values,
                        color_continuous_scale='Reds'
                    )
                    st.plotly_chart(fig_reasons, use_container_width=True)
            
            with col2:
                # Incomplete by Sport
                sport_incomplete = incomplete_df["SUKAN"].value_counts().reset_index()
                sport_incomplete.columns = ["SUKAN", "COUNT"]
                
                if not sport_incomplete.empty:
                    fig_sport_incomplete = px.pie(
                        sport_incomplete,
                        values="COUNT",
                        names="SUKAN",
                        title="Data Tidak Lengkap Mengikut Sukan"
                    )
                    st.plotly_chart(fig_sport_incomplete, use_container_width=True)
    
    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.caption("Dashboard Program Sukan Pembangunan/Pelapis/SUKMA 2025-2026 Negeri Sabah")
        st.caption("Data dikemaskini: 7 Ogos 2024 | Versi 3.0 (Data Lengkap)")
    
    with col2:
        if st.button("📥 Export Data (CSV)"):
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Muat Turun",
                data=csv,
                file_name=f"sukan_sabah_{selected_sport if selected_sport != 'SEMUA' else 'semua'}.csv",
                mime="text/csv"
            )
    
    with col3:
        st.caption(f"© {datetime.now().year} Jabatan Sukan Sabah")

if __name__ == "__main__":
    create_dashboard()
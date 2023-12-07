import streamlit as st
from actions.app import *
import math

# import matplotlib.pyplot as plt
# import seaborn as sns


st.set_page_config(page_title="Dashboard", layout="wide")
st.markdown(
    "<h1 style='color:#0b4eab;font-size:36px;border-radius:10px;'>Dashboard | Retail Sales Prediction Model </h1>",
    unsafe_allow_html=True,
)


# pickle_in = open("models/xgboost.pkl", "rb")
# calculator = pickle.load(pickle_in)


# def prediction(
#     DayOfWeek,
#     Customers,
#     Open,
#     Promo,
#     StateHoliday,
#     SchoolHoliday,
#     StoreType,
#     Assortment,
#     CompetitionDistance,
#     CompetitionOpenSinceMonth,
#     CompetitionOpenSinceYear,
#     Promo2,
#     Promo2SinceWeek,
#     PromoInterval_0,
#     PromoInterval_Feb_May_Aug_Nov,
#     PromoInterval_Jan_Apr_Jul_Oct,
#     PromoInterval_Mar_Jun_Sept_Dec,
# ):
#     if DayOfWeek == "minggu":
#         DayOfWeek = 1
#     elif DayOfWeek == "senin":
#         DayOfWeek = 2
#     elif DayOfWeek == "selasa":
#         DayOfWeek = 3
#     elif DayOfWeek == "rabu":
#         DayOfWeek = 4
#     elif DayOfWeek == "kamis":
#         DayOfWeek = 5
#     elif DayOfWeek == "jum'at":
#         DayOfWeek = 6
#     else:
#         DayOfWeek = 7

#     if StoreType == "a":
#         StoreType = 1
#     elif StoreType == "b":
#         StoreType = 2
#     elif StoreType == "c":
#         StoreType = 3
#     else:
#         StoreType = 4

#     if Assortment == "a":
#         Assortment = 0
#     elif Assortment == "b":
#         Assortment = 1
#     else:
#         Assortment = 2

#     Promo = 1 if Promo == "ya" else 0
#     SchoolHoliday = 1 if SchoolHoliday == "ya" else 0
#     StateHoliday = 1 if StateHoliday == "ya" else 0
#     Promo2 = 1 if Promo2 == "ya" else 0
#     Promo2SinceWeek = 1 if Promo2SinceWeek == "ya" else 0
#     PromoInterval_0 = 1 if PromoInterval_0 == "ya" else 0
#     PromoInterval_Feb_May_Aug_Nov = 1 if PromoInterval_Feb_May_Aug_Nov == "ya" else 0
#     PromoInterval_Jan_Apr_Jul_Oct = 1 if PromoInterval_Jan_Apr_Jul_Oct == "ya" else 0
#     PromoInterval_Mar_Jun_Sept_Dec = 1 if PromoInterval_Mar_Jun_Sept_Dec == "ya" else 0

#     # Making predictions
#     prediction = calculator.predict(
#         [
#             [
#                 DayOfWeek,
#                 Customers,
#                 Open,
#                 Promo,
#                 StateHoliday,
#                 SchoolHoliday,
#                 StoreType,
#                 Assortment,
#                 CompetitionDistance,
#                 CompetitionOpenSinceMonth,
#                 CompetitionOpenSinceYear,
#                 Promo2,
#                 Promo2SinceWeek,
#                 PromoInterval_0,
#                 PromoInterval_Feb_May_Aug_Nov,
#                 PromoInterval_Jan_Apr_Jul_Oct,
#                 PromoInterval_Mar_Jun_Sept_Dec,
#             ]
#         ]
#     )

#     return prediction


# def visualize_feature_importance():
#     # Gantilah dengan dataset atau fitur yang sesuai dengan model Anda
#     # Contoh menggunakan feature_importances_ dari model RandomForest
#     feature_importance = calculator.feature_importances_
#     feature_names = [
#         "DayOfWeek",
#         "Customers",
#         "Open",
#         "Promo",
#         "StateHoliday",
#         "SchoolHoliday",
#         "StoreType",
#         "Assortment",
#         "CompetitionDistance",
#         "CompetitionOpenSinceMonth",
#         "CompetitionOpenSinceYear",
#         "Promo2",
#         "Promo2SinceWeek",
#         "PromoInterval_0",
#         "PromoInterval_Feb,May,Aug,Nov",
#         "PromoInterval_Jan,Apr,Jul,Oct",
#         "PromoInterval_Mar,Jun,Sept,Dec",
#     ]  # Gantilah dengan nama fitur sesuai dataset Anda

#     # Visualisasi menggunakan bar plot
#     # fig, ax = plt.subplots()
#     st.set_option("deprecation.showPyplotGlobalUse", False)
#     plt.figure(figsize=(8, 6))
#     sns.barplot(x=feature_importance, y=feature_names)
#     plt.title("Fitur Penting")
#     plt.xlabel("Skor Fitur Penting")
#     plt.ylabel("Fitur")
#     st.pyplot()


def main():
    html_temp = """ 
    
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    # Sidebar dengan input pengguna
    menu = st.sidebar.radio("Menu", ["Prediksi", "Visualisasi Fitur Penting"])

    if menu == "Prediksi":
        DayOfWeek = st.selectbox(
            "Masukkan Hari",
            ("senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "minggu"),
        )
        Customers = st.number_input("Jumlah pelanggan")
        StoreType = st.selectbox("pilih tipe toko", ("a", "b", "c", "d"))
        Promo = st.selectbox("apakah kamu dalam promo ?", ("ya", "tidak"))
        StateHoliday = st.selectbox("Apakah libur nasional ?", ("ya", "tidak"))
        SchoolHoliday = st.selectbox("Apakah libur sekolah ?", ("ya", "tidak"))
        Assortment = st.selectbox("Pilih jenis", ("a", "b", "c"))
        CompetitionDistance = st.number_input("Masukan jarak kompetisi")
        CompetitionOpenSinceMonth = st.number_input(
            "Masukan jarak kompetisi baru bulan ini"
        )
        CompetitionOpenSinceYear = st.number_input(
            "Masukan jarak kompetisi baru tahun ini"
        )
        Promo2 = st.selectbox("Apakah ada promo ke dua ?", ("ya", "tidak"))
        Promo2SinceWeek = st.selectbox(
            "Apakah kamu ada didalam promo minggu ini", ("ya", "tidak")
        )
        result = ""
        Open = 1
        PromoInterval_0 = st.selectbox("Apakah ada interval promo ?", ("ya", "tidak"))
        PromoInterval_Feb_May_Aug_Nov = st.selectbox(
            "Apakah ada interval promo di bulan ini (Feb, May, Aug, Nov) ?",
            ("ya", "tidak"),
        )
        PromoInterval_Jan_Apr_Jul_Oct = st.selectbox(
            "Apakah ada interval promo di bulan ini (Jan, Apr, Jul, Oct)?",
            ("ya", "tidak"),
        )
        PromoInterval_Mar_Jun_Sept_Dec = st.selectbox(
            "Apakah ada interval promo di bulan ini (Mar, Jun, Sept, Dec)?",
            ("ya", "tidak"),
        )

        if st.button("Predict"):
            result = prediction(
                DayOfWeek,
                Customers,
                Open,
                Promo,
                StateHoliday,
                SchoolHoliday,
                StoreType,
                Assortment,
                CompetitionDistance,
                CompetitionOpenSinceMonth,
                CompetitionOpenSinceYear,
                Promo2,
                Promo2SinceWeek,
                PromoInterval_0,
                PromoInterval_Feb_May_Aug_Nov,
                PromoInterval_Jan_Apr_Jul_Oct,
                PromoInterval_Mar_Jun_Sept_Dec,
            )
            st.success("Perkiraan terjual adalah {}".format(math.ceil(result[0])))
    else:
        visualize_feature_importance()


if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import textwrap
import joblib


st.set_page_config(page_title="Dropout Detection and Dashboard Monitoring", layout="wide")

# ===============================
# Load Data
# ===============================
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv", delimiter=';')
    # Map numerical categorical features
    application_mode_map = {
    1: "1st phase - general contingent",
    2: "Ordinance No. 612/93",
    5: "1st phase - special contingent (Azores Island)",
    7: "Holders of other higher courses",
    10: "Ordinance No. 854-B/99",
    15: "International student (bachelor)",
    16: "1st phase - special contingent (Madeira Island)",
    17: "2nd phase - general contingent",
    18: "3rd phase - general contingent",
    26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
    27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
    39: "Over 23 years old",
    42: "Transfer",
    43: "Change of course",
    44: "Technological specialization diploma holders",
    51: "Change of institution/course",
    53: "Short cycle diploma holders",
    57: "Change of institution/course (International)"
        }
    course_map = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)"
        }
    Previous_qualification_map = {
    1: "Secondary education",
    2: "Higher education - bachelor's degree",
    3: "Higher education - degree",
    4: "Higher education - master's",
    5: "Higher education - doctorate",
    6: "Frequency of higher education",
    9: "12th year of schooling - not completed",
    10: "11th year of schooling - not completed",
    12: "Other - 11th year of schooling",
    14: "10th year of schooling",
    15: "10th year of schooling - not completed",
    19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
    38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    42: "Professional higher technical course",
    43: "Higher education - master (2nd cycle)"
        }
    yesno_map = {
    1: "yes",
    0: "no"
        }
    gender_map = {
    1: "male",
    0: "female"
        }
    
    df['Tuition_fees_up_to_date'] = df['Tuition_fees_up_to_date'].map(yesno_map)
    df['Application_mode'] = df['Application_mode'].map(application_mode_map)
    df['Course'] = df['Course'].map(course_map)
    df['Previous_qualification'] = df['Previous_qualification'].map(Previous_qualification_map)
    df['Scholarship_holder'] = df['Scholarship_holder'].map(yesno_map)
    df['Debtor'] = df['Debtor'].map(yesno_map)
    df['Gender'] = df['Gender'].map(gender_map)
    df['Target'] = df['Status'].map({
        'Dropout': 1,
        'Graduate': 0,
        'Enrolled': 0
        })
    df['Status'] = df['Status'].map({
        'Dropout': 'DO',
        'Graduate': 'Stay',
        'Enrolled': 'Stay'
        })
    categorical_features = [
        'Tuition_fees_up_to_date', 'Application_mode', 'Course', 
        'Scholarship_holder', 'Debtor', 'Previous_qualification', 'Gender']
    numerical_features = [
        'Age_at_enrollment', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade'
    ]
    df = df[categorical_features + numerical_features + ['Status']]
    return df

df = load_data()

# ===============================
# Sidebar
# ===============================
st.sidebar.title("📋 Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Ikhtisar", "Fitur Kategorikal", "Fitur Numerikal", "Prediksi Dropout"])
palette = {'DO': '#FF6B6B', 'Stay': '#51CF66'}

# ===============================
# Halaman 1: Ikhtisar
# ===============================
if page == "Ikhtisar":
    st.title("📊 Ikhtisar Dropout Mahasiswa")

    total = len(df)
    dropout = len(df[df['Status'] == 'DO'])
    stay = len(df[df['Status'] == 'Stay'])
    dropout_rate = (dropout / total) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Jumlah Mahasiswa", total)
    col2.metric("Dropout", dropout)
    col3.metric("Tingkat Dropout", f"{dropout_rate:.2f}%")

    st.markdown("### 📉 Perbandingan Mahasiswa Dropout dan Bertahan")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=df, x='Status', palette=palette)
    for container in ax1.containers:
        ax1.bar_label(container, fmt='%d', label_type='edge', padding=0.5)
    ax1.set_xticklabels(['Dropout', 'Bertahan'])
    st.pyplot(fig1)

# ===============================
# Halaman 2: Fitur Kategorikal
# ===============================
elif page == "Fitur Kategorikal":
    st.title("📌 Visualisasi Fitur Kategorikal")

    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    if 'Status' in categorical_cols:
        categorical_cols.remove('Status')

    selected_cat = st.selectbox("Pilih fitur kategorikal:", categorical_cols)

    fig, ax = plt.subplots(figsize=(10, 6))

    if selected_cat in ['Application_mode', 'Course', 'Previous_qualification']:
        # Ambil hanya top 5 kategori dengan dropout (DO) terbanyak
        top5_do = (
            df[df['Status'] == 'DO'][selected_cat]
            .value_counts()
            .nlargest(5)
            .index
        )
        df_filtered = df[df[selected_cat].isin(top5_do)]

        # Horizontal bar chart
        sns.countplot(data=df_filtered, y=selected_cat, hue='Status', palette=palette, ax=ax)
        ax.set_xlabel("Jumlah")
        # Wrap label Y agar tidak terlalu panjang
        ax.set_yticklabels([textwrap.fill(label.get_text(), 10) for label in ax.get_yticklabels()])
        ax.set_ylabel(selected_cat)
        ax.set_title(f'Top 5 Status DO Mahasiswa berdasarkan {selected_cat}', loc='center')
    else:
        # Vertical bar chart
        sns.countplot(data=df, x=selected_cat, hue='Status', palette=palette, ax=ax)
        ax.set_xlabel(selected_cat)
        ax.set_ylabel("Jumlah")
        plt.xticks(rotation=0, ha='right')
        ax.set_title(f'Status Mahasiswa berdasarkan {selected_cat}', loc='center')

    # Tambahkan label ke bar
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', padding=0.1)

    plt.tight_layout()
    st.pyplot(fig)

# ===============================
# Halaman 3: Fitur Numerikal
# ===============================
elif page == "Fitur Numerikal":
    st.title("📈 Visualisasi Fitur Numerikal")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    selected_num = st.selectbox("Pilih fitur numerikal:", numeric_cols)

    try:
        # Cek apakah kolom yang dipilih perlu dibinning
        if selected_num in ['Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_grade']:
            # Binning ke dalam 4 kuartil
            bin_col = selected_num + "_bin"
            df[bin_col] = pd.qcut(
                df[selected_num],
                q=4,
                labels=["Very Low", "Low", "High", "Very High"]
            )

            # Hitung dropout rate per bin
            grouped = df.groupby(bin_col)['Status'].apply(lambda x: (x == 'DO').mean()).reset_index()
            grouped = grouped.sort_values(by='Status', ascending=False).reset_index(drop=True)
            
            colors = sns.color_palette("Reds", n_colors=len(grouped))
            
            order = grouped[bin_col].tolist()


            fig3, ax3 = plt.subplots(figsize=(10, 5))
            sns.barplot(data=grouped, x=bin_col, y='Status', palette=colors, ax=ax3, order=order)

            ax3.set_ylabel("Dropout Rate")
            ax3.set_xlabel(selected_num.replace("_", " "))
            ax3.set_title(f'Tingkat Dropout berdasarkan {selected_num}')
            st.pyplot(fig3)
        else:
            # Jika bukan kolom yang dibinning, gunakan line plot seperti biasa
            grouped = df.groupby(selected_num)['Status'].apply(lambda x: (x == 'DO').mean()).reset_index()

            fig3, ax3 = plt.subplots(figsize=(10, 5))
            sns.lineplot(data=grouped, x=selected_num, y='Status', marker='o', ax=ax3)

            ax3.set_ylabel("Dropout Rate")
            ax3.set_title(f'Tingkat Dropout berdasarkan {selected_num}')
            ax3.grid(True)
            st.pyplot(fig3)

    except Exception as e:
        st.warning(f"Tidak dapat menampilkan grafik: {e}")

# ===============================
# Halaman 4: Prediksi Dropout
# ===============================
elif page == "Prediksi Dropout":
    st.title("📌 Prediksi Dropout Mahasiswa")

    # Load model terbaik
    try:
        best_model = joblib.load("logistic regression_model.pkl")
    except FileNotFoundError:
        st.error("Model belum dilatih. Silakan jalankan proses pelatihan terlebih dahulu.")
        st.stop()

    st.markdown("Masukkan data berikut untuk memprediksi apakah seorang siswa akan dropout:")

    # Input Kategorikal
    Tuition_fees_up_to_date = st.selectbox("Apakah pembayaran kuliah up to date?", df['Tuition_fees_up_to_date'].dropna().unique())
    Application_mode = st.selectbox("Mode aplikasi", df['Application_mode'].dropna().unique())
    Course = st.selectbox("Program Studi", df['Course'].dropna().unique())
    Scholarship_holder = st.selectbox("Penerima beasiswa?", df['Scholarship_holder'].dropna().unique())
    Debtor = st.selectbox("Apakah memiliki hutang?", df['Debtor'].dropna().unique())
    Previous_qualification = st.selectbox("Kualifikasi sebelumnya", df['Previous_qualification'].dropna().unique())
    Gender = st.selectbox("Jenis Kelamin", df['Gender'].dropna().unique())

    # Input Numerikal
    Age_at_enrollment = st.number_input("Usia saat mendaftar", min_value=16, max_value=70, value=18)
    Curricular_units_1st_sem_approved = st.number_input("Unit disetujui semester 1", min_value=0)
    Curricular_units_1st_sem_grade = st.number_input("Nilai semester 1", min_value=0.0, format="%.2f")
    Curricular_units_2nd_sem_approved = st.number_input("Unit disetujui semester 2", min_value=0)
    Curricular_units_2nd_sem_grade = st.number_input("Nilai semester 2", min_value=0.0, format="%.2f")

    if st.button("Prediksi"):
        input_data = pd.DataFrame([{
            'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
            'Application_mode': Application_mode,
            'Course': Course,
            'Scholarship_holder': Scholarship_holder,
            'Debtor': Debtor,
            'Previous_qualification': Previous_qualification,
            'Gender': Gender,
            'Age_at_enrollment': Age_at_enrollment,
            'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
            'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
            'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
            'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
        }])

        prediction = best_model.predict(input_data)[0]
        proba = best_model.predict_proba(input_data)[0]

        st.markdown(f"### 🎯 Hasil Prediksi")
        st.write(f"Prediksi: **{'Dropout' if prediction == 1 else 'Bertahan'}**")
        st.write(f"Probabilitas Dropout: **{proba[1]:.2%}**")
        st.write(f"Probabilitas Bertahan: **{proba[0]:.2%}**")

        if prediction == 1:
            st.error("⚠️ Berdasarkan data yang dimasukkan, siswa **berpotensi dropout**.")
        else:
            st.success("✅ Berdasarkan data yang dimasukkan, siswa **berpotensi bertahan**.")
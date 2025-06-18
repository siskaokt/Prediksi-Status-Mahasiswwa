import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.pkl')

st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="wide")

st.title("🎓 Prediksi Status Akhir Mahasiswa")

# Informasi Umum
st.markdown("### 👤 Informasi Umum")
col1, col2, col3 = st.columns(3)

with col1:
    # Marital Status
    marital_status_options = {
        "0 - Single": 0,
        "1 - Married": 1,
        "2 - Widower": 2,
        "3 - Divorced": 3,
        "4 - Facto Union": 4,
        "5 - Legally Seperated": 5
    }

    Marital_status_label = st.selectbox("Status Pernikahan", list(marital_status_options.keys()))
    Marital_status = marital_status_options[Marital_status_label]

    # Application Mode
    application_mode_options = {
    "1 - 1st phase - general contingent": 1,
    "2 - Ordinance No. 612/93": 2,
    "5 - 1st phase - special contingent (Azores Island)": 5,
    "7 - Holders of other higher courses": 7,
    "10 - Ordinance No. 854-B/99": 10,
    "15 - International student (bachelor)": 15,
    "16 - 1st phase - special contingent (Madeira Island)": 16,
    "17 - 2nd phase - general contingent": 17,
    "18 - 3rd phase - general contingent": 18,
    "26 - Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
    "27 - Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
    "39 - Over 23 years old": 39,
    "42 - Transfer": 42,
    "43 - Change of course": 43,
    "44 - Technological specialization diploma holders": 44,
    "51 - Change of institution/course": 51,
    "53 - Short cycle diploma holders": 53,
    "57 - Change of institution/course (International)": 57,
}
    Application_mode_label = st.selectbox("Mode Aplikasi", list(application_mode_options.keys()))
    Application_mode = application_mode_options[Application_mode_label]

    # Aplication Order
    Application_order = st.number_input("Urutan Pilihan Masuk", 0, 10, 0)

with col2:
    # Course Taken
    course_options = {
    "33 - Biofuel Production Technologies": 33,
    "171 - Animation and Multimedia Design": 171,
    "8014 - Social Service (evening attendance)": 8014,
    "9003 - Agronomy": 9003,
    "9070 - Communication Design": 9070,
    "9085 - Veterinary Nursing": 9085,
    "9119 - Informatics Engineering": 9119,
    "9130 - Equinculture": 9130,
    "9147 - Management": 9147,
    "9238 - Social Service": 9238,
    "9254 - Tourism": 9254,
    "9500 - Nursing": 9500,
    "9556 - Oral Hygiene": 9556,
    "9670 - Advertising and Marketing Management": 9670,
    "9773 - Journalism and Communication": 9773,
    "9853 - Basic Education": 9853,
    "9991 - Management (evening attendance)": 9991,
}

    Course_label = st.selectbox("Program Studi", list(course_options.keys()))
    Course = course_options[Course_label]

    # Class type
    attendance_options = {
    "Siang (Daytime)": 1,
    "Malam (Evening)": 0
}
    attendance_label = st.selectbox("Tipe Kelas", list(attendance_options.keys()))
    Daytime_evening_attendance = attendance_options[attendance_label]

    # Nationality
    nationality_options = {
    "Portuguese": 1,
    "German": 2,
    "Spanish": 6,
    "Italian": 11,
    "Dutch": 13,
    "English": 14,
    "Lithuanian": 17,
    "Angolan": 21,
    "Cape Verdean": 22,
    "Guinean": 24,
    "Mozambican": 25,
    "Santomean": 26,
    "Turkish": 32,
    "Brazilian": 41,
    "Romanian": 62,
    "Moldova (Republic of)": 100,
    "Mexican": 101,
    "Ukrainian": 103,
    "Russian": 105,
    "Cuban": 108,
    "Colombian": 109
}

    nationality_label = st.selectbox("Kewarganegaraan Mahasiswa", list(nationality_options.keys()))
    Nacionality = nationality_options[nationality_label]

with col3:
    # Gender
    gender_options = {
    "Perempuan": 0,
    "Laki-laki": 1
}
    gender_label = st.selectbox("Jenis Kelamin", list(gender_options.keys()))
    Gender = gender_options[gender_label]

    # Umur
    Age_at_enrollment = st.number_input("Usia Saat Masuk", 15, 70, 18)
    
    # Admission grade
    Admission_grade = st.number_input("Nilai Ujian Masuk", min_value=0.0, max_value=200.0, value=100.0)

    if Admission_grade < 0 or Admission_grade > 200:
        st.warning("⚠️ Nilai ujian masuk harus berada antara 0 hingga 200.")

st.markdown("---")

# Pendidikan Mahasiswa
st.markdown("### 📃 Pendidikan dan Beasiswa")
col4, col5 = st.columns(2)
with col4:
     # Pendidikan Terakhir
    previous_qualification_options = {
        "1 - Secondary education": 1,
        "2 - Higher education - bachelor's degree": 2,
        "3 - Higher education - degree": 3,
        "4 - Higher education - master's": 4,
        "5 - Higher education - doctorate": 5,
        "6 - Frequency of higher education": 6,
        "9 - 12th year of schooling - not completed": 9,
        "10 - 11th year of schooling - not completed": 10,
        "12 - Other - 11th year of schooling": 12,
        "14 - 10th year of schooling": 14,
        "15 - 10th year of schooling - not completed": 15,
        "19 - Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
        "38 - Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
        "39 - Technological specialization course": 39,
        "40 - Higher education - degree (1st cycle)": 40,
        "42 - Professional higher technical course": 42,
        "43 - Higher education - master (2nd cycle)": 43
    }
    Previous_qualification_label = st.selectbox("Pendidikan Terakhir", list(previous_qualification_options.keys()))
    Previous_qualification = previous_qualification_options[Previous_qualification_label]

    # Nilai Pendidikan Terakhir
    Previous_qualification_grade = st.number_input("Nilai Pendidikan Terakhir", 0.0, 200.0, 100.0)

with col5:
    # Penerima beasiswa
    scholarship_option = st.selectbox("Apakah Mahasiswa Penerima Beasiswa?", ["Tidak", "Ya"])
    Scholarship_holder = 1 if scholarship_option == "Ya" else 0

    # Mahasiswa Internasional
    international_option = st.selectbox("Apakah Mahasiswa Internasional?", ["Tidak", "Ya"])
    International = 1 if international_option == "Ya" else 0


st.markdown("---")

# Informasi Keluarga
st.markdown("### 👨‍👩‍👧‍👦  Latar Belakang Keluarga")
col6, col7 = st.columns(2)
with col6:
    # Pendidikan ibu
    mothers_qualification_dict = {
    "1 - Secondary Education - 12th Year or Eq.": 1,
    "2 - Higher Ed - Bachelor's": 2,
    "3 - Higher Ed - Degree": 3,
    "4 - Higher Ed - Master's": 4,
    "5 - Higher Ed - Doctorate": 5,
    "6 - Frequency of Higher Ed": 6,
    "9 - 12th Year - Not Completed": 9,
    "10 - 11th Year - Not Completed": 10,
    "11 - 7th Year (Old)": 11,
    "12 - Other - 11th Year": 12,
    "14 - 10th Year": 14,
    "18 - General Commerce": 18,
    "19 - Basic Ed 3rd Cycle (9th-11th Year)": 19,
    "22 - Technical-professional course": 22,
    "26 - 7th year of schooling": 26,
    "27 - 2nd cycle general high school": 27,
    "29 - 9th Year - Not Completed": 29,
    "30 - 8th year": 30,
    "34 - Unknown": 34,
    "35 - Can't read or write": 35,
    "36 - Can read, no 4th year": 36,
    "37 - Basic Ed 1st Cycle (4th/5th)": 37,
    "38 - Basic Ed 2nd Cycle (6th-8th)": 38,
    "39 - Tech specialization course": 39,
    "40 - Higher Ed - Degree (1st Cycle)": 40,
    "41 - Specialized Higher Studies": 41,
    "42 - Prof. Higher Technical Course": 42,
    "43 - Higher Ed - Master (2nd Cycle)": 43,
    "44 - Higher Ed - Doctorate (3rd Cycle)": 44
}

    mothers_qualification_label = st.selectbox(
        "Pendidikan Ibu",
        list(mothers_qualification_dict.keys())
    )
    Mothers_qualification = mothers_qualification_dict[mothers_qualification_label]

    # Pendidikan ayah
    fathers_qualification_dict = {
    "1 - Secondary Education - 12th Year": 1,
    "2 - Higher Ed - Bachelor's": 2,
    "3 - Higher Ed - Degree": 3,
    "4 - Higher Ed - Master's": 4,
    "5 - Higher Ed - Doctorate": 5,
    "6 - Frequency of Higher Ed": 6,
    "9 - 12th Year - Not Completed": 9,
    "10 - 11th Year - Not Completed": 10,
    "11 - 7th Year (Old)": 11,
    "12 - Other - 11th Year": 12,
    "13 - 2nd Yr Complementary HS Course": 13,
    "14 - 10th Year": 14,
    "18 - General Commerce Course": 18,
    "19 - Basic Ed 3rd Cycle (9th-11th)": 19,
    "20 - Complementary High School": 20,
    "22 - Technical-professional Course": 22,
    "25 - Comp. HS - Not Completed": 25,
    "26 - 7th Year of Schooling": 26,
    "27 - 2nd Cycle General HS": 27,
    "29 - 9th Year - Not Completed": 29,
    "30 - 8th Year of Schooling": 30,
    "31 - General Admin & Commerce": 31,
    "33 - Supplementary Accounting & Admin": 33,
    "34 - Unknown": 34,
    "35 - Can't Read or Write": 35,
    "36 - Can Read, No 4th Yr": 36,
    "37 - Basic Ed 1st Cycle (4th/5th)": 37,
    "38 - Basic Ed 2nd Cycle (6th-8th)": 38,
    "39 - Tech Specialization Course": 39,
    "40 - Higher Ed Degree (1st Cycle)": 40,
    "41 - Specialized Higher Studies": 41,
    "42 - Prof. Higher Technical Course": 42,
    "43 - Higher Ed - Master (2nd Cycle)": 43,
    "44 - Higher Ed - Doctorate (3rd Cycle)": 44
}

    fathers_qualification_label = st.selectbox(
        "Pendidikan ayah",
        list(fathers_qualification_dict.keys())
    )
    Fathers_qualification = fathers_qualification_dict[fathers_qualification_label]
with col7:
    # Pekerjaan Ibu
    mothers_occupation_dict = {
    "0 - Student": 0,
    "1 - Legislative/Executive Power, Directors & Execs": 1,
    "2 - Intellectual & Scientific Specialists": 2,
    "3 - Intermediate Technicians & Professions": 3,
    "4 - Administrative Staff": 4,
    "5 - Personal Services, Security, Sales": 5,
    "6 - Agriculture/Fisheries/Forestry Skilled Workers": 6,
    "7 - Industry/Construction/Crafts Skilled Workers": 7,
    "8 - Machine Operators & Assemblers": 8,
    "9 - Unskilled Workers": 9,
    "10 - Armed Forces Professions": 10,
    "90 - Other Situation": 90,
    "99 - Blank": 99,
    "122 - Health Professionals": 122,
    "123 - Teachers": 123,
    "125 - ICT Specialists": 125,
    "131 - Science & Engineering Technicians": 131,
    "132 - Health Technicians": 132,
    "134 - Legal/Social/Cultural Technicians": 134,
    "141 - Office Workers & Secretaries": 141,
    "143 - Finance/Accounting/Data Staff": 143,
    "144 - Other Admin Support Staff": 144,
    "151 - Personal Service Workers": 151,
    "152 - Sellers": 152,
    "153 - Personal Care Workers": 153,
    "171 - Skilled Construction Workers (Non-Electrician)": 171,
    "173 - Precision, Jewelry, Artisan Workers": 173,
    "175 - Food/Wood/Clothing Craft Workers": 175,
    "191 - Cleaning Workers": 191,
    "192 - Unskilled Agri/Fishery/Forestry": 192,
    "193 - Unskilled Industry/Transport Workers": 193,
    "194 - Meal Preparation Assistants": 194
}

    mothers_occupation_label = st.selectbox(
        "Pekerjaan Ibu",
        list(mothers_occupation_dict.keys())
    )
    Mothers_occupation = mothers_occupation_dict[mothers_occupation_label]
    
    # Pekerjaan Ayah
    fathers_occupation_dict = {
    "0 - Student": 0,
    "1 - Legislative/Executive/Directors": 1,
    "2 - Intellectual/Scientific Specialists": 2,
    "3 - Intermediate Technicians/Professions": 3,
    "4 - Administrative Staff": 4,
    "5 - Services/Security/Sellers": 5,
    "6 - Farmers/Fishermen/Forestry": 6,
    "7 - Skilled Industry/Construction Workers": 7,
    "8 - Machine Operators & Assemblers": 8,
    "9 - Unskilled Workers": 9,
    "10 - Armed Forces Professions": 10,
    "90 - Other Situation": 90,
    "99 - (blank)": 99,
    "101 - Armed Forces Officers": 101,
    "102 - Armed Forces Sergeants": 102,
    "103 - Other Armed Forces Personnel": 103,
    "112 - Admin/Commercial Service Directors": 112,
    "114 - Hotel/Catering/Trade Directors": 114,
    "121 - Physical Sciences/Engineering Specialists": 121,
    "122 - Health Professionals": 122,
    "123 - Teachers": 123,
    "124 - Finance/Accounting/Public Relations": 124,
    "131 - Science & Engineering Technicians": 131,
    "132 - Health Technicians": 132,
    "134 - Legal/Social/Culture Technicians": 134,
    "135 - ICT Technicians": 135,
    "141 - Secretaries & Data Operators": 141,
    "143 - Finance/Statistical/Registry Staff": 143,
    "144 - Other Admin Support": 144,
    "151 - Personal Service Workers": 151,
    "152 - Sellers": 152,
    "153 - Personal Care Workers": 153,
    "154 - Protection/Security Services": 154,
    "161 - Market-Oriented Farmers": 161,
    "163 - Subsistence Farmers/Fishermen": 163,
    "171 - Construction Workers (non-electricians)": 171,
    "172 - Metalwork & Similar": 172,
    "174 - Electrical/Electronic Workers": 174,
    "175 - Food/Wood/Clothing/Crafts": 175,
    "181 - Fixed Plant/Machine Operators": 181,
    "182 - Assembly Workers": 182,
    "183 - Drivers & Equipment Operators": 183,
    "192 - Unskilled Agri/Fishery/Forestry": 192,
    "193 - Unskilled Construction/Transport": 193,
    "194 - Meal Prep Assistants": 194,
    "195 - Street Vendors/Service Providers": 195
}

    fathers_occupation_label = st.selectbox(
        "Pekerjaan Ayah",
        list(fathers_occupation_dict.keys())
    )
    Fathers_occupation = fathers_occupation_dict[fathers_occupation_label]

st.markdown("---")

# Semester 1
st.markdown("### 📚 Hasil Pembelajaran Semester 1")
col8, col9, col10 = st.columns(3)
with col8:
    Curricular_units_1st_sem_credited = st.number_input("1st Sem: SKS Diakui", 0, 30, 0)
    Curricular_units_1st_sem_enrolled = st.number_input("1st Sem: SKS Diambil", 0, 30, 0)
with col9:
    Curricular_units_1st_sem_evaluations = st.number_input("1st Sem: Evaluasi", 0, 30, 0)
    Curricular_units_1st_sem_approved = st.number_input("1st Sem: Lulus", 0, 30, 0)
with col10:
    Curricular_units_1st_sem_grade = st.number_input("1st Sem: Nilai", 0.0, 20.0, 0.0)
    Curricular_units_1st_sem_without_evaluations = st.number_input("1st Sem: Tanpa Evaluasi", 0, 30, 0)

st.markdown("---")

# Semester 2
st.markdown("### 📚 Hasil Pembelajaran Semester 2")
col11, col12, col13 = st.columns(3)
with col11:
    Curricular_units_2nd_sem_credited = st.number_input("2nd Sem: SKS Diakui", 0, 30, 0)
    Curricular_units_2nd_sem_enrolled = st.number_input("2nd Sem: SKS Diambil", 0, 30, 0)
with col12:
    Curricular_units_2nd_sem_evaluations = st.number_input("2nd Sem: Evaluasi", 0, 30, 0)
    Curricular_units_2nd_sem_approved = st.number_input("2nd Sem: Lulus", 0, 30, 0)
with col13:
    Curricular_units_2nd_sem_grade = st.number_input("2nd Sem: Nilai", 0.0, 20.0, 0.0)
    Curricular_units_2nd_sem_without_evaluations = st.number_input("2nd Sem: Tanpa Evaluasi", 0, 30, 0)

st.markdown("---")

# Keadaan Sosial
st.markdown("### 🏘️ Kondisi Sosial")
col14, col15 = st.columns(2)
with col14:
    # Displaced
    displaced_option = st.selectbox("Apakah Mahasiswa Termasuk Displaced?", ["Tidak", "Ya"])
    Displaced = 1 if displaced_option == "Ya" else 0

    # Special Needs
    special_needs_option = st.selectbox("Apakah Mahasiswa Memiliki Kebutuhan Khusus?", ["Tidak", "Ya"])
    Educational_special_needs = 1 if special_needs_option == "Ya" else 0

with col15:
    # Bayar kuliah
    tuition_option = st.selectbox("Apakah Mahasiswa Membayar Biaya Kuliah Tepat Waktu?", ["Tidak", "Ya"])
    Tuition_fees_up_to_date = 1 if tuition_option == "Ya" else 0

    # Hutang
    debtor_option = st.selectbox("Apakah Mahasiswa Memiliki Hutang Pendidikan?", ["Tidak", "Ya"])
    Debtor = 1 if debtor_option == "Ya" else 0
    
st.markdown("---")

st.markdown("### 💰 Kondisi Ekonomi")
[col16] = st.columns(1)

with col16:
    Unemployment_rate = st.number_input("Tingkat Pengangguran (%)", min_value=-10.0, max_value=30.0, value=5.0, step=0.1, format="%.2f")
    Inflation_rate = st.number_input("Inflasi (%)", min_value=-10.0, max_value=30.0, value=5.0, step=0.1, format="%.2f")
    GDP = st.number_input("GDP (%)", min_value=-10.0, max_value=30.0, value=5.0, step=0.1, format="%.2f")

st.markdown("---")

# === Prediksi ===
if st.button("🔍 Prediksi Status Mahasiswa"):
    # Simpan semua input ke DataFrame
    input_data = pd.DataFrame([[
        Marital_status, Application_mode, Application_order, Course,
        Daytime_evening_attendance, Previous_qualification, Previous_qualification_grade,
        Nacionality, Mothers_qualification, Fathers_qualification,
        Mothers_occupation, Fathers_occupation, Admission_grade, Displaced,
        Educational_special_needs, Debtor, Tuition_fees_up_to_date, Gender,
        Scholarship_holder, Age_at_enrollment, International,
        Curricular_units_1st_sem_credited, Curricular_units_1st_sem_enrolled,
        Curricular_units_1st_sem_evaluations, Curricular_units_1st_sem_approved,
        Curricular_units_1st_sem_grade, Curricular_units_1st_sem_without_evaluations,
        Curricular_units_2nd_sem_credited, Curricular_units_2nd_sem_enrolled,
        Curricular_units_2nd_sem_evaluations, Curricular_units_2nd_sem_approved,
        Curricular_units_2nd_sem_grade, Curricular_units_2nd_sem_without_evaluations,
        Unemployment_rate, Inflation_rate, GDP
    ]])

    pred = model.predict(input_data)[0]
    status_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    st.success(f"🚀 Prediksi Status Mahasiswa: **{status_map[pred]}**")
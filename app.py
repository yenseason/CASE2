import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# 1. KONFIGURASI HALAMAN & STYLING KLASIK
# ---------------------------------------------------------
st.set_page_config(
    page_title="Dashboard Profil Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS Sederhana & Rapi
st.markdown("""
    <style>
    /* Styling Kartu KPI Klasik */
    .kpi-box {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 6px;
        padding: 16px;
        text-align: left;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .kpi-title {
        color: #6B7280;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    .kpi-value {
        color: #111827;
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    /* Layout Container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. LOAD DATA
# ---------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv('dataset_mahasiswa.csv')
    
    # Pengelompokan Kategori IPK (Ordinal)
    bins = [0, 3.00, 3.50, 4.00]
    labels = ['Perlu Evaluasi (< 3.00)', 'Memuaskan (3.00 - 3.50)', 'Sangat Memuaskan / Cumlaude (> 3.50)']
    df['Kategori_IPK'] = pd.cut(df['IPK'], bins=bins, labels=labels)
    return df

df = load_data()

# ---------------------------------------------------------
# 3. HEADER
# ---------------------------------------------------------
st.title("🎓 Laporan Analisis Profil Mahasiswa")
st.caption("Bedah Kasus 2: Visualisasi & Eksplorasi Data Akademik Mahasiswa")
st.divider()

# ---------------------------------------------------------
# 4. SIDEBAR FILTER
# ---------------------------------------------------------
st.sidebar.header("Filter Data")

jurusan_filter = st.sidebar.multiselect(
    "Pilih Jurusan:",
    options=df['Jurusan'].unique(),
    default=df['Jurusan'].unique()
)

semester_range = st.sidebar.slider(
    "Rentang Semester:",
    min_value=int(df['Semester'].min()),
    max_value=int(df['Semester'].max()),
    value=(int(df['Semester'].min()), int(df['Semester'].max()))
)

kategori_ipk_filter = st.sidebar.multiselect(
    "Kategori Prestasi IPK:",
    options=df['Kategori_IPK'].cat.categories,
    default=list(df['Kategori_IPK'].cat.categories)
)

# Terapkan Filter
df_filtered = df[
    (df['Jurusan'].isin(jurusan_filter)) &
    (df['Semester'] >= semester_range[0]) &
    (df['Semester'] <= semester_range[1]) &
    (df['Kategori_IPK'].isin(kategori_ipk_filter))
]

# ---------------------------------------------------------
# 5. METRIK KPI KLASIK
# ---------------------------------------------------------
tot_mhs = len(df_filtered)
avg_ipk = df_filtered['IPK'].mean() if not df_filtered.empty else 0
max_ipk = df_filtered['IPK'].max() if not df_filtered.empty else 0
avg_usia = df_filtered['Usia'].mean() if not df_filtered.empty else 0
tot_cumlaude = len(df_filtered[df_filtered['IPK'] > 3.5]) if not df_filtered.empty else 0

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Total Mahasiswa</div>
            <div class="kpi-value">{tot_mhs:,}</div>
        </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Rata-Rata IPK</div>
            <div class="kpi-value">{avg_ipk:.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">IPK Tertinggi</div>
            <div class="kpi-value">{max_ipk:.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Rata-Rata Usia</div>
            <div class="kpi-value">{avg_usia:.1f} thn</div>
        </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Mhs Cumlaude (>3.5)</div>
            <div class="kpi-value">{tot_cumlaude:,}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------------------------------------------------
# 6. VISUALISASI CHART
# ---------------------------------------------------------
COLOR_THEME = ['#1E3A8A', '#475569', '#0284C7', '#94A3B8', '#334155']

c1, c2 = st.columns(2)

with c1:
    st.subheader("📊 Distribusi Mahasiswa per Semester (Ordinal)")
    df_sem = df_filtered.groupby('Semester').size().reset_index(name='Jumlah')
    fig_sem = px.bar(
        df_sem, x='Semester', y='Jumlah',
        text_auto=True, color_discrete_sequence=['#1E3A8A']
    )
    fig_sem.update_layout(
        plot_bgcolor='#F8FAFC',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="Semester", yaxis_title="Jumlah Mahasiswa"
    )
    st.plotly_chart(fig_sem, use_container_width=True)

with c2:
    st.subheader("🏫 Jumlah Mahasiswa per Jurusan (Nominal)")
    df_jur = df_filtered.groupby('Jurusan').size().reset_index(name='Jumlah')
    fig_jur = px.bar(
        df_jur, x='Jumlah', y='Jurusan', orientation='h',
        text_auto=True, color_discrete_sequence=['#475569']
    )
    fig_jur.update_layout(
        plot_bgcolor='#F8FAFC',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="Jumlah Mahasiswa", yaxis_title=""
    )
    st.plotly_chart(fig_jur, use_container_width=True)

c3, c4 = st.columns(2)

with c3:
    st.subheader("🧱 Proporsi Prestasi IPK (Kategori Ordinal)")
    df_kat_ipk = df_filtered.groupby('Kategori_IPK', observed=False).size().reset_index(name='Jumlah')
    fig_ipk_kat = px.pie(
        df_kat_ipk, values='Jumlah', names='Kategori_IPK',
        hole=0.4, color_discrete_sequence=COLOR_THEME
    )
    fig_ipk_kat.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_ipk_kat, use_container_width=True)

with c4:
    st.subheader("📈 Hubungan Semester vs IPK (Scatter Plot)")
    fig_scatter = px.scatter(
        df_filtered, x='Semester', y='IPK', color='Jurusan',
        hover_data=['Usia'], opacity=0.75,
        color_discrete_sequence=COLOR_THEME
    )
    fig_scatter.update_layout(
        plot_bgcolor='#F8FAFC',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="Semester", yaxis_title="IPK"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

c5, c6 = st.columns(2)

with c5:
    st.subheader("🧱 Distribusi IPK Mahasiswa (Numerik Kontinu)")
    fig_hist = px.histogram(
        df_filtered, x='IPK', nbins=20,
        color='Jurusan', marginal="box",
        color_discrete_sequence=COLOR_THEME
    )
    fig_hist.update_layout(
        plot_bgcolor='#F8FAFC',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="IPK", yaxis_title="Jumlah"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

with c6:
    st.subheader("📦 Sebaran & Outlier Usia per Jurusan")
    fig_box = px.box(
        df_filtered, x='Jurusan', y='Usia',
        color='Jurusan', points="all",
        color_discrete_sequence=COLOR_THEME
    )
    fig_box.update_layout(
        plot_bgcolor='#F8FAFC',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="Jurusan", yaxis_title="Usia (Tahun)"
    )
    st.plotly_chart(fig_box, use_container_width=True)

# ---------------------------------------------------------
# 7. TABEL LAPORAN RINGKASAN
# ---------------------------------------------------------
st.divider()
st.subheader("📋 Ringkasan Performa Akademik per Jurusan")

summary_df = df_filtered.groupby('Jurusan').agg(
    Jumlah_Mahasiswa=('IPK', 'count'),
    Rata_Rata_IPK=('IPK', 'mean'),
    IPK_Min=('IPK', 'min'),
    IPK_Max=('IPK', 'max'),
    Rata_Rata_Usia=('Usia', 'mean')
).reset_index()

st.dataframe(
    summary_df.style.format({
        'Rata_Rata_IPK': '{:.2f}',
        'IPK_Min': '{:.2f}',
        'IPK_Max': '{:.2f}',
        'Rata_Rata_Usia': '{:.1f}'
    }),
    use_container_width=True
)

with st.expander("📄 Lihat Data Mentah (1.000 Baris)"):
    st.dataframe(df_filtered)

# ---------------------------------------------------------
# 8. FOOTER
# ---------------------------------------------------------
st.divider()
st.markdown(
    "<p style='text-align: center; color: #9CA3AF; font-size: 0.85rem;'>"
    "© 241051020 - <b>ANDRIQO MARIO IMANUEL MANOPO</b> | All Rights Reserved"
    "</p>",
    unsafe_allow_html=True
)
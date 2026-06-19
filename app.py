import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Workforce Intelligence Platform",
    page_icon="🚀",
    layout="wide"
)

# CSS
st.markdown("""
<style>

/* Ana Arka Plan */
.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #0f172a
    );
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#111827;
}

/* Sidebar Yazıları */
section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Başlık */
h1{
    color:white !important;
    font-size:48px !important;
    font-weight:800 !important;
}

/* Alt Başlık */
h2,h3,h4,h5,h6{
    color:white !important;
}

/* Yazılar */
p,label,span{
    color:#e2e8f0 !important;
}

/* Metric Kartları */
[data-testid="stMetric"]{
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(12px);
    border-radius:20px;
    padding:20px;
    border:1px solid rgba(255,255,255,0.1);
}

/* Tablolar */
[data-testid="stDataFrame"]{
    border-radius:20px;
    overflow:hidden;
}

/* Scrollbar */
::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#6366f1;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Employees",
        "Analytics",
        "AI Insights"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 👨‍💻 Developer

**Ebubekir Basal**

Management Information Systems Student

🔗 GitHub:
github.com/29basal

🔗 LinkedIn:
linkedin.com/in/ebubekirbasal
""")

# Demo Data
employees = [
    ["Ahmet", "Software", 50000, 98],
    ["Ayşe", "HR", 35000, 95],
    ["Mehmet", "Finance", 60000, 92],
    ["Fatma", "Sales", 45000, 88],
    ["Ali", "Software", 70000, 97],
    ["Zeynep", "HR", 42000, 85],
    ["Can", "Finance", 65000, 90],
]

df = pd.DataFrame(
    employees,
    columns=[
    "Name",
    "Department",
    "Salary",
    "Performance"
    ]
)
if "employees_df" not in st.session_state:
    st.session_state.employees_df = df.copy()

# DASHBOARD
if menu == "Dashboard":
    employee_count = len(st.session_state.employees_df)

    total_payroll = int(
        st.session_state.employees_df["Salary"].sum()
    )

    department_count = (
        st.session_state.employees_df["Department"]
        .nunique()
    )

    avg_performance = int(
        st.session_state.employees_df["Performance"]
        .mean()
    )

    st.title("🚀 AI Workforce Intelligence Platform")

    st.markdown("""
    ### Enterprise Workforce Analytics Suite

    Real-time employee analytics, payroll monitoring,
    performance tracking and AI-powered insights.
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#2563eb,#1d4ed8);
        padding:25px;
        border-radius:20px;
        text-align:center;
        color:white;
        ">
        <h4>👥 Employees</h4>
        <h1>{employee_count}</h1>       
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#7c3aed,#5b21b6);
        padding:25px;
        border-radius:20px;
        text-align:center;
        color:white;
        ">
        <h4>💰 Payroll</h4>
        <h1>₺{total_payroll:,}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#059669,#047857);
        padding:25px;
        border-radius:20px;
        text-align:center;
        color:white;
        ">
        <h4>📈 Productivity</h4>
        <h1>{avg_performance}%</h1>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#ea580c,#c2410c);
        padding:25px;
        border-radius:20px;
        text-align:center;
        color:white;
        ">
        <h4>🏢 Departments</h4>
        <h1>{department_count}</h1>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("📊 Employees by Department")

        fig = px.bar(
        st.session_state.employees_df,
            x="Department",
            color="Department"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("🥧 Salary Distribution")

        fig2 = px.pie(
            st.session_state.employees_df,
            names="Department",
            values="Salary"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.divider()

    st.subheader("🏆 Top Performers")

    c1, c2, c3 = st.columns(3)

    c1.success("🥇 Ahmet Yılmaz - 98")
    c2.info("🥈 Ayşe Kaya - 95")
    c3.warning("🥉 Mehmet Demir - 93")

# EMPLOYEES
elif menu == "Employees":

    st.title("👥 Employee Management")

    st.dataframe(
        st.session_state.employees_df,
        use_container_width=True
    )

    st.subheader("➕ Add New Employee")

    with st.form("employee_form"):

        name = st.text_input("👤 Employee Name")

        department = st.selectbox(
            "🏢 Department",
            ["Software", "HR", "Finance", "Sales", "Marketing"]
        )

        salary = st.number_input(
            "💰 Salary",
            min_value=0,
            step=1000
        )

        performance = st.slider(
            "📈 Performance Score",
            0,
            100,
            80
        )

        submit = st.form_submit_button(
            "🚀 Add Employee"
        )

        if submit:

            new_employee = pd.DataFrame(
                [[name, department, salary, performance]],
                columns=[
                    "Name",
                    "Department",
                    "Salary",
                    "Performance"
                ]
            )

            st.session_state.employees_df = pd.concat(
                [st.session_state.employees_df, new_employee],
                ignore_index=True
            )

            st.success(f"{name} added successfully!")

            st.rerun()

    st.subheader("🗑️ Delete Employee")

    employee_names = st.session_state.employees_df["Name"].tolist()

    selected_employee = st.selectbox(
        "Select Employee",
        employee_names
    )

    if st.button("Delete Employee"):

        st.session_state.employees_df = (
            st.session_state.employees_df[
                st.session_state.employees_df["Name"]
                != selected_employee
            ]
        )

        st.success(
            f"{selected_employee} deleted successfully!"
        )

        st.rerun()

 
 

# ANALYTICS
elif menu == "Analytics":

    st.title("📈 Analytics Center")

    fig = px.histogram(
        st.session_state.employees_df,
        x="Salary",
        color="Department"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("📋 Department Statistics")

    st.dataframe(
        st.session_state.employees_df.groupby("Department")
        .agg(
            Employees=("Name","count"),
            AverageSalary=("Salary","mean")
        ),
        use_container_width=True
    )

# AI INSIGHTS
elif menu == "AI Insights":

    st.title("🤖 AI Insights Engine")

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#22c55e,#16a34a);
    padding:22px;
    border-radius:20px;
    margin-bottom:15px;
    color:white;
    font-size:20px;
    font-weight:700;
    box-shadow:0 10px 30px rgba(34,197,94,.3);
    ">
    🟢 Software Department Performance Increased by 12%
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#f59e0b,#d97706);
    padding:22px;
    border-radius:20px;
    margin-bottom:15px;
    color:white;
    font-size:20px;
    font-weight:700;
    box-shadow:0 10px 30px rgba(245,158,11,.3);
    ">
    🟡 HR Department Staffing Below Target
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#ef4444,#dc2626);
    padding:22px;
    border-radius:20px;
    margin-bottom:15px;
    color:white;
    font-size:20px;
    font-weight:700;
    box-shadow:0 10px 30px rgba(239,68,68,.3);
    ">
    🔴 Payroll Costs Increased by 8%
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<br><br>

<div style="
background:linear-gradient(135deg,#4f46e5,#7c3aed);
padding:30px;
border-radius:25px;
text-align:center;
color:white;
box-shadow:0 10px 40px rgba(124,58,237,.4);
">

<h2>🚀 Developed by Ebubekir Basal</h2>

<h4>Management Information Systems Student</h4>

<p>
Python • Streamlit • Data Analytics • AI • Web Development
</p>

</div>
""", unsafe_allow_html=True)
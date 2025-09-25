import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import seaborn as sns



st.set_page_config(
    page_title="Richie Mighty's Cafe Rewards Project",   
    page_icon="☕",                       # Can be emoji, path to .png/.ico file
    layout="wide",                        
    initial_sidebar_state="expanded"      
)


st.markdown("""
    <style>
    /* Hide radio button circles */
    div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }

    /* Style the labels like a nav */
    div[role="radiogroup"] label {
        padding: 8px 16px;
        margin-top: 10px;
        # background-color: #f0f2f6;
        border-radius: 8px;
        cursor: pointer;
        font-weight: 500;
        color: #31333F;
    }

    /* Highlight selected nav */
    div[role="radiogroup"] label:hover {
        background-color: #C0C0C0;
        color: #000;
    }

    div[role="radiogroup"] label[data-baseweb="radio"] div[aria-checked="true"] + div {
        background-color: #4CAF50 !important;
        color: white !important;
        border-radius: 8px;
        padding: 8px 16px;
    }
    </style>
""", unsafe_allow_html=True)


customers = pd.read_csv("customers.csv")
events = pd.read_csv("events.csv")
offers = pd.read_csv("offers.csv")
final_df = pd.read_csv("Final Data.csv")

# st.header("Level 5 - Machine Learning Project ")



st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go to:",
        ["Home", "About the Dataset", "Offer Analysis", "Customer Demographics", "Patterns in Offer Completion"],
        label_visibility="collapsed"  # hides the "Go to:" text
)





# Sections
if section == "Home":

    col1, col2, col3 = st.columns([2,1, 2])
    # with col1:
    #     st.write("# SQI COLLEGE OF ICT")
    with col2:
        st.image("sqi-logo-removebg-preview.png", width=350)



    # Title
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <h1 style="color:#4B0082;">☕ Cafe Rewards Project</h1>
            <h3 style="color:gray;">Data Science Level 5 - Data Visualization Project</h3>
            <h4 style="color:#2F4F4F;">SQI College of ICT</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Author Info
    st.markdown(
        """
        <div style="text-align: center; margin-top: 30px; font-size:18px;">
            <p><b>By:</b> Kehinde Richard Oluwaseun</p>
            <p><b>Email:</b> richiemighty5@gmail.com</p>
        </div>
        """,
        unsafe_allow_html=True
            # <p><b>LinkedIn:</b> <a href="https://www.linkedin.com/in/richard-kehinde-719605227" target="_blank">www.linkedin.com/in/richard-kehinde-719605227</a></p>
    )

    # Project description
    st.markdown(
        """
        <div style="margin-top: 40px; font-size:16px; line-height:1.6;">
            <h3>Project Overview</h3>
            <p>
            This project analyzes customer behavior in response to different types of cafe rewards and offers.  
            The dataset simulates the behavior of cafe reward members over a 30-day period, including transactions and promotional responses.
            </p>
            <h3>Objectives</h3>
            <ul>
                <li>Investigate how many reward offers were completed and their completion rate.</li>
                <li>Analyze which informational offers were followed by transactions.</li>
                <li>Study customer demographics distribution.</li>
                <li>Explore demographic patterns in offer completion.</li>
            </ul>
            <h3>Libraries Used</h3>
            <ul>
                <li>Pandas</li>
                <li>Matplotlib</li>
                <li>Seaborn</li>
                <li>Streamlit</li>
            </ul>
            <h3>Tools Used</h3>
            <ul>
                <li>Python</li>
                <li>Jupyter Notebook</li>
                <li>Visual Studio Code</li>
                <li>Streamlit Cloud</li>
                <li>GitHub</li>
            </ul>
            <h3>Skills Earned</h3>
            <ul>
                <li>Data Cleaning & Preprocessing</li>
                <li>Data Visualization</li>
                <li>Exploratory Data Analysis (EDA)</li>
                <li>Streamlit Dashboard Development, Deployment & Reporting</li>
            </ul>
        """,
        unsafe_allow_html=True
    )

        # Footer
    st.markdown(
        """
        <hr>
        <div style="text-align:center; font-size:14px; color:gray; margin-bottom:0; padding:0">
            © 2025 | Cafe Rewards Project | SQI College of ICT
        </div>
        """,
        unsafe_allow_html=True
    )




elif section == "About the Dataset":
    st.title("About the Dataset")

    st.write("### Data Dictionary")


    st.markdown(
        """
        | Table     | Field             | Description                                                                 |
        |-----------|------------------|-----------------------------------------------------------------------------|
        | offers    |                  | Details on the offers sent to customers during the 30-day period            |
        | offers    | offer_id         | Unique offer ID (primary key)                                               |
        | offers    | offer_type       | Type of offer: bogo (buy one, get one), discount, or informational          |
        | offers    | difficulty       | Minimum amount required to spend in order to complete the offer             |
        | offers    | reward           | Reward (in dollars) obtained by completing the offer                        |
        | offers    | duration         | Days a customer has to complete the offer once received                     |
        | offers    | channels         | List of marketing channels used to send the offer                           |
        | customers |                  | Demographic data for each member                                            |
        | customers | customer_id      | Unique customer ID (primary key)                                            |
        | customers | became_member_on | Date when the customer created their account (yyyymmdd)                     |
        | customers | gender           | Customer's gender: (M)ale, (F)emale, or (O)ther                             |
        | customers | age              | Customer's age                                                              |
        | customers | income           | Customer's estimated annual income (USD)                                    |
        | events    |                  | Data on customer activity: transactions, offers received/viewed/completed   |
        | events    | customer_id      | Customer the event is associated with (foreign key)                         |
        | events    | event            | Description of the event (transaction, offer received, offer viewed, etc.)  |
        | events    | value            | Dictionary of values (amount for txn, offer_id & reward for offers, etc.)   |
        | events    | time             | Hours passed in the 30-day period (starting at 0)                           |
        """
    )


    st.write("#### Preview of all 3 given Datasets")
    with st.expander("Preview the head of Events Dataset"):
        st.dataframe(events.head())

    with st.expander("Preview the head of Offer Dataset"):
        st.dataframe(offers.head())

    with st.expander("Preview the head of Customers Dataset"):
        st.dataframe(customers.head())

    st.write("### Final Preprocessed Dataset")
    with st.expander("Preview the head of the Cleaned Merged Data"):
        st.dataframe(final_df.head())

    st.write("### Final Data Information")
    # st.write(final_df.info())
    buf = io.StringIO()
    final_df.info(buf=buf)         
    s = buf.getvalue()            
    st.code(s)                    

    st.write("### Checking Missing Data")
    with st.expander("Check frequency and proportion of Missing values"):
        missing_vals = final_df.isnull().sum()
        missing_prop = final_df.isnull().sum()/len(final_df)*100
        st.dataframe(pd.DataFrame({"Freq":missing_vals, "Prop": missing_prop}) )


    st.write(
        """
            | Column                    | % Missing | Notes                                                                  |
            | ------------------------- | --------- | ---------------------------------------------------------------------- |
            | `customer_id`             | 0%        | Perfect.                                                  |
            | `event`                   | 0%        | Clean.                                                                 |
            | `time`                    | 0%        | Clean.                                                                 |
            | `offer_id`                | **45%**   | Missing because not every event has an offer (transactions don’t).     |
            | `amount`                  | **55%**   | Missing because only transactions have an amount.                      |
            | `became_member_on`        | 0%        | Clean.                                                                 |
            | `gender`                  | **11%**   | Some customers didn’t provide gender.                                  |
            | `age`                     | 0%        | Looks clean, but where age = 118, sometimes i can be a placeholder. |
            | `income`                  | **11%**   | Same customers missing gender likely also missing income.              |
            | `offer_type`              | **45%**   | Same as `offer_id` – missing for transaction events.                   |
            | `difficulty`              | **45%**   | Same reason.                                                           |
            | `reward_y`                | **45%**   | Same reason.                                                           |
            | `duration`                | **45%**   | Same reason.                                                           |
            | `channels`                | 0%        | Clean.                                                                 |
            | `web/email/mobile/social` | 0%        | Clean (after one-hot expansion).                                       |
        """
    )




elif section == "Offer Analysis":
    st.header("Offer Completion Analysis")
    # 👉 Place your expander with offer stats + chart here
    st.write("### Question 1: How many reward offers were completed? Which offers had the highest completion rate?")

    # Total offers received
    offers_received = final_df[final_df["event"] == "offer received"].groupby("offer_id")["customer_id"].count()

    # Offers completed
    offers_completed = final_df[final_df["event"] == "offer completed"].groupby("offer_id")["customer_id"].count()

    # Merge into one table
    offer_stats = pd.concat([offers_received, offers_completed], axis=1, keys=["received", "completed"]).fillna(0)

    # Add completion rate
    offer_stats["completion_rate"] = offer_stats["completed"] / offer_stats["received"]

    offer_stats = offer_stats.merge(offers, on="offer_id", how="left")


    with st.expander("Offer Completion Analysis", expanded=False):
        st.write("### Offer Completion Stats Table")
        st.dataframe(offer_stats.sort_values("completion_rate", ascending=False))



    # Show the bar chart
    st.write("## Offer Completion Rate by Offer ID")
    fig, ax = plt.subplots()

    offer_stats.sort_values("completion_rate", ascending=True).plot(
        x="offer_id", y="completion_rate", kind="barh", legend=False, ax=ax
    )
    ax.set_title("Offer Completion Rate by ID")
    ax.set_ylabel("Completion Rate")
    st.pyplot(fig)


    # Reward offers completed
    reward_completed = final_df[final_df["event"] == "offer completed"].groupby("offer_type").size()

    # Offers received (baseline for completion rate)
    reward_received = final_df[final_df["event"] == "offer received"].groupby("offer_type").size()

    # Combine into DataFrame
    offer_stats = pd.DataFrame({
        "received": reward_received,
        "completed": reward_completed
    }).fillna(0)

    # Add completion rate
    offer_stats["completion_rate"] = offer_stats["completed"] / offer_stats["received"]


    st.write("## Offer Completion Rate by Offer Type")

    st.write(offer_stats.sort_values("completion_rate", ascending=False))

    # Show in Streamlit
    # with st.expander("Reward Offers Completion Stats"):
    fig, ax = plt.subplots()
    offer_stats.sort_values("completion_rate", ascending=False).plot(
        y="completion_rate", kind="bar", ax=ax, legend=False
    )
    ax.set_title("Offer Completion Rate by Offer Type")
    ax.set_ylabel("Completion Rate")
    st.pyplot(fig)




    st.write("## 2. How many informational offers were followed by transactions?")
  
    # Filter informational offers
    info_offers = final_df[final_df["offer_type"] == "informational"]
    with st.expander("View the Filtered Informational offers Rows"):
        st.dataframe(info_offers.head(50))

    # Merge with transactions by customer
    transactions = final_df[final_df["event"] == "transaction"]
    with st.expander("View the Filtered transactions data from the filtered Informational offers Rows"):
        st.dataframe(transactions.head(50))


    # counting customers who got informational offer 
    info_with_txn = info_offers.merge(transactions, on="customer_id", suffixes=("_offer", "_txn"))

    info_with_txn = info_with_txn[info_with_txn["time_txn"] > info_with_txn["time_offer"]]      # AND later transacted: 

    # Total informational offers
    total_info_offers = info_offers["customer_id"].nunique()

    st.write("### Informational Offers Followed by Transactions")
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.write("Total No. of Customer who received informational offer")
        st.write(total_info_offers)
    with col2:
        st.write("Total No. of ALL informational offers received and viewed")
        st.write(len(info_offers))

    with col3:
        st.write(f"Number of informational offers followed by transactions")
        st.write(info_with_txn.shape[0])


    col1, col2 = st.columns([1,1])

    with col1:
        # Customers who transacted after receiving an informational offer
        followed_txn = info_with_txn["customer_id"].nunique()

        # Customers who didn’t transact after receiving informational offers
        not_followed = total_info_offers - followed_txn

        # Plot pie chart
        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
            [followed_txn, not_followed],
            labels=["Followed by Transaction", "Not Followed"],
            autopct=lambda pct: f"{pct:.1f}%\n({int(round(pct/100*total_info_offers))})",  # % and count
            startangle=90
        )

        # Style labels
        for text in texts:
            text.set_fontsize(10)
        for autotext in autotexts:
            autotext.set_fontsize(9)
            autotext.set_color("white")

        ax.set_title("Informational Offers Followed by Transactions")
        st.pyplot(fig)

    with col2:


        info_off_typ = info_offers['event'].value_counts()


        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
            info_off_typ,
            labels=["offer received ", "offer Viewed"],
            autopct=lambda pct: f"{pct:.1f}%\n({int(round(pct/100*sum(info_off_typ)))})",  # % and count
            startangle=90
        )

        # Style labels
        for text in texts:
            text.set_fontsize(10)
        for autotext in autotexts:
            autotext.set_fontsize(9)
            autotext.set_color("white")

        ax.set_title("Informational Offers Followed by Transactions")
        plt.title("Distribution of Information Offers")
        st.pyplot(fig)



    with st.expander("Preview the Informational Offer Time by Transaction time Data"):
        info_by_txn = pd.DataFrame({ "Offer ID": info_with_txn["offer_id_offer"], "Customer ID": info_with_txn["customer_id"], "Recieved Time":info_with_txn["time_offer"], "transactions Time": info_with_txn["time_txn"]})
        st.dataframe(info_by_txn)
    
    # Make sure time columns are numeric or datetime
    # info_by_txn["Recieved Time"] = pd.to_numeric(info_by_txn["Recieved Time"])
    # info_by_txn["transactions Time"] = pd.to_numeric(info_by_txn["transactions Time"])

    # fig, ax = plt.subplots(figsize=(10, 6))

    # # Plot each customer's timeline
    # for i, row in info_by_txn.iterrows():
    #     ax.plot(
    #         [row["Recieved Time"], row["transactions Time"]],  # x-values
    #         [row["Customer ID"], row["Customer ID"]],          # y-values (same for a line)
    #         marker="o"
    #     )

    # ax.set_title("Offer Received vs Transaction Time per Customer")
    # ax.set_xlabel("Time")
    # ax.set_ylabel("Customer ID")
    # plt.tight_layout()
    # st.pyplot(fig)


    st.write("### Visualization: Transactions after Informational Offers")
    # Count how many times each customer transacted after an informational offer
    txn_counts = info_with_txn.groupby("customer_id")["time_txn"].count()
    fig, ax = plt.subplots()
    txn_counts.plot(kind="hist", bins=20, ax=ax)
    ax.set_title("Distribution of Transactions after Informational Offers")
    ax.set_xlabel("Number of Transactions")
    ax.set_ylabel("Number of Customers")
    st.pyplot(fig)







elif section == "Customer Demographics":
    st.header("Customer Demographics Distribution")
    # st.write("## 3. Customer Demographics Distribution")

    gender_counts = final_df["gender"].value_counts()

    # --- Combined Overview ---
    # if st.checkbox("Combined Overview"):
    st.write("Here’s a quick snapshot of all demographics together.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average Age", round(final_df["age"].mean(), 1))
    with col2:
        st.metric("Average Income", f"${round(final_df['income'].mean(), 2)}")
    with col3:
        st.metric("Gender Split", f"{gender_counts.idxmax()} leads")



    with st.expander("Show Summary Statistics"):
        st.write("### Summary Statistics")
        st.dataframe(final_df.describe())

    # --- Age Distribution ---
    with st.expander("👤 Age Distribution"):
        st.write("Here we explore customer age using multiple quantitative plots.")

        col1, col2 = st.columns(2)

        # Histogram
        with col1:
            fig, ax = plt.subplots(figsize=(6,4))
            ax.hist(final_df["age"], bins=20, color="skyblue", edgecolor="black")
            ax.set_title("Histogram of Age")
            ax.set_xlabel("Age")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)

        # Boxplot
        with col2:
            # Filter invalid ages (e.g., 118 as placeholder for missing)
            valid_age = final_df[final_df["age"] < 100]["age"]

            fig, ax = plt.subplots(figsize=(6,4))
            ax.boxplot([valid_age], vert=False, patch_artist=True, 
                    boxprops=dict(facecolor="lightgreen", color="black"),
                    medianprops=dict(color="red", linewidth=2))
            ax.set_title("Boxplot of Age")
            ax.set_xlabel("Age")
            st.pyplot(fig)

        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            # KDE Plot (Density Curve)
            fig, ax = plt.subplots(figsize=(6,4))
            sns.kdeplot(final_df["age"], shade=True, color="purple", ax=ax)
            ax.set_title("KDE Plot (Density) of Age")
            ax.set_xlabel("Age")
            st.pyplot(fig)


        

    # --- Gender Distribution ---
    with st.expander("🚻 Gender Distribution"):

        col1, col2 = st.columns([1,1])

        with col1:
            fig, ax = plt.subplots()
            ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
            ax.set_title("Gender Distribution of Customers")
            st.pyplot(fig)


        # --- Income Distribution ---
    if st.button("💰 Show Income Distribution"):
        st.write("This plot shows how customer income is distributed.")
        
        col1, col2 = st.columns(2)

        # Histogram
        with col1:
            fig, ax = plt.subplots(figsize=(8,5))
            ax.hist(final_df["income"], bins=20, color="green", edgecolor="black")
            ax.set_title("Income Distribution of Customers")
            ax.set_xlabel("Income ($)")
            ax.set_ylabel("Number of Customers")
            st.pyplot(fig)

        # Boxplot
        with col2:
            fig, ax = plt.subplots(figsize=(6,4))
            ax.boxplot([final_df["income"]], vert=False, patch_artist=True, 
                    boxprops=dict(facecolor="lightgreen", color="black"),
                    medianprops=dict(color="red", linewidth=2))
            ax.set_title("Boxplot of Income")
            ax.set_xlabel("Age")
            st.pyplot(fig)




    if st.button("Click here to Show the Relationship Between Income and Age"):
        st.write("Scatter plot showing the relationship between customer age and income.")
        
        fig, ax = plt.subplots(figsize=(8,5))
        ax.scatter(final_df["age"], final_df["income"], alpha=0.6, c="purple", edgecolor="k")
        ax.set_title("Age vs Income")
        ax.set_xlabel("Age")
        ax.set_ylabel("Income ($)")
        st.pyplot(fig)







elif section == "Patterns in Offer Completion":
    st.header("Demographic Patterns in Offer Completion")

    # --- Completion rate by gender ---
    gender_completion = final_df[final_df["event"].isin(["offer received", "offer completed"])]
    gender_stats = gender_completion.groupby(["gender", "event"]).size().unstack().fillna(0)
    gender_stats["completion_rate"] = gender_stats["offer completed"] / gender_stats["offer received"]

    with st.expander("Offer Completion by Gender"):
        col1, col2 = st.columns(2)

        with col1:
            st.write("### Table: Completion Rate by Gender")
            st.dataframe(gender_stats)

        with col2:
            fig, ax = plt.subplots()
            bars = gender_stats["completion_rate"].plot(kind="bar", ax=ax, color=["skyblue", "salmon", "lightgreen"])
            ax.set_title("Offer Completion Rate by Gender")
            ax.set_ylabel("Completion Rate")
            ax.set_xlabel("Gender")

            # Add data labels
            for p in ax.patches:
                ax.annotate(f"{p.get_height():.2f}", 
                            (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha="center", va="bottom", fontsize=9, color="black")
            st.pyplot(fig)


    # --- Completion rate by income group ---
    with st.expander("Completion Rate by Income Group and Age Group Tables"):
        income_bins = [0, 40000, 60000, 80000, 100000, 120000]
        final_df["income_group"] = pd.cut(final_df["income"], bins=income_bins)

        income_stats = final_df.groupby("income_group")["event"].value_counts().unstack().fillna(0)
        income_stats["completion_rate"] = income_stats["offer completed"] / income_stats["offer received"]

        age_bins = [18, 30, 40, 50, 60, 70, 100]
        final_df["age_group"] = pd.cut(final_df["age"], bins=age_bins)

        age_stats = final_df.groupby("age_group")["event"].value_counts().unstack().fillna(0)
        age_stats["completion_rate"] = age_stats["offer completed"] / age_stats["offer received"]

        # with col1:
        st.write("### Table: Completion Rate by Income Group")
        st.dataframe(income_stats)

        # with col2:

        st.write("### Table: Completion Rate by Age Group")
        st.dataframe(age_stats)



    # --- Completion rate by age group ---
    with st.expander("Completion Rate by Income Group and Age Group"):

        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots()
            bars = income_stats["completion_rate"].plot(kind="bar", ax=ax, color="orange", edgecolor="k")
            ax.set_title("Offer Completion Rate by Income Group", fontsize=10)
            ax.set_ylabel("Completion Rate", fontsize=3)
            ax.set_xlabel("Income Group")
            # ax.set_xticklabels(fontsize=3)
            plt.xticks(rotation=45, )
            # plt.yticks(fontsize=3)

            # Add data labels
            for p in ax.patches:
                ax.annotate(f"{p.get_height():.2f}", 
                            (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha="center", va="bottom", fontsize=9, color="black")
            st.pyplot(fig)

        with col2:
            fig, ax = plt.subplots()
            ax.plot(age_stats.index.astype(str), age_stats["completion_rate"], marker="o", color="green")
            ax.set_title("Offer Completion Rate by Age Group")
            ax.set_ylabel("Completion Rate")
            ax.set_xlabel("Age Group")

            # Add data labels
            for x, y in zip(age_stats.index.astype(str), age_stats["completion_rate"]):
                ax.annotate(f"{y:.2f}", (x, y), textcoords="offset points", xytext=(0, 5), ha="center")
            st.pyplot(fig)

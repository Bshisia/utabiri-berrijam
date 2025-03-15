from nicegui import ui
import pandas as pd
import plotly.express as px
def show_key_factors(df):
    """Creates visualization dashboard for heart attack mortality analysis.

    Args:
        df (pd.DataFrame): DataFrame containing patient data with columns:
            - Mortality (str): 'Yes'/'No' indicating patient outcome
            - Anion gap (float): Blood anion gap measurement
            - Rel failure (int): Renal failure indicator (0/1)
    """
    try:
        with ui.row().classes("w-full gap-4 flex flex-row"):
            with ui.card().tight().classes("flex-1 h-[400px]"):  
                ui.label("Patient Statistics").classes("text-xl font-bold p-4")
                total_patients = len(df)
                mortality_count = (df["Mortality"] == "Yes").sum()
                survival_count = total_patients - mortality_count
                survival_rate = (survival_count / total_patients) * 100 if total_patients > 0 else 0
                mortality_rate = (mortality_count / total_patients) * 100 if total_patients > 0 else 0                
                with ui.column().classes("h-full justify-center"): 
                    ui.html(
                        f"""
                        <div class="p-4">
                            <p class="text-lg"><b>Total Patients:</b> {total_patients}</p>
                            <p class="text-lg"><b>Mortality Cases:</b> {mortality_count}</p>
                            <p class="text-lg"><b>Survival Rate:</b> {survival_rate:.1f}%</p>
                            <p class="text-lg"><b>Mortality Rate:</b> {mortality_rate:.1f}%</p>
                        </div>
                        """
                    )
            
            with ui.card().tight().classes("flex-1 h-[400px]"):  
                ui.label("Survival Distribution").classes("text-xl font-bold p-4")
                pie_data = pd.DataFrame({
                    'Status': ['Survived', 'Deceased'],
                    'Count': [survival_count, mortality_count]
                })
                
                fig = px.pie(
                    pie_data,
                    values='Count',
                    names='Status',
                    color_discrete_sequence=['#0000FF', '#F44336'],
                    hole=0.3
                )
                
                fig.update_layout(
                    width=400,
                    height=300,
                    margin=dict(t=30, b=30, l=30, r=100),
                    showlegend=True,
                    legend=dict(
                        orientation="v",  
                        yanchor="middle",
                        y=0.5,  
                        xanchor="left",  
                        x=1.1,  
                        bgcolor="rgba(255, 255, 255, 0.8)",  
                        bordercolor="rgba(0, 0, 0, 0.1)",  
                        borderwidth=1,
                        font=dict(size=16),
                        itemsizing='constant',
                        itemwidth=30
                    )
                )
                
                fig.update_traces(
                    hovertemplate="<b>%{label}</b><br>" +
                                "Count: %{value}<br>" +
                                "Percentage: %{percent:.1%}<extra></extra>"
                )
                
                ui.plotly(fig).classes("w-full h-full")

        with ui.card().tight().classes("w-full mx-auto my-4"):
            ui.label("Key Risk Factors Summary").classes("text-xl font-bold p-4")
            ui.html(
                """
          <div class="p-4 bg-blue-50 rounded-lg">
            <p class="text-base">From the analysis of multiple clinical parameters, two key factors emerged as the strongest predictors 
            of mortality: Anion Gap and Rel Failure(Renal Failure). While other factors showed some correlation, these two 
            demonstrated the most significant impact on patient outcomes.</p>
          </div>
          """
            )
            ui.label("1. Anion Gap Impact").classes("text-lg font-bold p-4")

            anion_high = df["Anion gap"] > 16.91
            mortality_high_anion = (
                (df[anion_high]["Mortality"] == "Yes").mean() * 100
                if len(df[anion_high]) > 0
                else 0
            )
            mortality_low_anion = (
                (df[~anion_high]["Mortality"] == "Yes").mean() * 100
                if len(df[~anion_high]) > 0
                else 0
            )
            ui.html(
                f"""
                <div class="p-8">
                    <ul class="text-base">
                        <li>Mortality rate with high Anion gap (>16.91): {mortality_high_anion:.1f}%</li>
                        <li>Mortality rate with low Anion gap (≤16.91): {mortality_low_anion:.1f}%</li>
                    </ul>
                </div>
            """
            )
            
            df["Anion_Gap_Group"] = df["Anion gap"].apply(
                lambda x: ">16.91" if x > 16.91 else "≤16.91"
            )
            
            anion_gap_mortality = []
            for group in ["≤16.91", ">16.91"]:
                group_df = df[df["Anion_Gap_Group"] == group]
                if len(group_df) > 0:
                    mortality_rate = (group_df["Mortality"] == "Yes").sum() / len(group_df) * 100
                    anion_gap_mortality.append({"Anion_Gap_Group": group, "Mortality Rate (%)": round(mortality_rate, 1)})
                else:
                    anion_gap_mortality.append({"Anion_Gap_Group": group, "Mortality Rate (%)": 0.0})
            
            anion_gap_mortality = pd.DataFrame(anion_gap_mortality)
            
            fig_anion = px.bar(
                anion_gap_mortality,
                x="Anion_Gap_Group",
                y="Mortality Rate (%)",
                title="Mortality Rate by Anion Gap Level",
                color="Anion_Gap_Group",
                color_discrete_map={"≤16.91": "blue", ">16.91": "red"},
                text="Mortality Rate (%)"
            )
            
            fig_anion.update_layout(
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                    bgcolor="rgba(255, 255, 255, 0.8)",
                    bordercolor="rgba(0, 0, 0, 0.1)",
                    borderwidth=1,
                    font=dict(size=16),
                    itemsizing='constant',
                    itemwidth=30
                )
            )
            
            fig_anion.update_traces(
                texttemplate='%{text:.1f}%',
                textposition='inside',
                textfont=dict(color='white', size=14),
                hovertemplate="<b>%{x}</b><br>" +
                            "Mortality: %{y:.1f}%<extra></extra>"
            )
            ui.plotly(fig_anion).classes("w-full h-100")

            ui.label("2. Rel Failure Impact").classes("text-lg font-bold p-4")

            renal_failure = df["Rel failure"] > 0
            mortality_with_renal = (
                (df[renal_failure]["Mortality"] == "Yes").mean() * 100
                if len(df[renal_failure]) > 0
                else 0
            )
            mortality_without_renal = (
                (df[~renal_failure]["Mortality"] == "Yes").mean() * 100
                if len(df[~renal_failure]) > 0
                else 0
            )
            ui.html(
                f"""
                <div class="p-4">
                    <ul class="text-base">
                        <li>Mortality rate with Rel failure: {mortality_with_renal:.1f}%</li>
                        <li>Mortality rate without Rel failure: {mortality_without_renal:.1f}%</li>
                    </ul>
                </div>
            """
            )

            df["Renal_Failure_Group"] = df["Rel failure"].apply(
                lambda x: "Yes" if x > 0 else "No"
            )
            
            renal_failure_mortality = []
            for group in ["Yes", "No"]:
                group_df = df[df["Renal_Failure_Group"] == group]
                if len(group_df) > 0:
                    mortality_rate = (group_df["Mortality"] == "Yes").sum() / len(group_df) * 100
                    renal_failure_mortality.append({"Renal_Failure_Group": group, "Mortality Rate (%)": round(mortality_rate, 1)})
                else:
                    renal_failure_mortality.append({"Renal_Failure_Group": group, "Mortality Rate (%)": 0.0})
            
            renal_failure_mortality = pd.DataFrame(renal_failure_mortality)
            
            fig_renal = px.bar(
                renal_failure_mortality,
                x="Renal_Failure_Group",
                y="Mortality Rate (%)",
                title="Mortality Rate by Rel Failure",
                color="Renal_Failure_Group",
                color_discrete_map={"Yes": "red", "No": "blue"},
                text="Mortality Rate (%)"
            )
            
            fig_renal.update_layout(
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                    bgcolor="rgba(255, 255, 255, 0.8)",
                    bordercolor="rgba(0, 0, 0, 0.1)",
                    borderwidth=1,
                    font=dict(size=16),
                    itemsizing='constant',
                    itemwidth=30
                )
            )
            
            fig_renal.update_traces(
                texttemplate='%{text:.1f}%',
                textposition='inside',
                textfont=dict(color='white', size=14),
                hovertemplate="<b>%{x}</b><br>" +
                            "Mortality: %{y:.1f}%<extra></extra>"
            )
            ui.plotly(fig_renal).classes("w-full h-100")            

    except Exception as ex:
        ui.notify(f"Error generating summary: {ex}", type="negative")
        print(f"Error in summarize_dataset: {ex}")
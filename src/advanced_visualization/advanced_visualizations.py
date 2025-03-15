from nicegui import ui
import plotly.express as px
import pandas as pd


def add_advanced_visualizations(df):
    """Creates an interactive visualization dashboard for analyzing patient mortality based on Anion Gap and Renal Failure status.
    The visualization updates in real-time as users adjust the thresholds and filters.

    Args:
        df (pd.DataFrame): Input DataFrame containing patient data with the following required columns:
            - Anion gap (float): Blood anion gap measurements
            - Rel failure (int): Binary indicator for renal failure (0 or 1)
            - Mortality (str): Patient outcome ('Yes' or 'No')

    Returns:
        None: The function creates UI elements directly using the NiceGUI framework
    """
    try:
        with ui.card().tight().classes("w-full mx-auto my-4"):
            ui.label("Mortality Analysis").classes("text-xl font-bold p-4")

            anion_min = round(df["Anion gap"].min(), 1)
            anion_max = round(df["Anion gap"].max(), 1)

            with ui.column().classes("w-full gap-4"):
                with ui.row().classes("w-full items-center"):
                    ui.label("Anion Gap Threshold:").classes("text-lg")
                    anion_value_display = ui.label().classes("ml-2")

                anion_slider = ui.slider(
                    min=anion_min,
                    max=anion_max,
                    value=16.91,
                    step=0.1,
                    on_change=lambda e: (
                        anion_value_display.set_text(f"{e.value:.1f}"),
                        update_visualization(),
                    ),
                ).classes("w-full")

                with ui.row().classes("w-full items-center mt-4"):
                    ui.label("Renal Failure Status:").classes("text-lg")

                with ui.row().classes("w-full items-center gap-4"):
                    renal_status = ui.radio(
                        ["All Patients", "With Renal Failure", "Without Renal Failure"],
                        value="All Patients",
                        on_change=lambda: update_visualization(),
                    ).classes("mt-2")

            plot_container = ui.element("div").classes("w-full mt-4")
            insights = ui.html("").classes("w-full mt-4")

            def update_visualization():
                anion_threshold = anion_slider.value
                renal_selection = renal_status.value

                if renal_selection == "All Patients":
                    base_filter = df["Anion gap"] > anion_threshold
                elif renal_selection == "With Renal Failure":
                    base_filter = (df["Anion gap"] > anion_threshold) | (
                        df["Rel failure"] == 1
                    )
                else:
                    base_filter = (df["Anion gap"] > anion_threshold) & (
                        df["Rel failure"] == 0
                    )

                high_risk_patients = df[base_filter]
                mortality_counts = high_risk_patients["Mortality"].value_counts()
                total_patients = len(high_risk_patients)

                if total_patients > 0:
                    mortality_data = {
                        "Status": ["Survived", "Deceased"],
                        "Count": [
                            mortality_counts.get("No", 0),
                            mortality_counts.get("Yes", 0),
                        ],
                    }

                    fig = px.pie(
                        pd.DataFrame(mortality_data),
                        values="Count",
                        names="Status",
                        title=f"Mortality Distribution\nTotal Patients: {total_patients}",
                        color_discrete_sequence=["#0000FF", "#e74c3c"],
                    )

                    fig.update_layout(
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

                    fig.update_traces(textposition="inside", textinfo="percent+value")

                    plot_container.clear()
                    with plot_container:
                        ui.plotly(fig).classes("w-full")

                    survival_rate = mortality_counts.get("No", 0) / total_patients * 100
                    mortality_rate = (
                        mortality_counts.get("Yes", 0) / total_patients * 100
                    )

                    renal_status_text = {
                        "All Patients": "all patients",
                        "With Renal Failure": "patients with renal failure",
                        "Without Renal Failure": "patients without renal failure",
                    }[renal_selection]

                    insights_text = f"""
                    <div class="p-4 bg-blue-50 rounded-lg">
                        <p class="text-lg font-bold">Analysis Summary:</p>
                        <ul class="list-disc pl-5 mt-2">
                            <li>Total patients: {total_patients}</li>
                            <li>Survival rate: {survival_rate:.1f}%</li>
                            <li>Mortality rate: {mortality_rate:.1f}%</li>
                        </ul>
                        <p class="mt-2 text-sm text-gray-600">
                            *Analysis based on {renal_status_text} with Anion Gap > {anion_threshold:.1f}
                        </p>
                    </div>
                    """
                else:
                    plot_container.clear()
                    insights_text = """
                    <div class="p-4 bg-yellow-50 rounded-lg">
                        <p class="text-lg font-bold">No patients found matching the selected criteria</p>
                    </div>
                    """

                insights.set_content(insights_text)

            anion_value_display.set_text(f"{16.91:.1f}")
            update_visualization()

    except Exception as ex:
        ui.notify(f"Error creating visualization: {ex}", type="negative")
        print(f"Error in add_advanced_visualizations: {ex}")

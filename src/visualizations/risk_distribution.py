from nicegui import ui
import pandas as pd
import plotly.express as px


def show_risk_distribution(df):
    with ui.card().tight().classes("w-full mx-auto my-4"):
        ui.html(
            """
            <div class="p-4 bg-blue-50 rounded-lg">
                <p class="text-lg font-bold">Distribution Insights:</p>
                <ul class="list-disc pl-5 mt-2 text-base">
                    <li>The histograms show how values are distributed for both survivors and mortality cases</li>
                    <li>Blue bars represent patients who survived, while red bars show those who did not</li>
                    <li>The height of each bar indicates the number of patients with that specific value</li>
                    <li>Areas where red bars are taller suggest higher mortality risk for those values</li>
                </ul>
            </div>
        """
        )
        with ui.row().classes("w-full gap-4"):
            fig_dist1 = px.histogram(
                df,
                x="Anion gap",
                color="Mortality",
                title="Anion Gap Distribution by Mortality",
                color_discrete_map={"Yes": "red", "No": "blue"},
                opacity=0.7,
                text_auto=".2s",
                nbins=20,
                height=700,
                width=1200,
            )

            fig_dist1.update_traces(
                textposition="outside", textfont=dict(size=12), bingroup="1"
            )
            fig_dist1.update_layout(
                bargap=0.2,
                showlegend=True,
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="right",
                    x=0.99,
                    font=dict(size=16),
                    itemsizing="constant",
                    itemwidth=30,
                ),
            )

            ui.plotly(fig_dist1).classes("w-1/2")

            fig_dist2 = px.histogram(
                df,
                x="Rel failure",
                color="Mortality",
                title="Rel Failure Distribution by Mortality",
                color_discrete_map={"Yes": "red", "No": "blue"},
                opacity=0.7,
                text_auto=".2s",
                nbins=2,
                height=700,
                width=1200,
            )

            fig_dist2.update_traces(
                textposition="outside", textfont=dict(size=12), bingroup="1"
            )
            fig_dist2.update_layout(
                bargap=0.2,
                showlegend=True,
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="right",
                    x=0.99,
                    font=dict(size=16),
                    itemsizing="constant",  
                    itemwidth=30,
                ),
            )

            ui.plotly(fig_dist2).classes("w-1/2")

from nicegui import ui
import pandas as pd
import plotly.express as px

def show_combined_risk_factors(df):
    """
    Show Combined Risk Factors Impact visualization with blue to red color scheme.
    
    Args:
        df (pd.DataFrame): The input data as a pandas DataFrame.
    """
    if df.empty:
        raise ValueError("DataFrame cannot be empty")
        
    required_columns = ['Mortality', 'Anion gap', 'Rel failure']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"DataFrame missing required columns: {required_columns}")
    
    with ui.card().tight().classes("w-full mx-auto my-4"):
        ui.label("3. Combined Risk Factors Impact").classes("text-lg font-bold p-4")

        ui.html("""
            <div class="p-4">
                <p class="text-base">When analyzing how these two factors interact, we found that their combination significantly 
                amplifies the mortality risk. Patients were categorized into four groups based on their Anion Gap 
                and Rel Failure status:</p>
                <ul class="list-disc pl-5 mt-2 text-base">
                    <li>High Anion Gap + Rel Failure: Both factors present</li>
                    <li>High Anion Gap Only: Elevated Anion Gap without Rel Failure</li>
                    <li>Rel Failure Only: Normal Anion Gap with Rel Failure</li>
                    <li>No Risk Factors: Neither factor present</li>
                </ul>
            </div>
        """)

        df['Risk_Category'] = 'Other'
        df.loc[(df['Anion gap'] > 16.91) & (df['Rel failure'] > 0), 'Risk_Category'] = 'High Anion Gap + Rel Failure'
        df.loc[(df['Anion gap'] > 16.91) & (df['Rel failure'] <= 0), 'Risk_Category'] = 'High Anion Gap Only'
        df.loc[(df['Anion gap'] <= 16.91) & (df['Rel failure'] > 0), 'Risk_Category'] = 'Rel Failure Only'
        df.loc[(df['Anion gap'] <= 16.91) & (df['Rel failure'] <= 0), 'Risk_Category'] = 'No Risk Factors'

        risk_mortality = df.groupby('Risk_Category')['Mortality'].apply(
            lambda x: round((x == 'Yes').sum() / len(x) * 100, 1) 
        ).reset_index(name='Mortality Rate (%)')
        category_counts = df.groupby('Risk_Category').size().reset_index(name='Count')
        risk_mortality = risk_mortality.merge(category_counts, on='Risk_Category')

        custom_order = ['No Risk Factors', 'Rel Failure Only', 'High Anion Gap Only', 'High Anion Gap + Rel Failure']
        existing_categories = risk_mortality['Risk_Category'].unique()
        filtered_order = [cat for cat in custom_order if cat in existing_categories]

        if len(filtered_order) > 0:
            insights_html = "<div class='p-4 bg-blue-50 rounded-lg'><p class='text-lg font-bold'>Current Risk Analysis:</p><ul class='list-disc pl-5 mt-2'>"
            
            for category in filtered_order:
                category_data = risk_mortality[risk_mortality['Risk_Category'] == category]
                if len(category_data) > 0:
                    mortality_rate = category_data['Mortality Rate (%)'].values[0]
                    patient_count = category_data['Count'].values[0]
                    insights_html += f"<li class='text-base'>Patients with {category.lower()}: {mortality_rate:.1f}% mortality rate ({patient_count} patients)</li>"
            
            insights_html += "</ul></div>"
            ui.html(insights_html)
            
            risk_mortality['Risk_Category'] = pd.Categorical(
                risk_mortality['Risk_Category'],
                categories=filtered_order,
                ordered=True
            )
            risk_mortality = risk_mortality.sort_values('Risk_Category')
            
            color_map = {
                'No Risk Factors': '#2196F3',        
                'Rel Failure Only': '#9C27B0',       
                'High Anion Gap Only': '#FF5722',   
                'High Anion Gap + Rel Failure': '#F44336'  
            }
            
            fig_combined = px.bar(
                risk_mortality,
                x='Risk_Category',
                y='Mortality Rate (%)',
                title="Mortality Rate by Risk Category",
                color='Risk_Category',
                color_discrete_map=color_map,
                text='Mortality Rate (%)' 
            )
            
            fig_combined.update_layout(
                xaxis_title="Risk Category",
                yaxis_title="Mortality Rate (%)",
                xaxis={'categoryorder': 'array', 'categoryarray': filtered_order},
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
            
            fig_combined.update_traces(
                texttemplate='%{text:.1f}%',  
                textposition='inside',  
                textfont=dict(color='white', size=14),               
                hovertemplate="<b>%{x}</b><br>" +
                            "Mortality: %{y:.1f}%<br>" +
                            "Patients: %{customdata}<extra></extra>",
                customdata=risk_mortality['Count']
            )
            
            ui.plotly(fig_combined).classes("w-full h-150")
        else:
            ui.html("""
                <div class="p-4 bg-yellow-50 rounded-lg text-base">
                    <p class="text-lg font-bold">No data available for risk categories with current filters</p>
                    <p>Try adjusting your filters to see risk category data.</p>
                </div>
            """)

from nicegui import ui
import pandas as pd
from data.preview import show_data_preview
from visualizations.key_factors import show_key_factors
from visualizations.combined_factors import show_combined_risk_factors
from visualizations.risk_distribution import show_risk_distribution
from advanced_visualization.advanced_visualizations import add_advanced_visualizations
from visualizations.model_results import show_model_results

def add_interactive_filters(df, results_section):
    """Creates interactive filter controls for the patient data dashboard.

    Args:
        df (pd.DataFrame): DataFrame containing patient data
        results_section (ui.element): NiceGUI element where filtered results will be displayed
    """
    try:
        filters_container = ui.column().classes("w-full")

        # Filter controls row
        with filters_container:
            with ui.row().classes("w-full justify-around gap-4 p-2"):
                with ui.column().classes("flex-1"):
                    age_groups = ["All"] + sorted(df["Age Group"].unique().tolist())
                    age_filter = ui.select(
                        options=age_groups, value="All", label="Age Group"
                    ).classes("w-full")

                # Gender Filter
                with ui.column().classes("flex-1"):
                    gender_options = ["All", "Male", "Female"]
                    gender_filter = ui.select(
                        options=gender_options, value="All", label="Gender"
                    ).classes("w-full")

                # Anion Gap Filter
                with ui.column().classes("flex-1"):
                    anion_options = ["All", "≤16.91", ">16.91"]
                    anion_filter = ui.select(
                        options=anion_options, value="All", label="Anion Gap"
                    ).classes("w-full")

                # Renal Failure Filter
                with ui.column().classes("flex-1"):
                    renal_options = ["All", "Yes", "No"]
                    renal_filter = ui.select(
                        options=renal_options, value="All", label="Renal Failure"
                    ).classes("w-full")

            # Action Buttons
            with ui.row().classes("w-full justify-center gap-4 mt-4"):
                ui.button(
                    "Apply Filters",
                    on_click=lambda: apply_filters(
                        df,
                        age_filter,
                        gender_filter,
                        anion_filter,
                        renal_filter,
                        results_section,
                    ),
                    icon="search",
                ).props("color=primary")

                ui.button(
                    "Reset Filters",
                    on_click=lambda: reset_filters(
                        df,
                        age_filter,
                        gender_filter,
                        anion_filter,
                        renal_filter,
                        results_section,
                    ),
                    icon="refresh",
                ).props("color=secondary")

        return age_filter, gender_filter, anion_filter, renal_filter

    except Exception as ex:
        ui.notify(f"Error setting up filters: {ex}", type="negative")
        return None, None, None, None


def reset_filters(
    df, age_filter, gender_filter, anion_filter, renal_filter, results_section
):
    """Resets all filters to their default 'All' values and updates visualizations."""
    try:
        age_filter.value = "All"
        gender_filter.value = "All"
        anion_filter.value = "All"
        renal_filter.value = "All"
        apply_filters(
            df, age_filter, gender_filter, anion_filter, renal_filter, results_section
        )

        ui.notify("Filters reset successfully", type="positive")
    except Exception as ex:
        ui.notify(f"Error resetting filters: {ex}", type="negative")


def apply_filters(
    df, age_filter, gender_filter, anion_filter, renal_filter, results_section
):
    """Applies selected filters and updates visualizations

    Args:
        df (pd.DataFrame): Original dataset to filter
        age_filter (ui.select): Age group filter component
        gender_filter (ui.select): Gender filter component
        anion_filter (ui.select): Anion gap filter component
        renal_filter (ui.select): Renal failure filter component
        results_section (ui.element): NiceGUI element where filtered results will be displayed
    """
    try:
        filtered_df = df.copy()

        if age_filter.value != "All":
            filtered_df = filtered_df[filtered_df["Age Group"] == age_filter.value]

        if gender_filter.value != "All":
            filtered_df = filtered_df[filtered_df["Gender"] == gender_filter.value]

        if anion_filter.value != "All":
            if anion_filter.value == "≤16.91":
                filtered_df = filtered_df[filtered_df["Anion gap"] <= 16.91]
            else:
                filtered_df = filtered_df[filtered_df["Anion gap"] > 16.91]

        if renal_filter.value != "All":
            has_renal = renal_filter.value == "Yes"
            filtered_df = filtered_df[
                filtered_df["Rel failure"] == (1 if has_renal else 0)
            ]

        update_visualizations(
            filtered_df,
            age_filter.value,
            gender_filter.value,
            anion_filter.value,
            renal_filter.value,
            results_section,
        )

        ui.notify(
            f"Filters applied: {len(filtered_df)} patients match criteria",
            type="positive",
        )

    except Exception as ex:
        ui.notify(f"Error applying filters: {ex}", type="negative")
        print(f"Error in apply_filters: {ex}")


def update_visualizations(
    filtered_df, age_group, gender, anion_gap, renal_failure, results_section
):
    """Updates all visualization components with the filtered dataset."""

    try:
        results_section.clear()

        with results_section:
            # Create collapsible data preview
            with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                with ui.row().classes(
                    "w-full items-center p-4 cursor-pointer bg-gray-50"
                ) as header:
                    ui.label(f"Data Preview ({len(filtered_df)} patients)").classes(
                        "text-xl font-bold flex-grow"
                    )
                    expand_icon = ui.icon("expand_more")

                with ui.column().classes("w-full p-4") as content:
                    show_data_preview(filtered_df)

                def toggle():
                    content.visible = not content.visible
                    expand_icon.props(
                        f'icon={"expand_less" if content.visible else "expand_more"}'
                    )

                header.on("click", toggle)

            with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                ui.label("Overview").classes("text-xl font-bold p-4 bg-gray-50")
                with ui.column().classes("w-full p-4"):
                    show_key_factors(filtered_df)

            with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                ui.label("Combined Risk Factors").classes(
                    "text-xl font-bold p-4 bg-gray-50"
                )
                with ui.column().classes("w-full p-4"):
                    show_combined_risk_factors(filtered_df)

            with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                ui.label("Risk Distribution").classes(
                    "text-xl font-bold p-4 bg-gray-50"
                )
                with ui.column().classes("w-full p-4"):
                    show_risk_distribution(filtered_df)

            with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                ui.label("Advanced Visualizations").classes(
                    "text-xl font-bold p-4 bg-gray-50"
                )
                with ui.column().classes("w-full p-4"):
                    add_advanced_visualizations(filtered_df)

            ui.separator().classes("my-8")

            with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                ui.label("Model Results").classes("text-xl font-bold p-4 bg-gray-50")
                with ui.column().classes("w-full p-4"):
                    show_model_results()
    except Exception as ex:
        ui.notify(f"Error updating visualizations: {ex}", type="negative")
        print(f"Error in update_visualizations: {ex}")

import unittest
import pandas as pd
import sys
from unittest.mock import patch, MagicMock
from pathlib import Path
from nicegui import ui

sys.path.append(str(Path(__file__).parent.parent))
from src.visualizations.key_factors import show_key_factors

class TestKeyFactors(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Mortality': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
            'Anion gap': [17.0, 16.0, 18.0, 15.0, 19.0, 14.0],
            'Rel failure': [1, 0, 1, 0, 1, 0]
        })

    @patch('nicegui.ui.plotly')
    @patch('nicegui.ui.row')
    @patch('nicegui.ui.card')
    @patch('nicegui.ui.column')
    @patch('nicegui.ui.label')
    @patch('nicegui.ui.html')
    def test_patient_statistics(self, mock_html, mock_label, mock_column, mock_card, mock_row, mock_plotly):
        show_key_factors(self.df)
        
        total_patients = len(self.df)
        self.assertEqual(total_patients, 6)
        mortality_count = (self.df['Mortality'] == 'Yes').sum()
        self.assertEqual(mortality_count, 3)
        survival_rate = 50.0
        self.assertEqual((total_patients - mortality_count) / total_patients * 100, survival_rate)

    @patch('nicegui.ui.plotly')
    @patch('nicegui.ui.row')
    @patch('nicegui.ui.card')
    @patch('nicegui.ui.label')
    @patch('nicegui.ui.html')
    def test_anion_gap_analysis(self, mock_html, mock_label, mock_card, mock_row, mock_plotly):
        show_key_factors(self.df)
        
        anion_high = self.df['Anion gap'] > 16.91
        mortality_high_anion = (self.df[anion_high]['Mortality'] == 'Yes').mean() * 100
        self.assertAlmostEqual(mortality_high_anion, 100.0)

    @patch('nicegui.ui.plotly')
    @patch('nicegui.ui.row')
    @patch('nicegui.ui.card')
    @patch('nicegui.ui.label')
    @patch('nicegui.ui.html')
    def test_renal_failure_analysis(self, mock_html, mock_label, mock_card, mock_row, mock_plotly):
        show_key_factors(self.df)
        
        renal_failure = self.df['Rel failure'] > 0
        mortality_with_renal = (self.df[renal_failure]['Mortality'] == 'Yes').mean() * 100
        self.assertEqual(mortality_with_renal, 100.0)

    @patch('nicegui.ui.notify')
    def test_error_handling(self, mock_notify):
        invalid_df = pd.DataFrame({'Invalid': ['data']})
        show_key_factors(invalid_df)
        mock_notify.assert_called_once()

if __name__ == '__main__':
    unittest.main()

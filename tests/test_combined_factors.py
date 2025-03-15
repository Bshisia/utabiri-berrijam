import unittest
import pandas as pd
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
from nicegui import ui

sys.path.append(str(Path(__file__).parent.parent))
from src.visualizations.combined_factors import show_combined_risk_factors

class TestCombinedRiskFactors(unittest.TestCase):
    def setUp(self):
        """Setup test data"""
        self.df = pd.DataFrame({
            'Mortality': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
            'Anion gap': [17.0, 16.0, 18.0, 15.0, 19.0, 14.0],
            'Rel failure': [1, 0, 1, 0, 1, 0]
        })

    def test_risk_category_assignment(self):
        """Test correct assignment of risk categories"""
        show_combined_risk_factors(self.df)
        expected_categories = ['High Anion Gap + Rel Failure', 'No Risk Factors',
                             'High Anion Gap + Rel Failure', 'No Risk Factors',
                             'High Anion Gap + Rel Failure', 'No Risk Factors']
        self.assertEqual(list(self.df['Risk_Category']), expected_categories)

    @patch('nicegui.ui.plotly')
    @patch('nicegui.ui.card')
    @patch('nicegui.ui.html')
    def test_mortality_calculations(self, mock_html, mock_card, mock_plotly):
        """Test mortality rate calculations"""
        show_combined_risk_factors(self.df)
        high_risk = self.df[self.df['Risk_Category'] == 'High Anion Gap + Rel Failure']
        mortality_rate = (high_risk['Mortality'] == 'Yes').mean() * 100
        self.assertEqual(mortality_rate, 100.0)

    @patch('nicegui.ui.plotly')
    @patch('nicegui.ui.card')
    @patch('nicegui.ui.html')
    def test_visualization_generation(self, mock_html, mock_card, mock_plotly):
        """Test visualization components are created"""
        show_combined_risk_factors(self.df)
        mock_plotly.assert_called_once()

    def test_empty_data_handling(self):
        """Test handling of empty DataFrame"""
        empty_df = pd.DataFrame(columns=['Mortality', 'Anion gap', 'Rel failure'])
        with self.assertRaises(Exception):
            show_combined_risk_factors(empty_df)

    def test_missing_columns(self):
        """Test handling of missing columns"""
        invalid_df = pd.DataFrame({'Invalid': [1, 2, 3]})
        with self.assertRaises(Exception):
            show_combined_risk_factors(invalid_df)

if __name__ == '__main__':
    unittest.main()
import unittest
import pandas as pd
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.data.preview import show_data_preview

class TestDataPreview(unittest.TestCase):
    def setUp(self):
        """Setup test data"""
        self.test_df = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5, 6],
            'col2': ['a', 'b', 'c', 'd', 'e', 'f']
        })

    @patch('nicegui.ui.table')
    @patch('nicegui.ui.label')
    @patch('nicegui.ui.card')
    def test_preview_generation(self, mock_card, mock_label, mock_table):
        """Test data preview table generation"""
        show_data_preview(self.test_df)
        
        mock_table.assert_called_once()
        args = mock_table.call_args[1]
        self.assertEqual(len(args['rows']), 5)
        
        self.assertTrue(all('#' in row for row in args['rows']))

    @patch('nicegui.ui.table')
    @patch('nicegui.ui.label')
    @patch('nicegui.ui.card')
    def test_column_formatting(self, mock_card, mock_label, mock_table):
        """Test column configuration"""
        show_data_preview(self.test_df)
        
        args = mock_table.call_args[1]
        expected_columns = [
            {"name": "#", "label": "#", "field": "#"},
            {"name": "col1", "label": "col1", "field": "col1"},
            {"name": "col2", "label": "col2", "field": "col2"}
        ]
        self.assertEqual(args['columns'], expected_columns)

    @patch('nicegui.ui.table')
    @patch('nicegui.ui.label')
    @patch('nicegui.ui.card')
    def test_row_count_display(self, mock_card, mock_label, mock_table):
        """Test row count display"""
        show_data_preview(self.test_df)
        
        mock_label.assert_any_call(f"Showing 5 of {len(self.test_df)} records")

    @patch('nicegui.ui.table')
    @patch('nicegui.ui.label')
    @patch('nicegui.ui.card')
    def test_empty_dataframe(self, mock_card, mock_label, mock_table):
        """Test handling of empty DataFrame"""
        empty_df = pd.DataFrame()
        show_data_preview(empty_df)
        
        mock_table.assert_called_once()
        args = mock_table.call_args[1]
        self.assertEqual(len(args['rows']), 0)

if __name__ == '__main__':
    unittest.main()
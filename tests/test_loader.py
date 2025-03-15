import unittest
import pandas as pd
import os
from io import StringIO
from unittest.mock import patch, mock_open, MagicMock
from pathlib import Path

from src.data.loader import load_data, create_age_groups, DATA_PATH

class TestLoader(unittest.TestCase):
    def setUp(self):
        self.sample_data = """age,sex,cp,trestbps,chol
29,1,2,130,204
45,0,1,135,232
55,1,0,140,226
65,0,2,145,283
75,1,1,150,269"""
        self.sample_df = pd.read_csv(StringIO(self.sample_data))

    @patch('os.path.exists')
    @patch('pandas.read_csv')
    def test_load_data_success(self, mock_read_csv, mock_exists):
        mock_exists.return_value = True
        mock_read_csv.return_value = self.sample_df
        
        result = load_data()
        
        mock_exists.assert_called_once_with(DATA_PATH)
        mock_read_csv.assert_called_once_with(DATA_PATH)
        self.assertIsNotNone(result)
        pd.testing.assert_frame_equal(result, self.sample_df)

    @patch('os.path.exists')
    def test_load_data_file_not_found(self, mock_exists):
        mock_exists.return_value = False
        result = load_data()
        self.assertIsNone(result)

    def test_create_age_groups_success(self):
        df = pd.DataFrame({
            'age': [25, 45, 65, 85]
        })
        result = create_age_groups(df)
        
        expected_groups = ['<40', '40-60', '60-80', '>80']
        self.assertTrue('Age Group' in result.columns)
        self.assertEqual(list(result['Age Group'].unique()), expected_groups)

    def test_create_age_groups_missing_column(self):
        df = pd.DataFrame({
            'other_column': [1, 2, 3]
        })
        result = create_age_groups(df)
        self.assertEqual(result.equals(df), True)

    def test_create_age_groups_invalid_ages(self):
        df = pd.DataFrame({
            'age': [-1, 150, 'invalid']
        })
        result = create_age_groups(df)
        self.assertEqual(result.equals(df), True)

if __name__ == '__main__':
    unittest.main()
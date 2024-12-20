import unittest
from unittest.mock import patch, MagicMock
from manage_hourly_employee_access.manage_hourly_employee_access import (
    get_access_token,
    get_hourly_employees,
    check_employee_hours,
    manage_ms_teams_chat
)

class TestManageHourlyEmployeeAccess(unittest.TestCase):

    @patch("manage_hourly_employee_access.manage_hourly_employee_access.requests.post")
    def test_get_access_token(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"access_token": "test_token"}
        token = get_access_token("client_id", "client_secret", "tenant_id")
        self.assertEqual(token, "test_token")

    @patch("manage_hourly_employee_access.manage_hourly_employee_access.requests.get")
    def test_get_hourly_employees(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"value": [{"id": "employee1"}, {"id": "employee2"}]}
        employees = get_hourly_employees("test_token", "group_id")
        self.assertEqual(employees, ["employee1", "employee2"])

    def test_check_employee_hours_clocking_in(self):
        with patch("manage_hourly_employee_access.manage_hourly_employee_access.check_employee_hours", return_value="clocking_in") as mock_check:
            status = check_employee_hours("employee1", "test_token")
            self.assertEqual(status, "clocking_in")
            mock_check.assert_called_once_with("employee1", "test_token")

    def test_check_employee_hours_clocked_out(self):
        with patch("manage_hourly_employee_access.manage_hourly_employee_access.check_employee_hours", return_value="clocked_out") as mock_check:
            status = check_employee_hours("employee1", "test_token")
            self.assertEqual(status, "clocked_out")
            mock_check.assert_called_once_with("employee1", "test_token")

    @patch("manage_hourly_employee_access.manage_hourly_employee_access.requests.patch")
    def test_manage_ms_teams_chat_clocking_in(self, mock_patch):
        mock_patch.return_value.status_code = 200
        manage_ms_teams_chat("employee1", "clocking_in", "test_token")
        mock_patch.assert_called_once_with(
            "https://graph.microsoft.com/v1.0/users/employee1/presence",
            headers={"Authorization": "Bearer test_token"},
            json={"availability": "Available"}
        )

    @patch("manage_hourly_employee_access.manage_hourly_employee_access.requests.patch")
    def test_manage_ms_teams_chat_clocked_out(self, mock_patch):
        mock_patch.return_value.status_code = 200
        manage_ms_teams_chat("employee1", "clocked_out", "test_token")
        mock_patch.assert_called_once_with(
            "https://graph.microsoft.com/v1.0/users/employee1/presence",
            headers={"Authorization": "Bearer test_token"},
            json={"availability": "Offline"}
        )

if __name__ == "__main__":
    unittest.main()

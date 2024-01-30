from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.user import User

class ShowUsersCommand(BaseCommand):

    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)




    def execute(self, params):
        super().execute(params)
        user = self._app_data.find_user_by_username(params[0])
        if user.is_admin == True and ApplicationData.has_logged_in_user:
            return ApplicationData.print_users()

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 1




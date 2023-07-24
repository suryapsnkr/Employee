from django.contrib.auth.models import BaseUserManager


class EmployeeManager(BaseUserManager):
    def create_user(self, eid, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not eid:
            raise ValueError("Employees must have an employee_id")

        user = self.model(
            eid=eid
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, eid, password=None):
        """
        Creates and saves a superuser with the given employee_id, and password.
        """
        user = self.create_user(
            eid,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
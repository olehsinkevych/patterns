"""Contains Developer, QAEngineer and PM implementation.

class Developer
class QAEngineer
class ProjectManager

"""

from __future__ import annotations
from typing import List, Any, Optional


class Developer:
    """Developer representation.

    Attributes:
        full_name (str): first + last names
        address (str): registration address
        email (str): personal company e-mail
        projects (List[Projects]): list of assigned projects
                        (many-to-many with Project instance)

    """

    def __init__(self, full_name: str, address: str, email: str) -> None:
        """Developer's initializer"""
        self.full_name: str = full_name
        self.address: str = address
        self.email: str = email
        self.projects: List[Any] = []

    def assign(self, project: Any) -> Optional[bool]:
        """Assigns current developer to project instance.

        Arguments:
            project (Project): Project instance to be assigned to developer.
        """
        if project in self.projects:
            raise ValueError(f"Project {project.title} already exists")
        self.projects.append(project)
        return True

    def unassign(self, project: Any) -> Optional[bool]:
        """Assigns current developer to project instance.

        Arguments:
            project (Project): Project instance to be removed from developer.
        """
        pass

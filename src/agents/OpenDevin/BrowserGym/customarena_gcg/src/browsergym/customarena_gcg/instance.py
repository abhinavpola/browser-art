import playwright.sync_api
import requests


class CustomArenaInstance:
    """
    Utility class to access a WebArena instance.

    """

    def __init__(
        self,
    ) -> None:
        # import webarena on instanciation
        from .env_config import (
            NOTION,
            TWITTER,
            HOMEPAGE,
            EMAIL,
            REVIEW,
            CRM,
            API_KEY,
            GOOGLE,
            GITLAB_ISSUE,
            GITHUB_DOCKER_BUILD,
            LOGIN,
            GITHUB_PR,
            WEB_GITLAB,
        )
        self.urls = {
            "notion": NOTION,
            "twitter": TWITTER,
            "api_key": API_KEY,
            "email": EMAIL,
            "crm": CRM,
            "review": REVIEW,
            "gitlab_issue": GITLAB_ISSUE,
            "google": GOOGLE,
            'github_docker_build': GITHUB_DOCKER_BUILD,
            'github_pr': GITHUB_PR,
            'login': LOGIN,
            'gitlab': WEB_GITLAB,
        }
        self.home_url = HOMEPAGE

        print("Environment URLS : ", self.urls)

    def check_status(self):
        """
        Check the status of the instance. Raises an error if the instance is not ready to be used.

        """
        self._check_is_reachable()

    def _check_is_reachable(self):
        """
        Test that every website is reachable.

        """
        for site, url in self.urls.items():
            print(url)
            try:
                requests.get(url, timeout=5000)  # 5 secs
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
                raise RuntimeError(
                    f'WebArena site "{site}" ({url}) is not reacheable. Please check the URL.'
                )

    def ui_login(self, site: str, page: playwright.sync_api.Page):
        """
        Should only be called once per site (expects user to be logged out).
        """
        url = self.urls[site]
        print("Browsing to Site ", site, url)
        print("Loading")
        page.goto(url, wait_until="domcontentloaded")

        # match site:
        #     case "TWITTER":
        #         page.goto(f"{url}")
                
        #     case "NOTION":
        #         page.goto(f"{url}")
            
        #     case "REVIEW":
        #         page.goto(f"{url}")
                
        #     case "":
        #         page.goto(f"{url}")

        #     case _:
        #         raise ValueError

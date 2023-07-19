from httpx_oauth.clients.github import GitHubOAuth2

from src.core.config.settings import get_settings

settings = get_settings()

github_oauth_client = GitHubOAuth2(
    settings.github_client_id, settings.github_client_secret)

import requests
import json
from typing import Any, Dict
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class SafetyGuardrailsProvider(ToolProvider):
    
    def _validate_credentials(self, credentials: Dict[str, Any]) -> None:
        """
        Validate the provider credentials by testing API connection
        
        Args:
            credentials: Dictionary containing api_username and api_password
            
        Raises:
            CredentialsValidateFailedError: If credentials are invalid
        """
        try:
            # Extract credentials
            api_username = credentials.get("api_username")
            api_password = credentials.get("api_password")
            
            if not api_username or not api_password:
                raise ToolProviderCredentialValidationError("API username and password are required")
            
            # Test API connection by getting access token
            token_url = "https://safeai.shuanzhineng.com:8081/api/account/oauth2/token"
            token_data = {
                "username": api_username,
                "password": api_password
            }
            
            response = requests.post(
                token_url,
                data=token_data,  # 使用data而不是json
                timeout=10
            )
            
            if response.status_code != 200:
                try:
                    error_detail = response.json()
                    raise ToolProviderCredentialValidationError(
                        f"Failed to authenticate with Safety API. Status: {response.status_code}, Response: {error_detail}"
                    )
                except:
                    raise ToolProviderCredentialValidationError(
                        f"Failed to authenticate with Safety API. Status: {response.status_code}, Response: {response.text}"
                    )
            
            result = response.json()
            print(f"API Response: {result}")  # 调试输出
            
            # API返回的token在details字段中
            access_token = None
            if result.get("details") and result["details"].get("access_token"):
                access_token = result["details"]["access_token"]
            elif result.get("access_token"):
                access_token = result.get("access_token")
            elif result.get("token"):
                access_token = result.get("token")
            elif result.get("accessToken"):
                access_token = result.get("accessToken")
                
            if not access_token:
                raise ToolProviderCredentialValidationError(
                    f"Invalid response from Safety API - no access token received. Response: {result}"
                )
                
        except requests.exceptions.RequestException as e:
            raise ToolProviderCredentialValidationError(f"Network error: {str(e)}")
        except json.JSONDecodeError:
            raise ToolProviderCredentialValidationError("Invalid JSON response from Safety API")
        except Exception as e:
            raise ToolProviderCredentialValidationError(f"Credential validation failed: {str(e)}")

    #########################################################################################
    # If OAuth is supported, uncomment the following functions.
    # Warning: please make sure that the sdk version is 0.4.2 or higher.
    #########################################################################################
    # def _oauth_get_authorization_url(self, redirect_uri: str, system_credentials: Mapping[str, Any]) -> str:
    #     """
    #     Generate the authorization URL for safety_guardrails OAuth.
    #     """
    #     try:
    #         """
    #         IMPLEMENT YOUR AUTHORIZATION URL GENERATION HERE
    #         """
    #     except Exception as e:
    #         raise ToolProviderOAuthError(str(e))
    #     return ""
        
    # def _oauth_get_credentials(
    #     self, redirect_uri: str, system_credentials: Mapping[str, Any], request: Request
    # ) -> Mapping[str, Any]:
    #     """
    #     Exchange code for access_token.
    #     """
    #     try:
    #         """
    #         IMPLEMENT YOUR CREDENTIALS EXCHANGE HERE
    #         """
    #     except Exception as e:
    #         raise ToolProviderOAuthError(str(e))
    #     return dict()

    # def _oauth_refresh_credentials(
    #     self, redirect_uri: str, system_credentials: Mapping[str, Any], credentials: Mapping[str, Any]
    # ) -> OAuthCredentials:
    #     """
    #     Refresh the credentials
    #     """
    #     return OAuthCredentials(credentials=credentials, expires_at=-1)

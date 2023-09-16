import qs from "qs";

import JutsuService from "../jutsu-service";

class AuthService extends JutsuService {
  signUp = async (email: string, password: string) => {
    try {
      const response = await this.api.post("/auth/register", {
        email,
        password,
      });
      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  login = async ({
    username,
    password,
  }: {
    username: string;
    password: string;
  }) => {
    const data = qs.stringify({
      username,
      password,
    });

    const config = {
      headers: { "content-type": "application/x-www-form-urlencoded" },
    };
    try {
      const response = await this.api.post("/auth/login", data, config);

      return response.data;
    } catch (error: any) {
      console.log(error);
      /* this.defaultErrorMessages(error); */
    }
  };

  logout = async () => {
    try {
      const response = await this.api.post("/auth/logout");
      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  requestVerifyToken = async (email: string) => {
    try {
      const response = await this.api.post("/auth/request-verify-token", {
        email,
      });

      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  verifyUser = async (token: string) => {
    try {
      const response = await this.api.post("/auth/verify", {
        token,
      });

      return response;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  requestResetPassword = async (email: string) => {
    try {
      const response = await this.api.post("/auth/forgot-password", {
        email,
      });

      return response;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  resetPassword = async (token: string, password: string) => {
    try {
      const response = await this.api.post("/auth/reset-password", {
        token,
        password,
      });

      return response;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  getCurrentUser = async () => {
    try {
      const response = await this.api.get('/users/me')

    return response;
    } catch(error: any) {
    this.defaultErrorMessages(error)
    }
  }
}

const authService = new AuthService();

export default authService;

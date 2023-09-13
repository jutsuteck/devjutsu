import axios from "axios";
import qs from "qs";

class AuthService {
  private axiosInstance: any;

  constructor() {
    this.axiosInstance = axios.create({
      baseURL: process.env.NEXT_PUBLIC_AUTH_SERVICE_API_URL,
    });

    this.login = this.login.bind(this);

    this.axiosInstance.interceptors.request.use((config: any) => {
      const token = localStorage.getItem("access_token");

      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }

      return config;
    });
  }

  async signUp(email: string, password: string) {
    try {
      const response = await this.axiosInstance.post("/auth/register", {
        email,
        password,
      });
      return response.data;
    } catch (error: any) {
      /* console.log(error); */
      this.catchError(error);
    }
  }

  async login({ username, password }: { username: string; password: string }) {
    const data = qs.stringify({
      username,
      password,
    });

    const config = {
      headers: { "content-type": "application/x-www-form-urlencoded" },
    };
    try {
      const response = await this.axiosInstance.post(
        "/auth/login",
        data,
        config
      );

      return response.data;
    } catch (error: any) {
      this.catchError(error);
    }
  }

  async logout() {
    try {
      const response = await this.axiosInstance.post("/auth/logout");
      return response.data;
    } catch (error: any) {
      this.catchError(error);
    }
  }

  async requestVerifyToken(email: string) {
    try {
      const response = await this.axiosInstance.post(
        "/auth/request-verify-token",
        {
          email,
        }
      );

      return response.data;
    } catch (error: any) {
      this.catchError(error);
    }
  }

  async verifyUser(token: string) {
    try {
      const response = await this.axiosInstance.post("/auth/verify", {
        token,
      });

      return response;
    } catch (error: any) {
      this.catchError(error);
    }
  }

  private catchError(error: any) {
    let errorMessage = "Unexpected error. Try again.";

    if (error.response) {
      if (error.response.status === 400) {
        errorMessage = "Invalid data.";
      } else if (error.response.status === 409) {
        errorMessage = "Email already exists.";
      } else if (error.response.status == 422) {
        errorMessage = error.response.data.message || "Data error.";
      } else if (error.response.status === 500) {
        errorMessage = "Server error. Try again.";
      } else {
        errorMessage = error.response.data.message || errorMessage;
      }
    } else if (error.request) {
      errorMessage = "No server response. Check connection.";
    }

    throw errorMessage;
  }
}

const authService = new AuthService();

export default authService;

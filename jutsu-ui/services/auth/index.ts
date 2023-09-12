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
      const token = localStorage.getItem("access_token)");

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
        "/auth/jwt/login",
        data,
        config
      );

      return response.data;
    } catch (error: any) {
      console.error("Full error: ", error);
      let errorMessage = "An unexpected error occurred. Please try again.";

      if (error.response) {
        if (error.response.status === 400) {
          errorMessage = "Invalid data provided. Please check your input";
        } else if (error.response.status === 409) {
          errorMessage = "An account with this email already exists.";
        } else if (error.response.status == 422) {
          errorMessage =
            error.response.data.message || "Data cannot be processed";
        } else if (error.response.status === 500) {
          errorMessage = "Server error. Please try again later";
        } else {
          errorMessage = error.response.data.message || errorMessage;
        }
      } else if (error.request) {
        errorMessage =
          "No response from the server. Please check your connection.";
      }

      throw new Error(errorMessage);
    }
  }

  async logout() {
    try {
      const response = await this.axiosInstance.post("/auth/jwt/logout");
      return response.data;
    } catch (error: any) {
      this.catchError(error);
    }
  }

  private catchError(error: any) {
    let errorMessage = "An unexpected error occurred. Please try again.";

    if (error.response) {
      if (error.response.status === 400) {
        errorMessage = "Invalid data provided. Please check your input";
      } else if (error.response.status === 409) {
        errorMessage = "An account with this email already exists.";
      } else if (error.response.status == 422) {
        errorMessage =
          error.response.data.message || "Data cannot be processed";
      } else if (error.response.status === 500) {
        errorMessage = "Server error. Please try again later";
      } else {
        errorMessage = error.response.data.message || errorMessage;
      }
    } else if (error.request) {
      errorMessage =
        "No response from the server. Please check your connection.";
    }

    throw new Error(errorMessage);
  }
}

const authService = new AuthService();

export default authService;

import axios from "axios";

abstract class JutsuService {
  protected api: any;

  constructor() {
    this.api = axios.create({
      baseURL: process.env.NEXT_PUBLIC_AUTH_SERVICE_API_URL,
    });

    this.api.interceptors.request.use((config: any) => {
      const token = localStorage.getItem("access_token");
      console.log(token);

      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }

      return config;
    });
  }

  protected defaultErrorMessages = (error: any) => {
    let errorMessage = "Unexpected error. Try again.";

    if (error.response) {
      if (error.response.status === 400) {
        errorMessage = "Invalid data.";
      } else if (error.response.status === 401) {
        errorMessage = "Unauthorized to access this page";
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
  };
}

export default JutsuService;

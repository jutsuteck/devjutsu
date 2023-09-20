import axios from "axios";

abstract class JutsuService {
  protected api: any;

  constructor() {
    this.api = axios.create({
      baseURL: process.env.NEXT_PUBLIC_AUTH_SERVICE_API_URL,
    });
    this.api.interceptors.request.use((config: any) => {
      const token = localStorage.getItem("access_token");
      console.log("Token from local storage:", token);

      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }

      return config;
    });
  }

  protected defaultErrorMessages = (error: any) => {
    let errorMessage = "Oops! We hit a snag. Give it another whirl.";

    if (error.response) {
      if (error.response.status === 400) {
        errorMessage = "Whoopsie daisy! Looks like you sent some wonky data.";
      } else if (error.response.status === 401) {
        errorMessage = "Hold up! You need special clearance for this area.";
      } else if (error.response.status === 409) {
        errorMessage = "Déjà vu! This email's already in our dance card.";
      } else if (error.response.status == 422) {
        errorMessage =
          error.response.data.message ||
          "Hmm... Something's off with the data you sent.";
      } else if (error.response.status === 500) {
        errorMessage =
          "Yikes! Our servers are having a hiccup. Try again in a jiffy.";
      } else {
        errorMessage = error.response.data.message || errorMessage;
      }
    } else if (error.request) {
      errorMessage =
        "Hello? Hello? Server seems to be playing hide and seek. Check your connection.";
    }

    throw errorMessage;
  };
}

export default JutsuService;

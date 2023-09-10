import axios from "axios";

const AUTH_SERVICE_URL = process.env.AUTH_SERVICE_API_URL;

/**
 * Registers a new user.
 *
 * @param  email: The email address of the user.
 * @param password: The password for the user.
 * @returns The data returned from the registration endpoint.
 * @throws Throws an error if registration fails.
 */
export const signUp = async (email: string, password: string) => {
  try {
    const response = await axios.post(`http://127.0.0.1:8001/auth/register`, {
      email,
      password,
    });
    return response.data;
  } catch (error: any) {
    let errorMessage = "An unexpected error occurred. Please try again.";

    if (error.response) {
      if (error.response.message === 400) {
        errorMessage = "Invalid data provided. Please check your input";
      } else if (error.response.status === 409) {
        errorMessage = "An account with this email already exists.";
      } else if (error.response.status == 422) {
        errorMessage = "Data can not be processed.";
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
};

export const loginUser = async (email: string, password: string) => {
  try {
    const response = await axios.post(`${AUTH_SERVICE_URL}/auth/login`, {
      email,
      password,
    });
  } catch (error) {
    let errorMessage = "An unexpected error occured Please try again.";
  }
};

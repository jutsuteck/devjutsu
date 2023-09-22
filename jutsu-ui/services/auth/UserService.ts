import JutsuService from "../jutsu-service";

class UserService extends JutsuService {
  getCurrentUser = async () => {
    try {
      const response = await this.api.get("/users/me");

      return response.data;
    } catch (error: any) {
      this.defaultErrorMessages(error);
    }
  };

  updateCurrentUser = async (first_name: string, last_name: string) => {
    try {
      const response = await this.api.patch("/users/me", {
        first_name,
        last_name,
      });

      return response.data;
    } catch (error) {
      this.defaultErrorMessages(error);
    }
  };
}

const userService = new UserService();

export default userService;

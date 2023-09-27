import { UpdateUser } from "@/models/users";
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

  updateCurrentUser = async (data: UpdateUser) => {
    console.log(data);
    try {
      const response = await this.api.patch("/users/me", { ...data });

      return response.data;
    } catch (error) {
      this.defaultErrorMessages(error);
    }
  };
}

const userService = new UserService();

export default userService;

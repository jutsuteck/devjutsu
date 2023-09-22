import { User } from "@/models/users";
import userService from "@/services/auth/UserService";
import { useQuery } from "react-query";

const useCurrentUser = () => {
  return useQuery<User, Error>(["currentUser"], () =>
    userService.getCurrentUser()
  );
};

export default useCurrentUser;

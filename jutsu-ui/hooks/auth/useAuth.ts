import { AuthContext } from "@/contexts/AuthProvider";
import { useContext } from "react";

export const useAuth = () => {
  const context = useContext(AuthContext);

  if (context === undefined) {
    throw new Error("useAuth must be used withing an AuthProvider");
  }

  return context;
};

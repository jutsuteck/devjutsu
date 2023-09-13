import authService from "@/services/auth";
import { useEffect, useState } from "react";

export const useVerifyUser = (token: string) => {
  const [isVerified, setIsVerified] = useState(false);
  const [message, setMessage] = useState<string | undefined>(undefined);

  useEffect(() => {
    (async () => {
      if (token) {
        try {
          const response = await authService.verifyUser(token as string);

          if (response.status === 200) {
            setIsVerified(true);
            setMessage("Verification successfull");
          }
        } catch (error: any) {
          setIsVerified(false);
          setMessage(error);
        }
      }
    })();
  }, [token]);

  return { isVerified, message };
};

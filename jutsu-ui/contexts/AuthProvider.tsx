import useCurrentUser from "@/hooks/users/useCurrentUser";
import authService from "@/services/auth";
import userService from "@/services/auth/UserService";
import { useRouter } from "next/router";
import { FC, ReactNode, createContext, useEffect, useState } from "react";
import { QueryClient, useMutation } from "react-query";

interface AuthContextType {
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  errorMessage: string | null;
  login: (username: string, passwword: string) => void;
  logout: () => void;
}

interface ProviderProps {
  children: ReactNode;
}

export const AuthContext = createContext<AuthContextType | undefined>(
  undefined
);

/**
 * AuthProvider component. Provides authentication context to its children.
 *
 * @param props - Props for the AuthProvider.
 * @returns AuthProvider component.
 */
export const AuthProvider: FC<ProviderProps> = ({ children }) => {
  const [token, setToken] = useState<string | null>(null);
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const {
    data: currentUser,
    isLoading: isLoadingCurrentUser,
    isError: isCurrentUserError,
  } = useCurrentUser();
  const router = useRouter();

  useEffect(() => {
    const storedToken = localStorage.getItem("access_token");
    console.log("Loading user: ", isLoadingCurrentUser);

    if (storedToken) {
      setToken(storedToken);
      setIsAuthenticated(true);
    }

    setIsLoading(false);
  }, [isLoadingCurrentUser]);

  useEffect(() => {
    const handleRouteChange = (url: string) => {
      if (currentUser?.is_onboarded === false && url !== "/onboarding") {
        router.push("/onboarding");
      }
    };

    router.events.on("routeChangeStart", handleRouteChange);

    return () => {
      router.events.off("routeChangeStart", handleRouteChange);
    };
  }, [currentUser, router]);

  const queryClient = new QueryClient();

  const loginMutation = useMutation(authService.login, {
    onSuccess: async (data: any) => {
      setToken(data.access_token);
      setIsAuthenticated(true);
      localStorage.setItem("access_token", data.access_token);

      const user = await userService.getCurrentUser();

      if (user?.is_onboarded === false) {
        router.push("/onboarding");
      } else {
        router.push("/projects");
      }
    },
    onError: (error: any) => {
      setErrorMessage(error);
    },
  });

  const login = (username: string, password: string) => {
    return loginMutation.mutateAsync({ username, password });
  };

  const logout = async () => {
    try {
      await authService.logout();
      setIsAuthenticated(false);
      localStorage.removeItem("access_token");
      // Clear currentUser data on logout
      queryClient.removeQueries("currentUser");
      router.push("/login");
    } catch (error) {
      throw error;
    }
  };

  return (
    <AuthContext.Provider
      value={{
        token,
        isAuthenticated,
        login,
        logout,
        isLoading,
        errorMessage,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

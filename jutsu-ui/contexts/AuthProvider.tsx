import useCurrentUser from "@/hooks/users/useCurrentUser";
import authService from "@/services/auth";
import { useRouter } from "next/router";
import { FC, ReactNode, createContext, useEffect, useState } from "react";
import { useMutation } from "react-query";

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

    if (storedToken) {
      setToken(storedToken);
      setIsAuthenticated(true);
    }

    setIsLoading(false);
  }, []);

  useEffect(() => {
    if (typeof window === "undefined") return;

    if (currentUser?.is_onboarded === false) {
      setTimeout(() => {
        router.push("/onboarding");
      }, 100);
    }
  }, [currentUser, router]);

  const loginMutation = useMutation(authService.login, {
    onSuccess: (data: any) => {
      setToken(data.access_token);
      setIsAuthenticated(true);
      localStorage.setItem("access_token", data.access_token);

      router.push("/projects");
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

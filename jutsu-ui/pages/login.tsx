import { useAuth } from "@/hooks/useAuth";
import { useRouter } from "next/router";
import { NextPage } from "next";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import { useState } from "react";
import { AiFillGithub } from "react-icons/ai";

import { useVerifyUser } from "@/hooks/useVerifyUser";

import CustomInput from "@/components/forms/CustomInput";
import FormGroup from "@/components/forms/FormGroup";
import CenteredContainer from "@/components/layout/CenteredContainer";
import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";
import Alert from "@/components/ui/Alert";
import authService from "@/services/auth";
import { useMutation } from "react-query";

interface LoginFormProps {
  username: string;
  password: string;
}

interface ForgotPasswordFormProps {
  email: string;
}

const loginSchema = yup.object().shape({
  username: yup
    .string()
    .required("Email is required")
    .email("Invalid email format"),
  password: yup.string().required("Password is required"),
});

const forgotPasswordSchema = yup.object().shape({
  email: yup.string().required().email("Invalid email format"),
});

const LoginPage: NextPage = () => {
  const {
    register: registerLogin,
    handleSubmit: handleSubmitLogin,
    formState: { errors: loginErrors },
  } = useForm<LoginFormProps>({
    resolver: yupResolver(loginSchema),
    mode: "onChange",
  });
  const {
    register: registerForgoPassword,
    handleSubmit: handleSubmitForgotPassword,
    formState: { errors: forgotPasswordErrors },
  } = useForm<ForgotPasswordFormProps>({
    resolver: yupResolver(forgotPasswordSchema),
    mode: "onChange",
  });
  const router = useRouter();
  const { token } = router.query;

  const { login, isAuthenticated, errorMessage } = useAuth();

  const { isVerified, message } = useVerifyUser(token as string);
  const [forgotPassword, setForgotPassword] = useState(false);

  const [alertMessage, setAlertMessage] = useState<string | null>(null);

  const onSubmitLogin = (data: LoginFormProps) => {
    try {
      login(data.username, data.password);
    } catch (error) {
      console.log(error);
    }
  };

  const forgetPasswordMutation = useMutation(({ email }) =>
    authService.requestResetPassword(email)
  );

  const onSubmitRequestForgotPassword = (data: ForgotPasswordFormProps) => {
    forgetPasswordMutation.mutate(data, {
      onSuccess: () => {
        setAlertMessage("Check your inbox for further instructions");
      },
      onError: (error: any) => {
        setAlertMessage(error);
      },
    });
  };

  const onClickHandleForgotPassword = () => {
    setForgotPassword(!forgotPassword);
  };

  return (
    <CenteredContainer flexCol>
      {isVerified ||
        (message && (
          <Alert message={message} severity={isVerified ? `info` : `error`} />
        ))}
      {errorMessage && <Alert message={errorMessage} severity="error" />}
      {alertMessage && <Alert message={alertMessage} severity="success" />}
      <Card transparent>
        <h1 className="text-5xl text-nord-snowstorm-light mb-6 text-center">
          {isAuthenticated ? "Logged in" : "Login"}
        </h1>
        <Button
          icon={<AiFillGithub />}
          text="Continue with Github"
          transparent
        />

        <hr className="my-6 border-t border-nord-polar-night-light" />

        {forgotPassword ? (
          <form
            onSubmit={handleSubmitForgotPassword(onSubmitRequestForgotPassword)}
          >
            <FormGroup label="Email">
              <CustomInput
                placeholder="Enter your email address ..."
                name="email"
                type="email"
                register={registerForgoPassword}
                error={forgotPasswordErrors.email?.message}
              />
            </FormGroup>
            <Button type="submit" text="Send reset link" />
          </form>
        ) : (
          <form onSubmit={handleSubmitLogin(onSubmitLogin)}>
            <FormGroup label="Email">
              <CustomInput
                placeholder="Enter your email address ..."
                name="username"
                type="email"
                register={registerLogin}
                error={loginErrors.username?.message}
              />
            </FormGroup>
            <FormGroup label="Password">
              <CustomInput
                placeholder="password ..."
                name="password"
                type="password"
                register={registerLogin}
                error={loginErrors.password?.message}
              />
            </FormGroup>
            <Button type="submit" text="Login" />
          </form>
        )}

        <p
          className="text-center underline mt-6 cursor-pointer"
          onClick={onClickHandleForgotPassword}
        >
          {forgotPassword ? "Back to login" : "Forgot password?"}
        </p>
      </Card>
    </CenteredContainer>
  );
};

export default LoginPage;

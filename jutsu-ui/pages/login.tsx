import { useAuth } from "@/hooks/useAuth";
import { useRouter } from "next/router";
import { NextPage } from "next";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";

import { useVerifyUser } from "@/hooks/useVerifyUser";

import CustomInput from "@/components/forms/CustomInput";
import FormGroup from "@/components/forms/FormGroup";
import CenteredContainer from "@/components/layout/CenteredContainer";
import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";
import Alert from "@/components/ui/Alert";
import { useState } from "react";
import { AiFillGithub, AiFillGoogleCircle } from "react-icons/ai";

interface LoginFormProps {
  username: string;
  password: string;
}

interface ForgotPasswordFormProps {}

const schema = yup.object().shape({});

const LoginPage: NextPage = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormProps>({ resolver: yupResolver(schema) });
  const router = useRouter();
  const { token } = router.query;
  const { isVerified, message } = useVerifyUser(token as string);
  const { login, isAuthenticated } = useAuth();
  const [forgotPassword, setForgotPassword] = useState(false);

  const onSubmitLogin = (data: LoginFormProps) => {
    try {
      login(data.username, data.password);
    } catch (error: any) {
      console.log(error.message);
    }
  };

  const onSubmitRequestForgetPassword = () => {};

  const onClickHandleForgotPassword = () => {
    setForgotPassword(!forgotPassword);
  };

  return (
    <CenteredContainer flexCol>
      {isVerified ||
        (message && (
          <Alert message={message} severity={isVerified ? `info` : `error`} />
        ))}
      <Card transparent>
        <h1 className="text-5xl text-nord-snowstorm-light mb-6 text-center">
          {isAuthenticated ? "Logged in" : "Login"}
        </h1>
        <Button
          icon={<AiFillGithub />}
          text="Continue with Github"
          transparent
        />
        <Button
          icon={<AiFillGoogleCircle />}
          text="Continue with Google"
          className="mt-2"
          transparent
        />

        <hr className="my-6 border-t border-nord-polar-night-light" />

        {forgotPassword ? (
          <form onSubmit={handleSubmit(onSubmitRequestForgetPassword)}>
            <FormGroup label="Email">
              <CustomInput
                placeholder="Enter your email address ..."
                name="email"
                type="email"
                register={register}
              />
            </FormGroup>
            <Button type="submit" text="Send reset link" />
          </form>
        ) : (
          <form onSubmit={handleSubmit(onSubmitLogin)}>
            <FormGroup label="Email">
              <CustomInput
                placeholder="Enter your email address ..."
                name="username"
                type="email"
                register={register}
              />
            </FormGroup>
            <FormGroup label="Password">
              <CustomInput
                placeholder="password ..."
                name="password"
                type="password"
                register={register}
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

import { NextPage } from "next";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";

import CustomInput from "@/components/forms/CustomInput";
import FormGroup from "@/components/forms/FormGroup";
import CenteredContainer from "@/components/layout/CenteredContainer";
import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";
import { useAuth } from "@/hooks/useAuth";

interface LoginFormProps {
  username: string;
  password: string;
}

const schema = yup.object().shape({});

const LoginPage: NextPage = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormProps>({ resolver: yupResolver(schema) });

  const { login, isAuthenticated } = useAuth();

  const onSubmit = (data: LoginFormProps) => {
    try {
      login(data.username, data.password);
    } catch (error: any) {
      console.log(error.message);
    }
  };

  return (
    <CenteredContainer>
      <Card transparent>
        <h1 className="text-5xl text-nord-snowstorm-light mb-6 text-center">
          {isAuthenticated ? "Logged in" : "Login"}
        </h1>
        <form onSubmit={handleSubmit(onSubmit)}>
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
        <p className="text-center underline mt-6">Forgot password?</p>
      </Card>
    </CenteredContainer>
  );
};

export default LoginPage;

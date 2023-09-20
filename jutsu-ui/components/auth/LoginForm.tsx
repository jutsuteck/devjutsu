import { FC, useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";

import FormGroup from "../forms/FormGroup";
import CustomInput from "../forms/CustomInput";
import Button from "../ui/Button";
import { useAuth } from "@/hooks/auth/useAuth";
import { loginSchema } from "@/utils/validationSchemas/auth";
import Alert from "../ui/Alert";

interface LoginFormProps {
  username: string;
  password: string;
}

const LoginForm: FC = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormProps>({
    resolver: yupResolver(loginSchema),
    mode: "onChange",
  });
  const { login } = useAuth();
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  const onSubmitLogin = (data: LoginFormProps) => {
    try {
      login(data.username, data.password);
      setErrorMsg(null); // clear any previous error messages
    } catch (error: any) {
      setErrorMsg(error.message);
    }
  };

  useEffect(() => {
    if (errorMsg) {
      const timer = setTimeout(() => {
        setErrorMsg(null);
      }, 5000);

      return () => clearTimeout(timer);
    }
  }, [errorMsg]);

  return (
    <>
      {errorMsg && <Alert message={errorMsg} severity="error" maxSize="md" />}
      <form onSubmit={handleSubmit(onSubmitLogin)}>
        <FormGroup label="Email">
          <CustomInput
            placeholder="Enter your email address ..."
            name="username"
            type="email"
            register={register}
            error={errors.username?.message}
          />
        </FormGroup>
        <FormGroup label="Password">
          <CustomInput
            placeholder="password ..."
            name="password"
            type="password"
            register={register}
            error={errors.password?.message}
          />
        </FormGroup>
        <Button type="submit" text="Login" fullWidth />
      </form>
    </>
  );
};

export default LoginForm;

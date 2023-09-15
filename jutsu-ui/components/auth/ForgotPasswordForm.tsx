import { FC } from "react";
import { useMutation } from "react-query";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";

import { forgotPasswordSchema } from "@/utils/validationSchemas/auth";
import FormGroup from "../forms/FormGroup";
import CustomInput from "../forms/CustomInput";
import Button from "../ui/Button";
import authService from "@/services/auth";

interface ForgotPasswordFormProps {
  email: string;
}

const ForgotPasswordForm: FC = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ForgotPasswordFormProps>({
    resolver: yupResolver(forgotPasswordSchema),
    mode: "onChange",
  });

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

  return (
    <form onSubmit={handleSubmit(onSubmitRequestForgotPassword)}>
      <FormGroup label="Email">
        <CustomInput
          placeholder="Enter your email address ..."
          name="email"
          type="email"
          register={register}
          error={errors.email?.message}
        />
      </FormGroup>
      <Button type="submit" text="Send reset link" />
    </form>
  );
};

export default ForgotPasswordForm;

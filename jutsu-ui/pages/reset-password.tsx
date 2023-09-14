import CustomInput from "@/components/forms/CustomInput";
import FormGroup from "@/components/forms/FormGroup";
import CenteredContainer from "@/components/layout/CenteredContainer";
import Alert from "@/components/ui/Alert";
import Button from "@/components/ui/Button";
import Card from "@/components/ui/Card";
import authService from "@/services/auth";
import { NextPage } from "next";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation } from "react-query";

interface ResetPasswordForm {
  token: string;
  password: string;
  passwordConfirm: string;
}

const ResetPasswordPage: NextPage = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ResetPasswordForm>({ mode: "onChange" });
  const router = useRouter();
  const { token } = router.query;
  const { alertMessage, setAlertMessage } = useState<string | null>(null);

  const mutation = useMutation(({ token, password }) =>
    authService.resetPassword(token, password)
  );

  const onSubmit = (data: ResetPasswordForm) => {
    mutation.mutate(
      { token: token as string, password: data.password },
      {
        onSuccess: () => {
          router.push("/login");
        },
        onError: (error: Error) => {
          setAlertMessage(error);
        },
      }
    );
  };

  return (
    <CenteredContainer flexCol>
      {mutation.isError && <Alert message={alertMessage} severity="error" />}
      <Card transparent>
        <h1 className="text-center">Reset password</h1>
        <form onSubmit={handleSubmit(onSubmit)}>
          <FormGroup label="Password">
            <CustomInput
              placeholder="Enter new password..."
              name="password"
              type="password"
              register={register}
              error={errors.password?.message}
            />
          </FormGroup>
          <FormGroup label="Confirm password">
            <CustomInput
              placeholder="Confirm new password..."
              name="confirmPassword"
              type="password"
              register={register}
              error={errors.passwordConfirm?.message}
            />
          </FormGroup>
          <Button type="submit" text="Reset password" />
        </form>
      </Card>
    </CenteredContainer>
  );
};

export default ResetPasswordPage;

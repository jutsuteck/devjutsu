import { FC, useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation } from "react-query";
import { yupResolver } from "@hookform/resolvers/yup";

import FormGroup from "@/components/forms/FormGroup";
import CustomInput from "@/components/forms/CustomInput";
import Alert from "../Alert";

import { UpdateUser } from "@/models/users";
import { isRequiredValidation } from "@/utils/validationSchemas/auth";

import userService from "@/services/auth/UserService";

import { GiSamuraiHelmet } from "react-icons/gi";

interface Props {
  onNextStep: () => void;
}

interface UserDetailform {
  name: string;
}

const OnBoardingUserDetail: FC<Props> = ({ onNextStep }) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<UserDetailform>({
    resolver: yupResolver(isRequiredValidation),
    mode: "onChange",
  });
  const [errMsg, setErrMsg] = useState<string | null>(null);

  const mutation = useMutation((data: UpdateUser) =>
    userService.updateCurrentUser(data.name)
  );

  const onSubmit = (data: UserDetailform) => {
    mutation.mutate(data, {
      onSuccess: () => {
        console.log("Username updated");
        onNextStep();
      },
      onError: (error: any) => {
        setErrMsg(error);
      },
    });
  };

  return (
    <>
      {errMsg && <Alert message={errMsg} severity="error" />}
      <form onSubmit={handleSubmit(onSubmit)}>
        <FormGroup
          icon={<GiSamuraiHelmet />}
          label="What's your name?"
          labelStyle="text-xl font-semibold mb-4"
        >
          <CustomInput
            name="name"
            placeholder="e.g. Miyamoto Musashi"
            register={register}
            error={errors.name?.message}
          />
        </FormGroup>
      </form>
    </>
  );
};

export default OnBoardingUserDetail;

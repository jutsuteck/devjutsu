import { NextPage } from "next";
import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "react-query";

import CustomInput from "@/components/forms/CustomInput";
import FormGroup from "@/components/forms/FormGroup";
import Container from "@/components/layout/Container";
import Button from "@/components/ui/Button";
import SettingsSideBar from "@/components/ui/SettingsSideBar";
import TopBar from "@/components/ui/TopBar";

import useCurrentUser from "@/hooks/users/useCurrentUser";
import userService from "@/services/auth/UserService";

import { RxUpdate } from "react-icons/rx";
import { UpdateUser } from "@/models/users";
import { useState } from "react";
import Alert from "@/components/ui/Alert";

interface FormProps {
  name?: string;
  email?: string;
  password?: string;
}

const ProfileSettingsPage: NextPage = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormProps>();
  const { data: currentUser, isLoading, isError } = useCurrentUser();
  const [errMsg, setErrMsg] = useState<string | null>(null);
  const [successMsg, setSuccessMsg] = useState<string | null>(null);

  const queryClient = useQueryClient();

  const mutation = useMutation((data: UpdateUser) =>
    userService.updateCurrentUser(data)
  );

  const onSubmit = (data: FormProps) => {
    mutation.mutate(data, {
      onSuccess: () => {
        queryClient.invalidateQueries("currentUser");
        setSuccessMsg("Account updated!");
        setErrMsg(null);
      },
      onError: (error) => {
        setErrMsg(error);
      },
    });
  };

  return (
    <div>
      <TopBar showBottomSection={false} title="Settings" />
      <Container>
        {/* Sidebar */}
        {errMsg && <Alert message={errMsg} severity="error" />}
        <SettingsSideBar />
        <div className="flex-grow px-8">
          {successMsg && <Alert message={successMsg} severity="success" />}
          <h1 className="text-2xl font-extrabold">Account</h1>
          <hr className="bg-nord-polar-night-medium h-0.5 border-none my-6" />
          <form onSubmit={handleSubmit(onSubmit)}>
            <FormGroup label="Name">
              <CustomInput
                name="name"
                placeholder={currentUser?.name}
                register={register}
                error={errors?.name?.message}
              />
            </FormGroup>

            <Button
              icon={<RxUpdate />}
              text="Update profile"
              type="submit"
              bgFrost
            />
          </form>
        </div>
      </Container>
    </div>
  );
};

export default ProfileSettingsPage;

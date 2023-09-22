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
  firstName?: string;
  lastName?: string;
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
    userService.updateCurrentUser(data.first_name, data.last_name)
  );

  const onSubmit = (formData: FormProps) => {
    const data = {
      first_name: formData.firstName,
      last_name: formData.lastName,
    };

    console.log(data);

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
            <FormGroup label="Firstname">
              <CustomInput
                name="firstName"
                placeholder={
                  currentUser?.first_name
                    ? currentUser?.first_name
                    : "Firstname ..."
                }
                register={register}
                error={errors?.firstName?.message}
              />
            </FormGroup>
            <FormGroup label="Lastname">
              <CustomInput
                name="lastName"
                placeholder={
                  currentUser?.last_name
                    ? currentUser?.last_name
                    : "Lastname ..."
                }
                register={register}
                error={errors?.lastName?.message}
              />
              <Button
                icon={<RxUpdate />}
                text="Update profile"
                type="submit"
                bgFrost
              />
            </FormGroup>
          </form>
        </div>
      </Container>
    </div>
  );
};

export default ProfileSettingsPage;

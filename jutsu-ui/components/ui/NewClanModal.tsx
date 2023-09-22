import { FC, useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "react-query";
import Image from "next/image";

import BaseModal from "../ui/BaseModal";
import FormGroup from "../forms/FormGroup";
import CustomInput from "../forms/CustomInput";
import Button from "../ui/Button";

import { GiNinjaHead } from "react-icons/gi";

interface Props {
  onClose?: () => void;
}

interface FormProps {
  name: string;
}

const NewClanModal: FC<Props> = ({ onClose }) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormProps>({
    mode: "onChange",
  });
  const [errMessage, setErrMessage] = useState(null);

  const onSubmit = () => {
    console.log("clicked");
  };

  return (
    <BaseModal onClose={onClose} maxSize="2xl">
      <h1 className="mb-2 text-lg font-extrabold flex items-center">
        <GiNinjaHead />
        <span className="ml-2">Create a new clan</span>
      </h1>
      <p className="text-nord-polar-night-lightest">
        Gather your coding samurais, and embark on legendary software quests.
        Unite under a new clan banner!
      </p>
      <form onSubmit={handleSubmit(onSubmit)} className="my-4">
        <FormGroup label="Clan name" labelStyle="font-extrabold">
          <CustomInput
            name="name"
            placeholder="e.g. Code Katanas, Bit Bujinkans, Function Fu Masters"
            register={register}
            error={errors.name?.message}
          />
        </FormGroup>
        <Button icon={<GiNinjaHead />} text="Craft the Clan" type="submit" bgFrost />
      </form>
    </BaseModal>
  );
};

export default NewClanModal;

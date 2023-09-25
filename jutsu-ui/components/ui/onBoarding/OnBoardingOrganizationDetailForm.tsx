import { isRequiredValidation } from "@/utils/validationSchemas/auth";
import { yupResolver } from "@hookform/resolvers/yup";
import { FC, useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation } from "react-query";

import Alert from "../Alert";
import FormGroup from "@/components/forms/FormGroup";
import CustomInput from "@/components/forms/CustomInput";

import tenantService from "@/services/auth/TenantService";

import { GoOrganization } from "react-icons/go";
import { UpdateTenant } from "@/models/users";

interface Props {
  onNextStep: () => void;
  currentUserId: string | undefined;
}

interface TenantDetailFormProps {
  name: string;
}

const OnBoardingOrganizationDetailForm: FC<Props> = ({
  onNextStep,
  currentUserId,
}) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<TenantDetailFormProps>({
    resolver: yupResolver(isRequiredValidation),
    mode: "onChange",
  });
  const [errMsg, setErrMsg] = useState<string | null>(null);

  const mutation = useMutation((data: UpdateTenant) =>
    tenantService.createTenant(data.name, data.members?.push(currentUserId))
  );

  const onSubmit = (formData: TenantDetailFormProps) => {
    const data = {
      member_ids: [currentUserId],
      ...formData,
    };

    mutation.mutate(data, {
      onSuccess: () => {
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
          icon={<GoOrganization />}
          label="Organization Name (or Your Personal Brand)"
          labelStyle="text-xl font-semibold mb-4"
        >
          <CustomInput
            name="name"
            placeholder="e.g. John's Dev Studio"
            register={register}
            error={errors.name?.message}
          />
        </FormGroup>
      </form>
    </>
  );
};

export default OnBoardingOrganizationDetailForm;

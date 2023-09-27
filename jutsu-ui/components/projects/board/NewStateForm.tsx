import { Dispatch, FC, SetStateAction, useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "react-query";

import CustomInput from "@/components/forms/CustomInput";

import { NewState } from "@/models/projects";
import stateService from "@/services/projects/StateService";
import useHideForm from "@/hooks/useHideForm";

import { GrAdd } from "react-icons/gr";

interface Props {
  workflowId: string | undefined;
  successMsg: string | null;
  errMsg: string | null;
  setSuccessMsg: Dispatch<SetStateAction<string | null>>;
  setErrMsg: Dispatch<SetStateAction<string | null>>;
}

interface FormProps {
  name: string;
}

const NewStateForm: FC<Props> = ({
  workflowId,
  successMsg,
  errMsg,
  setSuccessMsg,
  setErrMsg,
}) => {
  const [showForm, setShowForm] = useState<boolean>(false);
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormProps>();

  useHideForm(showForm, () => setShowForm(false));

  const queryClient = useQueryClient();

  const mutation = useMutation(
    async (data: NewState) => await stateService.createState(data)
  );

  const onSubmit = (formData: FormProps) => {
    const data = {
      ...formData,
      workflow_id: workflowId,
    };
    mutation.mutate(data, {
      onSuccess: () => {
        queryClient.invalidateQueries(["states", workflowId]);
        setSuccessMsg(`${data.name} column added`);
        setShowForm(false);
      },
      onError: (error: any) => {
        setErrMsg(error);
      },
    });
  };

  return (
    <>
      {showForm && (
        <form onSubmit={handleSubmit(onSubmit)}>
          <CustomInput
            noHeight
            autoComplete="off"
            name="name"
            placeholder="e.g. In Progress"
            register={register}
            error={errors.name?.message}
            borderColor="focus:border-nord-frost-medium"
          />
        </form>
      )}
      {!showForm && (
        <button
          className="bg-nord-polar-night-medium rounded-lg py-2 px-4 shadow-md flex items-center justify-center"
          onClick={() => setShowForm(true)}
        >
          <GrAdd />
          <span className="ml-2 font-semibold">Add column</span>
        </button>
      )}
    </>
  );
};

export default NewStateForm;

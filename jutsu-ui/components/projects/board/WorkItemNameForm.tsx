import { FC, useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "react-query";

import CustomInput from "@/components/forms/CustomInput";
import FormGroup from "@/components/forms/FormGroup";

import { GrAdd } from "react-icons/gr";

import { NewWorkItem } from "@/models/projects";
import useHideForm from "@/hooks/useHideForm";
import workItemService from "@/services/projects/WorkItemService";

interface Props {
  workflowId: string;
  stateId: string;
}

interface FormProps {
  name: string;
}

const WorkItemNameForm: FC<Props> = ({ workflowId, stateId }) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormProps>();
  const [showForm, setShowForm] = useState<boolean>(false);

  useHideForm(showForm, () => setShowForm(false));

  const queryClient = useQueryClient();

  const mutation = useMutation((data: NewWorkItem) =>
    workItemService.createWorkItem(data.workflow_id, data.state_id, data.name)
  );

  const onSubmit = (formData: FormProps) => {
    const data = {
      workflow_id: workflowId,
      state_id: stateId,
      ...formData,
    };

    mutation.mutate(data, {
      onSuccess: () => {
        queryClient.invalidateQueries(["stateWorkItems", stateId]);
        setShowForm(false);
      },
    });
  };

  const onClickToggleForm = () => {
    setShowForm(true);
  };

  return (
    <div className="mb-8">
      {showForm && (
        <form onSubmit={handleSubmit(onSubmit)}>
          <FormGroup>
            <CustomInput
              placeholder="Enter you work ..."
              name="name"
              register={register}
              autoComplete="off"
              borderColor="focus:border-nord-frost-medium"
            />
          </FormGroup>
        </form>
      )}
      {!showForm && (
        <button
          className="mb-4 p-2 rounded-lg bg bg-nord-polar-night-medium shadow-md hover:shadow-lg"
          onClick={onClickToggleForm}
        >
          <GrAdd />
        </button>
      )}
    </div>
  );
};

export default WorkItemNameForm;

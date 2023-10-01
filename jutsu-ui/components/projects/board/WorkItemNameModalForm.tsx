import CustomInput from "@/components/forms/CustomInput";
import useHideForm from "@/hooks/useHideForm";
import { UpdateWorkItem } from "@/models/projects";
import workItemService from "@/services/projects/WorkItemService";
import { FC, useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "react-query";

interface Props {
  stateId: string;
  workItemId: string;
  name?: string;
}

interface FormProps {
  name: string;
}

const WorkItemNameModalForm: FC<Props> = ({ workItemId, name, stateId }) => {
  const [showForm, setShowForm] = useState<boolean>(false);
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormProps>();

  useHideForm(showForm, () => setShowForm(false));

  const useQuery = useQueryClient();

  const mutation = useMutation((data: UpdateWorkItem) =>
    workItemService.updateWorkItem(workItemId, data)
  );

  const onSubmit = (formData: FormProps) => {
    const data = {
      work_item_id: workItemId,
      name: formData.name,
    };

    mutation.mutate(data, {
      onSuccess: () => {
        useQuery.invalidateQueries(["stateWorkItems", stateId]);
        setShowForm(false);
        console.log(data);
      },
      onError: () => {
        console.log(data);
      },
    });
  };

  return (
    <div className="mb-4">
      {showForm && (
        <form onSubmit={handleSubmit(onSubmit)}>
          <input
            className="text-xl font-bold bg-nord-polar-night-medium m-0 p-0 outline-none"
            placeholder={name}
            {...register("name")}
            autoFocus
            autoComplete="off"
          />
        </form>
      )}
      {!showForm && (
        <h1
          className="text-xl font-bold hover:bg-nord-polar-night-light hover:cursor-text rounded p-2 -m-2 transition-colors duration-8000"
          onClick={() => setShowForm(true)}
        >
          {name}
        </h1>
      )}
    </div>
  );
};

export default WorkItemNameModalForm;

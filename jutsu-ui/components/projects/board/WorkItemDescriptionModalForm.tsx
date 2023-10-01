import CustomTextArea from "@/components/forms/CustomTextArea";
import useHideForm from "@/hooks/useHideForm";
import workItemService from "@/services/projects/WorkItemService";
import { FC, useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "react-query";

interface Props {
  workItemId: string;
  description: string | undefined;
  stateId: string;
}

interface FormProps {
  description: string;
}

const WorkItemDescriptionModalForm: FC<Props> = ({
  workItemId,
  description,
  stateId,
}) => {
  const [showForm, setShowForm] = useState<boolean>(false);
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormProps>();

  const useQuery = useQueryClient();

  const mutation = useMutation((data: UpdateWorkItem) =>
    workItemService.updateWorkItem(workItemId, data)
  );

  const onSubmit = (formData: FormProps) => {
    const data = {
      work_item_id: workItemId,
      description: formData.description,
    };

    mutation.mutate(data, {
      onSuccess: () => {
        useQuery.invalidateQueries(["stateWorkItems", stateId]);
      },
    });
  };

  useHideForm(showForm, () => setShowForm(false));

  return (
    <>
      <h1 className="mb-2 text-nord-polar-night-light font-semibold">
        Description
      </h1>
      {showForm && (
        <form>
          <CustomTextArea name="description" register={register} />
        </form>
      )}
      {!showForm && (
        <p onClick={() => setShowForm(true)}>
          {description ? description : "No description"}
        </p>
      )}
    </>
  );
};

export default WorkItemDescriptionModalForm;

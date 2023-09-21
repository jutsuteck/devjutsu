import CustomInput from "@/components/forms/CustomInput";
import FormGroup from "@/components/forms/FormGroup";
import { NewWorkItem } from "@/models/projects";
import workItemService from "@/services/projects/WorkItemService";
import { FC, useEffect, useRef, useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "react-query";
import { GrAdd } from "react-icons/gr";

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

  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (showForm && inputRef.current) {
      inputRef.current.focus();
    }
  }, [showForm]);

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

  useEffect(() => {
    const handleEscapePress = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        setShowForm(false);
      }
    };

    const handleFocusOut = (event: FocusEvent) => {
      if (!event.currentTarget.contains(event.relatedTarget as Node)) {
        setShowForm(false);
      }
    };

    if (showForm) {
      document.addEventListener("keydown", handleEscapePress);
      document.addEventListener("focusout", handleFocusOut);
    }

    return () => {
      document.removeEventListener("keydown", handleEscapePress);
      document.removeEventListener("focusout", handleFocusOut);
    };
  }, [showForm]);

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
              ref={inputRef}
              autoComplete="off"
              borderColor="focus:border-nord-polar-night-light"
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

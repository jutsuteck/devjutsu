import { FC, useState } from "react";
import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "react-query";
import Image from "next/image";

import BaseModal from "../ui/BaseModal";
import FormGroup from "../forms/FormGroup";
import CustomInput from "../forms/CustomInput";
import CustomTextArea from "../forms/CustomTextArea";
import Button from "../ui/Button";
import Alert from "../ui/Alert";

import { Methodology, NewProject } from "@/models/projects";

import projectService from "@/services/projects/ProjectService";

import { LuRocket } from "react-icons/lu";

interface Props {
  onClose?: () => void;
}

interface FormProps {
  name: string;
  description?: string;
}

const NewProjectModal: FC<Props> = ({ onClose }) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormProps>({
    mode: "onChange",
  });
  const [selectedMethodology, setSelectedMethodology] = useState<Methodology>(
    Methodology.SCRUM
  );
  const [errMessage, setErrMessage] = useState(null);

  const queryClient = useQueryClient();

  const mutation = useMutation((data: NewProject) =>
    projectService.createProject(data.name, data.description, data.methodology)
  );

  const onSubmit = (formData: FormProps) => {
    const data: NewProject = {
      methodology: selectedMethodology,
      ...formData,
    };

    mutation.mutate(data, {
      onSuccess: () => {
        queryClient.invalidateQueries(["projects"]);
        setErrMessage(null);
        onClose && onClose();
      },
      onError: (error: any) => {
        setErrMessage(error);
      },
    });
  };

  return (
    <BaseModal onClose={onClose} maxSize="xl">
      {mutation.isError && <Alert message={errMessage} severity="error" />}
      <h1 className="mb-2 text-lg font-extrabold flex items-center">
        <LuRocket />
        <span className="ml-2">Create a new project</span>
      </h1>
      <p className="text-nord-polar-night-lightest">
        Turn your code dreams into secure realities, one project at a time.
      </p>
      <form onSubmit={handleSubmit(onSubmit)} className="my-4">
        <FormGroup label="Name" labelStyle="font-extrabold">
          <CustomInput
            name="name"
            placeholder="Enter project name ..."
            register={register}
            autoComplete="off"
            bgColor="bg-nord-polar-night-medium"
            borderColor="border-nord-polar-night-light"
            error={errors.name?.message}
          />
        </FormGroup>
        <FormGroup label="Description" labelStyle="font-extrabold">
          <CustomTextArea
            placeholder="Legend has it, this project will change everything. Dive in ..."
            name="description"
            register={register}
            bgColor="bg-nord-polar-night-medium"
            borderColor="border-nord-polar-night-light"
            error={errors.description?.message}
            autoFocus={false}
          />
        </FormGroup>
        <FormGroup label="Methodology" labelStyle="font-extrabold">
          <div className="flex items-center space-x-4">
            <div
              onClick={() => setSelectedMethodology(Methodology.SCRUM)}
              className={`${
                selectedMethodology === Methodology.SCRUM
                  ? "border-nord-frost-medium border-2 shadow-md"
                  : "border-nord-polar-night-light"
              } cursor-pointer flex flex-col items-center justify-center w-1/2 p-6 rounded-md border-2`}
            >
              <h1 className="font-bold mb-2">Scrum</h1>
              <Image
                src="/icons/scrum.svg"
                alt="scrum"
                width={100}
                height={100}
              />
            </div>
            <div
              onClick={() => setSelectedMethodology(Methodology.KANBAN)}
              className={`${
                selectedMethodology === Methodology.KANBAN
                  ? "border-nord-frost-medium border-2 shadow-md"
                  : "border-nord-polar-night-light"
              } cursor-pointer flex flex-col items-center justify-center w-1/2 p-6 rounded-md border-2`}
            >
              <h1 className="font-bold mb-2">Kanban</h1>
              <Image
                src="/icons/kanban.svg"
                alt="scrum"
                width={100}
                height={100}
              />
            </div>
          </div>
        </FormGroup>
        <Button
          icon={<LuRocket />}
          text="Launch project"
          type="submit"
          bgFrost
        />
      </form>
    </BaseModal>
  );
};

export default NewProjectModal;

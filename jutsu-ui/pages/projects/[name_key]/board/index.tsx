import { useState } from "react";
import { NextPage } from "next";
import { useRouter } from "next/router";

import Dashboard from "@/components/layout/Dashboard";
import StateList from "@/components/projects/board/StateList";
import NewStateForm from "@/components/projects/board/NewStateForm";
import Alert from "@/components/ui/Alert";

import useCurrentWorkflow from "@/hooks/projects/useCurrentWorkflow";
import useProjectDetail from "@/hooks/projects/useProjectDetail";

import { FaTableList } from "react-icons/fa6";
import { PiKanbanFill } from "react-icons/pi";
import { LiaLaptopCodeSolid } from "react-icons/lia";

const ProjectBoardPage: NextPage = () => {
  const router = useRouter();
  const [successMsg, setSuccessMsg] = useState<string | null>(null);
  const [errMsg, setErrMsg] = useState<string | null>(null);
  const { projectId } = router.query;
  const {
    data: currentWorkflow,
    isLoading: isCurrentWorkflowLoading,
    isError: isCurrentWorkflowError,
  } = useCurrentWorkflow(projectId);
  const {
    data: project,
    isLoading: projectLoading,
    isError: projectError,
  } = useProjectDetail(projectId);

  return (
    <>
      {errMsg && <Alert message={errMsg} severity="error" />}
      {successMsg && <Alert message={successMsg} severity="success" />}
      <Dashboard
        projectId={projectId}
        pageName="Board"
        isScrum
        scrumHeader={currentWorkflow?.name}
      >
        <div className="flex justify-between mt-8">
          <div className="flex space-x-3">
            {/* Table Button */}
            <button className="bg-nord-polar-night-medium rounded-lg p-2 shadow-md">
              <FaTableList size={15} />
            </button>

            {/* Kanban Button */}
            <button className="bg-nord-polar-night-medium rounded-lg p-2 shadow-md">
              <PiKanbanFill size={15} />
            </button>
            {/* State Button and Form */}
            <NewStateForm
              workflowId={currentWorkflow?.id}
              successMsg={successMsg}
              errMsg={errMsg}
              setSuccessMsg={setSuccessMsg}
              setErrMsg={setErrMsg}
            />
          </div>

          {/* Add Column Button */}
          <button className="bg-nord-polar-night-medium rounded-lg py-2 px-4 shadow-md flex items-center justify-center">
            <LiaLaptopCodeSolid size={20} />
            <span className="ml-2 font-semibold">Create work</span>
          </button>
        </div>

        <StateList workflowId={currentWorkflow?.id} />
      </Dashboard>
    </>
  );
};

export default ProjectBoardPage;

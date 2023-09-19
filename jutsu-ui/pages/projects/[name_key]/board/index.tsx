import { NextPage } from "next";
import { useRouter } from "next/router";
import { FaTableList } from "react-icons/fa6";
import { PiKanbanFill } from "react-icons/pi";
import { GrAdd } from "react-icons/gr";

import Dashboard from "@/components/layout/Dashboard";
import StateList from "@/components/projects/board/StateList";
import Alert from "@/components/ui/Alert";
import useCurrentWorkflow from "@/hooks/projects/useCurrentWorkflow";
import useProjectDetail from "@/hooks/projects/useProjectDetail";

const ProjectBoardPage: NextPage = () => {
  const router = useRouter();
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

  console.log(isCurrentWorkflowError);

  return (
    <Dashboard
      projectId={projectId}
      pageName="Board"
      isScrum
      scrumHeader={currentWorkflow?.name}
    >
      {isCurrentWorkflowError && (
        <Alert message={isCurrentWorkflowError} severity="error" />
      )}
      <div className="flex justify-between mt-8">
        <div className="space-x-3">
          {/* Table Button */}
          <button className="bg-nord-polar-night-medium rounded-lg p-2 shadow-md">
            <FaTableList size={15} />
          </button>
          {/* Kanban Button */}
          <button className="bg-nord-polar-night-medium rounded-lg p-2 shadow-md">
            <PiKanbanFill size={15} />
          </button>
        </div>
        <button className="bg-nord-polar-night-medium rounded-lg py-2 px-4 shadow-md flex flex items-center justify-center">
          <GrAdd />
          <span className="ml-2 font-semibold"> Add column </span>
        </button>
      </div>
      <StateList workflowId={currentWorkflow?.id} />
    </Dashboard>
  );
};

export default ProjectBoardPage;

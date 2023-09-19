import { FC, ReactNode } from "react";
import Sidebar from "./Sidebar";
import useProjectDetail from "@/hooks/projects/useProjectDetail";
import Header from "./Header";
import TopBar from "../ui/TopBar";

interface Props {
  children: ReactNode;
  projectId: string;
  pageName: string;
  headerButton?: boolean;
  headerButtonText?: string;
  headerButtonAction?: () => void;
  isScrum?: boolean;
  scrumHeader?: string | ReactNode;
}

const Dashboard: FC<Props> = ({
  children,
  projectId,
  pageName,
  headerButton,
  headerButtonText,
  headerButtonAction,
  isScrum,
  scrumHeader,
}) => {
  const { data: project, isLoading, isError } = useProjectDetail(projectId);

  return (
    <div className="flex flex-col h-full">
      <TopBar />
      <div className="flex h-full">
        <Sidebar projectId={projectId} />
        <div className="flex-grow p-8">
          <Header
            projectName={project?.name}
            pageName={pageName}
            hasButton={headerButton}
            headerButton={headerButtonText}
            onClick={headerButtonAction}
            isScrum={isScrum}
            scrumHeader={scrumHeader}
          />
          {children}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;

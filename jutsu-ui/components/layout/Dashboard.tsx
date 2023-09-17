import { FC, ReactNode } from "react";
import Sidebar from "./Sidebar";

interface Props {
  children: ReactNode;
  projectId: string;
}

const Dashboard: FC<Props> = ({ children, projectId }) => {
  return (
    <>
      <Sidebar projectId={projectId} />
      {children}
    </>
  );
};

export default Dashboard;

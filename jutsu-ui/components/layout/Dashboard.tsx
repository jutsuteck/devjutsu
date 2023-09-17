import { FC, ReactNode } from "react";
import Sidebar from "./Sidebar";

interface Props {
  children: ReactNode;
}

const Dashboard: FC<Props> = ({ children }) => {
  return (
      <>
        <Sidebar />
        {children}
      </>
      )
}

export default Dashboard;

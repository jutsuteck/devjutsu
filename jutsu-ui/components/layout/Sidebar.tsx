import useProjectDetail from "@/hooks/projects/useProjectDetail";
import { FC, useState } from "react";
import SidebarLink from "./SidebarLink";
import { AiFillBook } from "react-icons/ai";
import { PiKanbanFill } from "react-icons/pi";

interface Props {
  projectId: string;
}

const Sidebar: FC<Props> = ({ projectId }) => {
  const { data: project, isLoading, isError } = useProjectDetail(projectId);
  const [isLinkHovered, setIsLinkHovered] = useState<boolean>(false);

  return (
    <div className="flex flex-col h-full w-64 p-8 space-y-4">
      <nav className="flex flex-col space-y-2">
        <SidebarLink
          name="Journal"
          icon={<AiFillBook />}
          projectId={project?.id}
          projectNameKey={project?.name_key}
          isHovered={isLinkHovered}
          setIsHovered={setIsLinkHovered}
        />
        <SidebarLink
          name="Board"
          icon={<PiKanbanFill />}
          projectId={project?.id}
          projectNameKey={project?.name_key}
          isHovered={isLinkHovered}
          setIsHovered={setIsLinkHovered}
        />
      </nav>
    </div>
  );
};

export default Sidebar;

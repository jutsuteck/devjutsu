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
      <div className="space-y-2">
        <div className="flex items-center justify-center">
          <img src="/icons/rocket.svg" alt="Rocket" className="w-100 h-100" />
        </div>
        <div className="text-center">
          <h1 className="text-2xl font-extrabold">{project?.name_key}</h1>
          <h2 className="text-lg font-semibold text-nord-polar-night-light">
            {project?.name}
          </h2>
          <p className="text-xs font-semibold p-2 text-nord-polar-night-light">
            {project?.methodology.toUpperCase()} Project
          </p>
        </div>
      </div>
      <hr className="w-2/4 mx-auto border-t border-nord-polar-night-medium" />
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

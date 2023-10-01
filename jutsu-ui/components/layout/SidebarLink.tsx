import Link from "next/link";
import { useRouter } from "next/router";
import { FC, ReactNode } from "react";

interface Props {
  projectId?: string;
  projectNameKey?: string;
  name: string;
  icon: ReactNode;
  isHovered: boolean;
  setIsHovered: (value: boolean) => void; // Corrected type here
}

const SidebarLink: FC<Props> = ({
  name,
  projectId,
  projectNameKey,
  icon,
  isHovered,
  setIsHovered,
}) => {
  const router = useRouter();
  const isActive =
    router.asPath ===
    `/projects/${projectNameKey}/${name.toLowerCase()}?projectId=${projectId}`;

  const baseClasses = "font-sm py-2 rounded-full text-sm";
  const activeClasses =
    isActive && !isHovered
      ? "text-nord-frost-dark bg-nord-frost-medium font-semibold"
      : "";
  const hoverClasses =
    "hover:bg-nord-frost-medium hover:text-nord-frost-dark font-semibold transition-colors duration-300";

  const finalClasses = `${baseClasses} ${activeClasses} ${hoverClasses}`;

  return (
    <Link
      href={{
        pathname: `/projects/${projectNameKey}/${name.toLowerCase()}`,
        query: { projectId: projectId },
      }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className={`${finalClasses} flex items-center justify-center`}
    >
      {icon}
      <span className="ml-2">{name}</span>{" "}
      {/* Optional: Add some margin between the icon and the name */}
    </Link>
  );
};

export default SidebarLink;

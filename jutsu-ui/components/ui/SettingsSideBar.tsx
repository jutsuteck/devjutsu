import { FC, useState } from "react";
import SidebarLink from "../layout/SidebarLink";

import { RiUserSettingsLine } from "react-icons/ri";

const SettingsSideBar: FC = () => {
  const [isLinkHovered, setIsLinkHovered] = useState<boolean>(false);

  return (
    <nav className="flex flex-col h-full w-64">
      <SidebarLink
        name="Account"
        icon={<RiUserSettingsLine />}
        isHovered={isLinkHovered}
        setIsHovered={setIsLinkHovered}
      />
    </nav>
  );
};

export default SettingsSideBar;

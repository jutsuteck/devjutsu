import { FC } from "react";
import { LuRocket, LuSchool } from "react-icons/lu";
import TopBarLink from "./TopBarLink";
import UserProfileMenu from "./UserProfileMenu";

const TopBar: FC = () => {
  return (
    <div className="w-full mb-2 bg-nord-polar-night-darkest">
      {/* Top section */}
      <div className="flex justify-between items-center py-4 px-8">
        <div className="flex items-center space-x-4 py-2">
          <img src="/icons/dummy-logo.svg" alt="Logo" className="w-10 h-10" />
          <span className="font-semibold">Tenant Name</span>
        </div>

        <UserProfileMenu />
      </div>

      {/* Bottom section */}
      <div className="flex items-center py-2 px-8 space-x-4">
        <TopBarLink href="/projects" icon={<LuRocket />} name="Projects" />
        <TopBarLink href="/dojo" icon={<LuSchool />} name="Dojo" />
      </div>
    </div>
  );
};

export default TopBar;

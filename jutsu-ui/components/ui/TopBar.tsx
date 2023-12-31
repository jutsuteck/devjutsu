import { FC } from "react";
import { LuRocket, LuSchool } from "react-icons/lu";
import { BiCheckShield } from "react-icons/bi";

import TopBarLink from "./TopBarLink";
import UserProfileMenu from "./UserProfileMenu";
import { useRouter } from "next/router";
import Image from "next/image";
import useCurrentUser from "@/hooks/users/useCurrentUser";

interface Props {
  showBottomSection?: boolean;
  title?: string;
}

const TopBar: FC<Props> = ({ showBottomSection = true, title }) => {
  const router = useRouter();
  const { data: currentUser, isLoading, isError } = useCurrentUser();

  return (
    <div
      className={`w-full mb-2 transition duration-500 ease-in-out bg-nord-polar-night-darkest`}
    >
      {/* Top section */}
      <div className="flex justify-between items-center py-4 px-8">
        <div className="flex items-center space-x-4 py-2">
          <Image
            src="/icons/dummy-logo.svg"
            alt="Logo"
            height={35}
            width={35}
            onClick={() => router.push("/projects")}
            className="cursor-pointer"
          />
          <span className="font-semibold">
            {title ? title : `Devjutsu / ${currentUser?.name}`}
          </span>
        </div>

        <UserProfileMenu />
      </div>

      {/* Bottom section */}
      <div
        className={`transition-all duration-500 ease-in-out overflow-hidden ${
          showBottomSection ? "h-auto" : "h-0"
        }`}
      >
        {showBottomSection && (
          <div className="flex items-center py-2 px-8 space-x-4">
            <TopBarLink href="/projects" icon={<LuRocket />} name="Projects" />
            <TopBarLink href="/dojo" icon={<LuSchool />} name="Dojo" />
            <TopBarLink
              href="/security-checklists"
              icon={<BiCheckShield />}
              name="Security Checklists"
            />
          </div>
        )}
      </div>
    </div>
  );
};

export default TopBar;

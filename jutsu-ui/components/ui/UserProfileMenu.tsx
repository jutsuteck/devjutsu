import Link from "next/link";
import Image from "next/image";

import { FC, useState } from "react";
import { motion } from "framer-motion";

import { useAuth } from "@/hooks/auth/useAuth";
import useCurrentUser from "@/hooks/users/useCurrentUser";

import Button from "./Button";

import { AiOutlineLogout } from "react-icons/ai";
import { RiUserSettingsLine } from "react-icons/ri";

const UserProfileMenu: FC = () => {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const { logout, token } = useAuth();
  const { data: currentUser, isLoading, isError } = useCurrentUser();

  const username = `${currentUser?.first_name} ${currentUser?.last_name}`;

  const sidebarVariants = {
    open: { x: 0 },
    closed: { x: "100%" },
  };

  const onClickLogout = () => {
    logout();
  };

  return (
    <div className="relative">
      {/* User avatar */}
      <div onClick={() => setIsOpen(!isOpen)}>
        <Image
          src="https://robohash.org/samurai"
          alt="avatar"
          className="rounded-full border-nord-snowstorm-light border-2 hover:cursor-pointer"
          height={40}
          width={40}
        />
      </div>

      {/* Overlay Menu */}
      {isOpen && (
        <>
          {/* Blur Overlay */}
          <div
            className="fixed inset-0 bg-nord-polar-night-medium opacity-50 backdrop-blur-lg z-40"
            onClick={() => setIsOpen(false)}
          ></div>

          {/* User Menu */}
          <motion.div
            initial="closed"
            animate={isOpen ? "open" : "closed"}
            variants={sidebarVariants}
            transition={{ type: "spring", stiffness: 300, damping: 30 }}
            className="fixed top-0 right-0 w-80 h-full bg-nord-polar-night-darkest z-50 rounded-lg border-l border-nord-polar-night-medium shadow-2xl"
          >
            {/* Overlay Header */}
            <div className="flex items-center p-4">
              <Image
                src="https://robohash.org/samurai"
                alt="avatar"
                className="rounded-full mr-4 border-nord-snowstorm-light border-2"
                height={40}
                width={40}
              />
              <div className="ml-2">
                <h1 className="font-bold">Tenant name</h1>
                <h2>{isLoading ? "Loading..." : `${currentUser?.name}`}</h2>
              </div>
            </div>

            <div className="p-4">
              <Link
                href="/settings/profile"
                className="flex items-center transition-colors duration-3000 rounded-md p-2 hover:bg-nord-polar-night-dark"
              >
                <RiUserSettingsLine />
                <span className="ml-4">Settings</span>
              </Link>
            </div>

            <div className="absolute bottom-0 w-full p-4">
              <Button
                fullWidth
                icon={<AiOutlineLogout />}
                text="Logout"
                onClick={onClickLogout}
                bgFrost
              />
            </div>
          </motion.div>
        </>
      )}
    </div>
  );
};

export default UserProfileMenu;

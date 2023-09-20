import Image from "next/image";
import { FC, useState } from "react";
import { motion } from "framer-motion";
import { AiOutlineLogout } from "react-icons/ai";
import Button from "./Button";
import { useAuth } from "@/hooks/auth/useAuth";

const UserProfileMenu: FC = () => {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const { logout, token } = useAuth();

  const sidebarVariants = {
    open: { x: 0 },
    closed: { x: "100%" },
  };

  const onClickLogout = () => {
    console.log(token);
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
                <h2>Username</h2>
              </div>
            </div>

            <div className="p-4">
              <span>Settings</span>
            </div>

            <div className="absolute bottom-0 w-full p-4">
              <Button
                fullWidth
                icon={<AiOutlineLogout />}
                text="Logout"
                onClick={onClickLogout}
              />
            </div>
          </motion.div>
        </>
      )}
    </div>
  );
};

export default UserProfileMenu;

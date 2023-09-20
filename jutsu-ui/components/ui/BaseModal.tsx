import { FC, ReactNode } from "react";
import { motion } from "framer-motion";

interface Props {
  children: ReactNode;
  maxSize?: "xs" | "sm" | "md" | "lg" | "xl" | "2xl";
  className?: string;
  onClose?: () => void; // Callback function to handle modal close
}

const sizeClasses = {
  xs: "max-w-xs",
  sm: "max-w-sm",
  md: "max-w-md",
  lg: "max-w-lg",
  xl: "max-w-xl",
  "2xl": "max-w-2xl",
};

const BaseModal: FC<Props> = ({
  children,
  maxSize = "md",
  className,
  onClose,
}) => {
  return (
    <div className="fixed inset-0 flex items-center justify-center z-50">
      {/* Pixelated Background */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        className="absolute inset-0 bg-black bg-opacity-50 backdrop-filter backdrop-blur-md"
        onClick={onClose} // Close modal when background is clicked
      ></motion.div>

      {/* Modal Content */}
      <div className="relative z-10">
        {" "}
        {/* This container ensures the modal content is above the pixelated background */}
        <motion.div
          initial={{ opacity: 0, y: -50 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 50 }}
          className={`${sizeClasses[maxSize]} ${className} bg-nord-polar-night-medium shadow-xl rounded-lg p-6`}
        >
          {children}
        </motion.div>
      </div>
    </div>
  );
};

export default BaseModal;

import { FC, useState } from "react";
import {
  AiOutlineCheckCircle,
  AiOutlineExclamationCircle,
  AiOutlineInfoCircle,
  AiOutlineWarning,
} from "react-icons/ai";
import { motion } from "framer-motion";

interface Props {
  message: string;
  severity: "error" | "warning" | "info" | "success";
  maxSize?: "sm" | "md" | "lg" | "xl" | "2xl";
}

const sizeClasses = {
  sm: "max-w-sm",
  md: "max-w-md",
  lg: "max-w-lg",
  xl: "max-w-xl",
  "2xl": "max-w-2xl",
};

const severityClasses = {
  error: "bg-nord-aurora-red",
  warning: "bg-nord-golden",
  info: "bg-nord-frost-medium",
  success: "bg-nord-meaduw",
};

const icons = {
  error: <AiOutlineExclamationCircle className="mr-2" />,
  warning: <AiOutlineWarning className="mr-2" />,
  info: <AiOutlineInfoCircle className="mr-2" />,
  success: <AiOutlineCheckCircle className="mr-2" />,
};

const fadeIn = {
  hidden: { opacity: 0 },
  visible: { opacity: 1 },
};

const Alert: FC<Props> = ({ message, severity, maxSize = "md" }) => {
  const [isVisible, setIsVisble] = useState(true);

  if (!isVisible) return null;

  return (
    <motion.div
      initial="hidden"
      animate="visible"
      variants={fadeIn}
      className={`text-white p-2 rounded-md w-full text-center cursor-pointer ${severityClasses[severity]} ${sizeClasses[maxSize]}`}
      onClick={() => setIsVisble(false)}
    >
      <div className="flex items-center justify-center">
        {severity === "error" && icons.error}
        {severity === "warning" && icons.warning}
        {severity === "info" && icons.info}
        {severity === "success" && icons.success}
        {message}
      </div>
    </motion.div>
  );
};

export default Alert;

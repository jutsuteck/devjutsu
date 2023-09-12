import { FC, ReactNode } from "react";

interface Props {
  children: ReactNode;
}

const CenteredContainer: FC<Props> = ({ children }) => {
  return (
    <div className="min-h-screen flex items-center justify-center">
      {children}
    </div>
  );
};

export default CenteredContainer;

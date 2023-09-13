import { FC, ReactNode } from "react";

interface Props {
  children: ReactNode;
  flexCol?: boolean;
}

const CenteredContainer: FC<Props> = ({ children, flexCol }) => {
  return (
    <div
      className={`min-h-screen flex items-center justify-center ${
        flexCol ? "flex-col" : ""
      }`}
    >
      {children}
    </div>
  );
};

export default CenteredContainer;
